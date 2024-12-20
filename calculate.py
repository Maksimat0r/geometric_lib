figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'area-circle': 1,
    'perimeter-circle': 1,
    'area-square': 1,
    'perimeter-square': 1,
    'area-triangle': 3,
    'perimeter-triangle': 3,
}


def calc(fig, func, size):
    assert fig in figs, "Invalid figure"
    assert func in funcs, "Invalid function"
    result = eval(f'{fig}.{func}(*{size})')
    return result
