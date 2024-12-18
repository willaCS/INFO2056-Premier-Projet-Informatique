from typing import List


emptyLambda = lambda: None

class Component:
	def __init__(self,
		rect,
		margin=0,
		padding=0,
		z=0,
		draw=emptyLambda,
		click=emptyLambda,
		clickOutside=emptyLambda,
		childs=[] # type: List[Component]
	):
		self._rect = rect
		self.margin = margin
		self.padding = padding
		self.z = z

		self._draw = draw
		self._click = click
		self._clickOutside = clickOutside

		self._hidden = False
		self._temp = False

		self._parent = None # type: Component
		self._childs = childs # type: List[Component]
		for child in self._childs:
			child.add_parent(self)
	
	def show(self):
		self._hidden = False

	def hide(self):
		self._hidden = True

	def _baseRect(self, parent_rect):
		if callable(self._rect):
			if self._parent and self._rect.__code__.co_argcount >= 1:
				return self._rect(parent_rect)
			else:
				return self._rect()
		else:
			return self._rect
	
	def rect(self):
		parent = self._parent.child_rect() if self._parent else ((0, 0), (0, 0))
		base = self._baseRect(parent)
		return (
			(
				parent[0][0] + base[0][0] + self.margin,
				parent[0][1] + base[0][1] + self.margin,
			),
			(
				base[1][0] - 2 * self.margin,
				base[1][1] - 2 * self.margin,
			),
		)
	
	def child_rect(self):
		parent = self._parent.child_rect() if self._parent else ((0, 0), (0, 0))
		base = self._baseRect(parent)
		return (
			(
				parent[0][0] + base[0][0] + self.margin + self.padding,
				parent[0][1] + base[0][1] + self.margin + self.padding,
			),
			(
				base[1][0] - 2 * (self.padding + self.margin),
				base[1][1] - 2 * (self.padding + self.margin),
			),
		)
	
	def draw(self, mouse_position):
		if self._hidden:
			return	
		rect = self.rect()
		if self._draw.__code__.co_argcount >= 2:
			self._draw(rect, self.is_in(mouse_position))
		else:
			self._draw(rect)
		self._childs.sort(key=lambda c: c.z)
		for child in self._childs:
			child.draw(mouse_position)


	def is_in(self, pos):
		rect = self.rect()
		return rect[0][0] <= pos[0] <= rect[0][0] + rect[1][0]\
			and rect[0][1] <= pos[1] <= rect[0][1] + rect[1][1]

	def click(self, pos, has_already_clicked=False):
		if self._hidden:
			return False
		self._childs.sort(key=lambda c: c.z, reverse=True)
		for child in self._childs:
			if child.click(pos, has_already_clicked):
				has_already_clicked = True
		if self._click is not None and self.is_in(pos):
			if has_already_clicked:
				return has_already_clicked
			has_already_clicked = True
			if self._click.__code__.co_argcount >= 1:
				self._click(pos)
			else:
				self._click()
		else:
			if self._clickOutside.__code__.co_argcount >= 1:
				self._clickOutside(pos)
			else:
				self._clickOutside()
		return has_already_clicked

	def add_parent(self, parent):
		self._parent = parent

	def add_temp(self,
		new_childs # type: List[Component]
	):  
		for child in new_childs:
			if not child:
				continue
			child._temp = True
			self._childs.append(child)
			child.add_parent(self)

	def temp_remove(self):
		self._childs = [child for child in self._childs if not child._temp]