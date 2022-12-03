from datatypes import Feature


def new(n): return Feature(n, 0, 0)


FEATURES: dict[str, Feature] = {name: new(name) for name in [
    # Colors in the flag. At least what I can see in a picture I googled of all the flags :shrug:
    'red',
    'maroon',
    'brown',
    'white',
    'blue',
    'lightblue',
    'green',
    'lightgreen',
    'yellow',
    'black',

    # Structures within the flag.
    # for each star... I guess the USA needs to hope this is a good feature.
    'star',
    'dragon',
    'maple',
    'cross',
    'circle',
    'sun',
    'emblem',  # Any kind of coat of arms
    'arabic',  # any Arabic lettering
    'cresent',
    'sword',
    'bird',
    'crown',
    # Like those zig-zag patterns in Qatar and the diamond in Brazil.
    'angles',
    'flag',  # Did you know the Ecuadorian flag is within it's own flag?
    'latin',  # Any latin lettering
    'castel',  # Why does portugal need so many castles?

    # Orientations of the colors
    'vertical',
    'horizontal'
]}

# Load saved results of optimization
FEATURES = {k: Feature.from_json(v) for (k, v) in {'angles': {'angles': {'defensive_value': 3.116, 'offensive_value': -0.965}},
                                                   'arabic': {'arabic': {'defensive_value': 0.411, 'offensive_value': -0.7}},
                                                   'bird': {'bird': {'defensive_value': -2.172, 'offensive_value': 1.879}},
                                                   'black': {'black': {'defensive_value': -0.092, 'offensive_value': -0.286}},
                                                   'blue': {'blue': {'defensive_value': 0.178, 'offensive_value': 0.352}},
                                                   'brown': {'brown': {'defensive_value': 2.543, 'offensive_value': -2.438}},
                                                   'castel': {'castel': {'defensive_value': -0.125, 'offensive_value': 0.28}},
                                                   'circle': {'circle': {'defensive_value': -0.355, 'offensive_value': -0.46}},
                                                   'cresent': {'cresent': {'defensive_value': 1.075, 'offensive_value': -0.97}},
                                                   'cross': {'cross': {'defensive_value': -0.522, 'offensive_value': -0.2}},
                                                   'crown': {'crown': {'defensive_value': 0.044, 'offensive_value': 0.531}},
                                                   'dragon': {'dragon': {'defensive_value': -0.012, 'offensive_value': -1.68}},
                                                   'emblem': {'emblem': {'defensive_value': 0.78, 'offensive_value': -1.343}},
                                                   'flag': {'flag': {'defensive_value': 0.689, 'offensive_value': 0.888}},
                                                   'green': {'green': {'defensive_value': -0.543, 'offensive_value': -0.143}},
                                                   'horizontal': {'horizontal': {'defensive_value': -0.57,
                                                                                 'offensive_value': -0.679}},
                                                   'latin': {'latin': {'defensive_value': -1.495, 'offensive_value': -0.197}},
                                                   'lightblue': {'lightblue': {'defensive_value': -0.108,
                                                                               'offensive_value': 2.021}},
                                                   'lightgreen': {'lightgreen': {'defensive_value': -1.68,
                                                                                 'offensive_value': 0.899}},
                                                   'maple': {'maple': {'defensive_value': -1.16, 'offensive_value': -0.157}},
                                                   'maroon': {'maroon': {'defensive_value': -4.649, 'offensive_value': -0.622}},
                                                   'red': {'red': {'defensive_value': -0.539, 'offensive_value': -0.249}},
                                                   'star': {'star': {'defensive_value': 0.017, 'offensive_value': -0.029}},
                                                   'sun': {'sun': {'defensive_value': 0.418, 'offensive_value': -1.193}},
                                                   'sword': {'sword': {'defensive_value': -2.158, 'offensive_value': 0.082}},
                                                   'vertical': {'vertical': {'defensive_value': -0.402,
                                                                             'offensive_value': 0.013}},
                                                   'white': {'white': {'defensive_value': -0.32, 'offensive_value': 0.328}},
                                                   'yellow': {'yellow': {'defensive_value': -0.03, 'offensive_value': 0.09}}}.items()}
