#tableau de tuple a 5 dimentions (niveau,((x, y), (longueur, hauteur))) de taille variable 
rectangle_array = []
ids = 0

def append_array(z, rect, draw, exec):
    global ids
    
    rectangle_array.append((z, ids, rect, draw, exec))
    ids += 1
    return ids - 1 

def remove_array(elem):
    rectangle_array.remove(elem)

def sort_array():
    rectangle_array.sort()

def reverse_array():
    rectangle_array.sort(reverse=True)

def find(ids):
    for rect in rectangle_array:
        if ids == rect[1]:
            return rect
    return None

def draw_all_rect():
    sort_array()
    for rect in rectangle_array:
        rect[3](rect[2])

def isInRectangle(pos, rect):
    return pos[0] < rect[0][0] + rect[1][0] and pos[0] > rect[0][0]\
        and pos[1] < rect[0][1] + rect[1][1] and pos[0] > rect[0][1]

def exec_click(pos):
    reverse_array()
    print(rectangle_array)
    for rect in rectangle_array:
        if isInRectangle(pos, rect[2]):
            rect[4]()
            return

