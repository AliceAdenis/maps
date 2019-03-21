from .color_gradient import linear_gradient, polylinear_gradient


def get_colors(list_vals, list_colors=["#fb4747", "#315ace", "#b5f6e5", "#FFB347"]):
    dict_colors = {}
    dict_colors['hex'] = []
    i = 0
    while len(dict_colors['hex']) < len(list_vals):
        dict_colors = polylinear_gradient(list_colors, n=i+len(list_vals))
        i += 1

    dict_colors_ok = {}
    for i, val in enumerate(list_vals):
        dict_colors_ok[val] = dict_colors['hex'][i]

    return dict_colors_ok




