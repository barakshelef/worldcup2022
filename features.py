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
# Group stage
# FEATURES = {k: Feature.from_json(v) for (k, v) in {'angles': {'angles': {'defensive_value': 3.116, 'offensive_value': -0.965}},
#                                                    'arabic': {'arabic': {'defensive_value': 0.411, 'offensive_value': -0.7}},
#                                                    'bird': {'bird': {'defensive_value': -2.172, 'offensive_value': 1.879}},
#                                                    'black': {'black': {'defensive_value': -0.092, 'offensive_value': -0.286}},
#                                                    'blue': {'blue': {'defensive_value': 0.178, 'offensive_value': 0.352}},
#                                                    'brown': {'brown': {'defensive_value': 2.543, 'offensive_value': -2.438}},
#                                                    'castel': {'castel': {'defensive_value': -0.125, 'offensive_value': 0.28}},
#                                                    'circle': {'circle': {'defensive_value': -0.355, 'offensive_value': -0.46}},
#                                                    'cresent': {'cresent': {'defensive_value': 1.075, 'offensive_value': -0.97}},
#                                                    'cross': {'cross': {'defensive_value': -0.522, 'offensive_value': -0.2}},
#                                                    'crown': {'crown': {'defensive_value': 0.044, 'offensive_value': 0.531}},
#                                                    'dragon': {'dragon': {'defensive_value': -0.012, 'offensive_value': -1.68}},
#                                                    'emblem': {'emblem': {'defensive_value': 0.78, 'offensive_value': -1.343}},
#                                                    'flag': {'flag': {'defensive_value': 0.689, 'offensive_value': 0.888}},
#                                                    'green': {'green': {'defensive_value': -0.543, 'offensive_value': -0.143}},
#                                                    'horizontal': {'horizontal': {'defensive_value': -0.57,
#                                                                                  'offensive_value': -0.679}},
#                                                    'latin': {'latin': {'defensive_value': -1.495, 'offensive_value': -0.197}},
#                                                    'lightblue': {'lightblue': {'defensive_value': -0.108,
#                                                                                'offensive_value': 2.021}},
#                                                    'lightgreen': {'lightgreen': {'defensive_value': -1.68,
#                                                                                  'offensive_value': 0.899}},
#                                                    'maple': {'maple': {'defensive_value': -1.16, 'offensive_value': -0.157}},
#                                                    'maroon': {'maroon': {'defensive_value': -4.649, 'offensive_value': -0.622}},
#                                                    'red': {'red': {'defensive_value': -0.539, 'offensive_value': -0.249}},
#                                                    'star': {'star': {'defensive_value': 0.017, 'offensive_value': -0.029}},
#                                                    'sun': {'sun': {'defensive_value': 0.418, 'offensive_value': -1.193}},
#                                                    'sword': {'sword': {'defensive_value': -2.158, 'offensive_value': 0.082}},
#                                                    'vertical': {'vertical': {'defensive_value': -0.402,
#                                                                              'offensive_value': 0.013}},
#                                                    'white': {'white': {'defensive_value': -0.32, 'offensive_value': 0.328}},
#                                                    'yellow': {'yellow': {'defensive_value': -0.03, 'offensive_value': 0.09}}}.items()}

# Round of 16
FEATURES = {k: Feature.from_json(v) for (k, v) in {'angles': {'angles': {'defensive_value': 0.296, 'offensive_value': 0.076}},
                                                   'arabic': {'arabic': {'defensive_value': -0.731, 'offensive_value': -0.867}},
                                                   'bird': {'bird': {'defensive_value': -0.444, 'offensive_value': 0.077}},
                                                   'black': {'black': {'defensive_value': -0.503, 'offensive_value': -0.148}},
                                                   'blue': {'blue': {'defensive_value': 0.103, 'offensive_value': 0.162}},
                                                   'brown': {'brown': {'defensive_value': -0.401, 'offensive_value': -0.69}},
                                                   'castel': {'castel': {'defensive_value': -0.091, 'offensive_value': 0.089}},
                                                   'circle': {'circle': {'defensive_value': -0.209, 'offensive_value': 0.345}},
                                                   'cresent': {'cresent': {'defensive_value': 1.388, 'offensive_value': -1.551}},
                                                   'cross': {'cross': {'defensive_value': -0.245, 'offensive_value': 0.195}},
                                                   'crown': {'crown': {'defensive_value': -0.266, 'offensive_value': -0.21}},
                                                   'dragon': {'dragon': {'defensive_value': -1.333, 'offensive_value': -2.015}},
                                                   'emblem': {'emblem': {'defensive_value': -0.114, 'offensive_value': -0.025}},
                                                   'flag': {'flag': {'defensive_value': 0.392, 'offensive_value': 0.127}},
                                                   'green': {'green': {'defensive_value': 0.604, 'offensive_value': 0.052}},
                                                   'horizontal': {'horizontal': {'defensive_value': 0.1,
                                                                                 'offensive_value': -0.065}},
                                                   'latin': {'latin': {'defensive_value': 0.629, 'offensive_value': 0.404}},
                                                   'lightblue': {'lightblue': {'defensive_value': 0.361,
                                                                               'offensive_value': 1.928}},
                                                   'lightgreen': {'lightgreen': {'defensive_value': -0.417,
                                                                                 'offensive_value': 0.68}},
                                                   'maple': {'maple': {'defensive_value': -1.096, 'offensive_value': -0.265}},
                                                   'maroon': {'maroon': {'defensive_value': -1.345, 'offensive_value': -0.281}},
                                                   'red': {'red': {'defensive_value': -0.167, 'offensive_value': 0.987}},
                                                   'star': {'star': {'defensive_value': 0.014, 'offensive_value': -0.026}},
                                                   'sun': {'sun': {'defensive_value': 0.091, 'offensive_value': -0.096}},
                                                   'sword': {'sword': {'defensive_value': -1.151, 'offensive_value': 1.487}},
                                                   'vertical': {'vertical': {'defensive_value': 0.085, 'offensive_value': 0.279}},
                                                   'white': {'white': {'defensive_value': 0.04, 'offensive_value': 0.041}},
                                                   'yellow': {'yellow': {'defensive_value': 0.154, 'offensive_value': -0.091}}}.items()}
