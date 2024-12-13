import pygame
from signal import signal, SIGINT
from utils.caller import call

class Window:
	def __init__(self, *,
		name,
		resolution,
		framerate,
		setup		= lambda: None,
		tick		= lambda: None,
		handleEvent	= lambda event: None,
		leftClick	= lambda: None,
		rightClick	= lambda: None,
		repeatKey	= lambda key: None,
		singleKey	= lambda key: None,
	):
		self._done = False
		self._framerate = framerate

		self.mouse_position = (0, 0)
		self.repeatKeyMap = {}
		self.fonts = {}
		self.images = {}

		self.instance = 0
		self._is_fullscreen = False
		self.resolution = resolution
		self._windowed_resolution = resolution

		if not all(callable(func) for func in (setup, tick, handleEvent, leftClick, rightClick, repeatKey, singleKey)):
			raise ValueError("function passed in Window is not callable")
		self._setup_func			= setup
		self._tick_func				= tick
		self._handle_events_func	= handleEvent
		self._left_click			= leftClick
		self._right_click			= rightClick
		self._repeat_key_func		= repeatKey
		self._single_key_func		= singleKey

		pygame.init()
		signal(SIGINT, lambda signal, frame: self.stop())
		pygame.display.set_caption(name)
		self._update_window()

	def start(self):
		call(self._setup_func, window=self)
		self.time = pygame.time.Clock()
		while not self._done:
			self._handle_events()
			call(self._tick_func, window=self, time=pygame.time.get_ticks())
			pygame.display.flip()
			self.time.tick(self._framerate)
		pygame.display.quit()
		pygame.quit()

	def stop(self):
		self._done = True

	def _handle_events(self):
		for event in pygame.event.get():
			match event.type:
				case pygame.QUIT:
					self.stop()

				case pygame.KEYDOWN:
					self._single_key_func(event.key)
					self.repeatKeyMap[event.key] = True
				case pygame.KEYUP:
					self.repeatKeyMap[event.key] = False

				case pygame.WINDOWRESIZED:
					self._update_resolution((event.x, event.y))
				case pygame.WINDOWSIZECHANGED:
					self._update_resolution((event.x, event.y))
							
				case pygame.MOUSEMOTION:
					self.mouse_position = event.pos
				
				case pygame.MOUSEBUTTONUP:
					match event.button:
						case 1:
							call(self._left_click, window=self, pos=self.mouse_position)
						case 3:
							call(self._right_click, window=self, pos=self.mouse_position)

			self._handle_events_func(event)

		for (key, is_pressed) in self.repeatKeyMap.items():
			if not is_pressed:
				continue
			self._repeat_key_func(key)



	def _update_resolution(self, coord):
		self.resolution = coord
		self._update_window()


	def toggleFullscreen(self):
		if (not self._is_fullscreen):
			self._windowed_resolution = self.resolution
		else:
			self.resolution = self._windowed_resolution
		self._is_fullscreen = not self._is_fullscreen
		self._update_window()
		
	def _update_window(self):
		if (self._is_fullscreen):
			self.instance = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.NOFRAME)
		else:
			self.instance = pygame.display.set_mode(self.resolution, pygame.RESIZABLE)





	def load_font(self, id, name, size, bold = False):
		self.fonts[id] = pygame.font.SysFont(name, size, bold)

	def load_image(self, key, path):
		self.images[key] = pygame.image.load(path).convert_alpha(self.instance)

	def draw_rect(self, rect, color, rounding = 0, outline = 0):
		pygame.draw.rect(self.instance, color, rect, outline, rounding)

	# anchor can be one of the following:
	# topleft, bottomleft, topright, bottomright
	# midtop, midleft, midbottom, midright
	# center, centerx, centery
	def draw_text(
		self,
		fontId: str,
		coord,
		text: str,
		color,
		anchor: str = "topleft"
	):
		font = self.fonts.get(fontId) # type: pygame.font.Font
		if font is None:
			raise ValueError(f"Font {fontId} not loaded")
		text_prepared = font.render(text, True, color)
		rect = text_prepared.get_rect()
		setattr(rect, anchor, coord)
		self.instance.blit(text_prepared, rect)

	def draw_image(self, image_key, rect):
		img_inst = self.images[image_key]
		img = pygame.transform.scale(img_inst, rect[1])
		self.instance.blit(img, rect[0])


