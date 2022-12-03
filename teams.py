from datatypes import Team, TeamName
from features import FEATURES


def new(name, features):
    return Team(
        name=name,
        features=[FEATURES[feature] for feature in features]
    )


TEAMS: dict[TeamName, Team] = {name: new(name, features) for (name, features) in [
    ('Netherlands', ['red', 'white', 'blue', 'horizontal']),
    ('Senegal', ['lightgreen', 'red', 'yellow', 'star']),
    ('Qatar', ['white', 'maroon', 'vertical', 'angles']),
    ('Ecuador', ['blue', 'yellow', 'red', 'emblem',
     'bird', 'horizontal', 'flag', 'sun']),
    ('England', ['red', 'white', 'cross']),
    ('Iran', ['red', 'white', 'lightgreen', 'arabic', 'horizontal']),
    ('USA', ['red', 'white', 'blue', 'horizontal'] + ['star'] * 50),
    ('Wales', ['red', 'white', 'lightgreen', 'dragon', 'horizontal']),
    ('Argentina', ['lightblue', 'white', 'yellow', 'sun', 'horizontal']),
    ('SaudiArabia', ['green', 'white', 'arabic', 'sword']),
    ('Mexico', ['red', 'white', 'green', 'bird', 'vertical', 'brown']),
    ('Poland', ['red', 'white', 'horizontal']),
    ('Denmark', ['red', 'white', 'cross']),
    ('Tunisia', ['red', 'white', 'star', 'circle', 'cresent']),
    ('France', ['red', 'white', 'blue', 'vertical']),
    ('Australia', ['red', 'white', 'blue', 'flag'] +
     ['star'] * 6 + ['cross'] * 3),
    ('Germany', ['black', 'red', 'yellow', 'horizontal']),
    ('Japan', ['white', 'red', 'circle']),
    ('Spain', ['yellow', 'red', 'emblem', 'horizontal',
     'latin', 'white', 'castel'] + ['crown'] * 3),
    ('CostaRica', ['red', 'white', 'blue', 'horizontal']),
    ('Morocco', ['red', 'green', 'star']),
    ('Croatia', ['red', 'white', 'blue', 'emblem', 'horizontal', 'crown']),
    ('Belgium', ['red', 'yellow', 'black', 'vertical']),
    ('Canada', ['red', 'white', 'maple', 'vertical']),
    ('Switzerland', ['red', 'white', 'cross']),
    ('Cameroon', ['green', 'red', 'yellow', 'star', 'vertical']),
    ('Brazil', ['lightgreen', 'blue', 'yellow', 'circle',
     'angles', 'white', 'latin'] + ['star'] * 27),
    ('Serbia', ['blue', 'white', 'red', 'emblem',
     'horizontal', 'bird', 'crown', 'cross']),
    ('Portugal', ['green', 'red', 'emblem',
     'vertical', 'circle', 'white'] + ['castel'] * 7),
    ('Ghana', ['lightgreen', 'red', 'yellow', 'star', 'black', 'horizontal']),
    ('Uruguay', ['white', 'blue', 'yellow', 'sun', 'horizontal']),
    ('Korea', ['black', 'blue', 'red', 'white', 'circle'])
]}
