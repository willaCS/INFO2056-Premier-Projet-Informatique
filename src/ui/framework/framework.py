emptyLambda = lambda: None

def component(
	rect,
	margin=0,
	padding=0,
	z=0,
	draw=emptyLambda,
	click=emptyLambda,
	clickOutside=emptyLambda,
	childs=[]
):
	res = {
		'_rect': rect,
		'margin': margin,
		'padding': padding,
		'z': z,

		'_draw': draw,
		'_click': click,
		'_clickOutside': clickOutside,

		'_hidden': False,
		'_temp': False,

		'_parent': None,
		'_childs': childs,
	}

	for child in res['_childs']:
		component_add_parent(child, res)
	return res
	
def component_show(component):
	component['_hidden'] = False

def component_hide(component):
	component['_hidden'] = True





def _component_baseRect(component, parent_rect):
	if callable(component['_rect']):
		if component['_parent'] and component['_rect'].__code__.co_argcount >= 1:
			return component['_rect'](parent_rect)
		else:
			return component['_rect']()
	else:
		return component['_rect']


def component_rect(component):
	parent = component_child_rect(component['_parent']) if component['_parent'] else ((0, 0), (0, 0))
	base = _component_baseRect(component, parent)
	# print('base',base, component)
	return (
		(
			parent[0][0] + base[0][0] + component['margin'],
			parent[0][1] + base[0][1] + component['margin'],
		),
		(
			base[1][0] - 2 * component['margin'],
			base[1][1] - 2 * component['margin'],
		),
	)

def component_child_rect(component):
	parent = component_child_rect(component['_parent']) if component['_parent'] else ((0, 0), (0, 0))
	base = _component_baseRect(component, parent)
	return (
		(
			parent[0][0] + base[0][0] + component['margin'] + component['padding'],
			parent[0][1] + base[0][1] + component['margin'] + component['padding'],
		),
		(
			base[1][0] - 2 * (component['padding'] + component['margin']),
			base[1][1] - 2 * (component['padding'] + component['margin']),
		),
	)
	






def component_draw(component, mouse_position):
	if component['_hidden']:
		return	
	rect = component_rect(component)
	if component['_draw'].__code__.co_argcount >= 2:
		component['_draw'](rect, component_is_in(component, mouse_position))
	else:
		component['_draw'](rect)
	component['_childs'].sort(key=lambda c: c['z'])
	for child in component['_childs']:
		component_draw(child, mouse_position)

def component_is_in(component, pos):
	rect = component_rect(component)
	return rect[0][0] <= pos[0] <= rect[0][0] + rect[1][0]\
		and rect[0][1] <= pos[1] <= rect[0][1] + rect[1][1]

def component_click(component, pos, has_already_clicked=False):
	if component['_hidden']:
		return False
	component['_childs'].sort(key=lambda c: c['z'], reverse=True)
	for child in component['_childs']:
		if component_click(child, pos, has_already_clicked):
			has_already_clicked = True
	if component['_click'] is not None and component_is_in(component, pos):
		if has_already_clicked:
			return has_already_clicked
		has_already_clicked = True
		if component['_click'].__code__.co_argcount >= 1:
			component['_click'](pos)
		else:
			component['_click']()
	else:
		if component['_clickOutside'].__code__.co_argcount >= 1:
			component['_clickOutside'](pos)
		else:
			component['_clickOutside']()
	return has_already_clicked

def component_add_parent(component, parent):
	component['_parent'] = parent
