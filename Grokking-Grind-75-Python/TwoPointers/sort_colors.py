def sort_colors(colors):
    red, white, blue = 0, 0, len(colors) - 1

    while white <= blue:
        if colors[white] == 0: 
            colors[red], colors[white] = colors[white], colors[red]
            red += 1
            white += 1
        elif colors[white] == 1: 
            white += 1
        else:  # Blue
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1

    return colors
