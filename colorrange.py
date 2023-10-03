def rangeparam(l_range,h_range,d) :
    if d>h_range:
        return "#FF0000"
    elif d<l_range:
        return "#1b9838"
    else:
        return "#FFA500"

# Red: #FF0000
#  Orange: #FFA500
#  Green: #1b9838