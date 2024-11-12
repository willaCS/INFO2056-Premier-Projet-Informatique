#tableau de tuple a 5 dimentions (niveau, x, y, longueur, hauteur) de taille variable 
rectangle_array = []
ids = 0

def append_array(height, coord_rectangle, size):
    global ids
    
    rectangle_array.append((height, coord_rectangle, size, ids))
    ids += 1
    return ids - 1

def remove_array(elem):
    rectangle_array.remove(elem)

def sort_array():
    rectangle_array.sort()

def find(ids):
    for rect in rectangle_array:
        if ids == rect[3]:
            return rect
    return None
