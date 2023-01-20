def catAndMouse(x, y, z):
    catA_distance = abs(z-x)
    catB_distance = abs(z-y)
    if catA_distance == catB_distance:
        return "Mouse C"
    elif catA_distance < catB_distance:
        return "Cat A"
    elif catB_distance < catA_distance:
        return "Cat B"
    