from pprint import pprint
from datatypes import Score
import math
from typing import Callable

from features import FEATURES
from results import RESULTS
from teams import TEAMS


def _compare_scores(calculated: Score, measured: Score) -> float:
    a = calculated[0] - measured[0]
    b = calculated[1] - measured[1]
    return math.sqrt(a**2 + b**2)/2


def _winner(score: Score) -> int:
    if score[0] > score[1]:
        return 1
    elif score[1] > score[0]:
        return -1
    else:
        return 0


def calculate(should_print=False) -> float:
    fit = 0
    guess = 0

    if should_print:
        print('Measured vs Calculated results:')

    for (a, b), measured in RESULTS.items():
        calculated = TEAMS[a].play(TEAMS[b])
        if should_print:
            calculated = tuple(map(round, calculated))
            guessed_correctly = _winner(calculated) == _winner(measured)
            if guessed_correctly:
                guess += 1
            print(
                f'{a:16} {b:16}\t{measured}\t{calculated}\t{guessed_correctly}')
        fit += _compare_scores(calculated, measured)

    if should_print:
        print('Guess %', round(100 * guess / len(RESULTS)))
        print('Fit accuracy', round(fit / len(RESULTS), 2), 'goals / team / match')

    return fit


STEP = 0.001


def _get_step_function(idx: int):
    def step_feature(dir: int):
        key = list(FEATURES.keys())[(idx // 2) % len(FEATURES)]
        feature = FEATURES[key]
        if bool(idx % 2):
            feature.defensive_value += dir * STEP
        else:
            feature.offensive_value += dir * STEP

    return step_feature


TOL = 1e-5


def _tol(a, b):
    if abs(a-b) > TOL:
        return a-b
    else:
        return 0


def _get_direction(step_function, fit_function) -> int:
    fit = fit_function()
    step_function(1)
    plus_fit = fit_function()
    step_function(-2)
    minus_fit = fit_function()
    step_function(1)

    over, under = _tol(plus_fit, fit), _tol(minus_fit, fit)

    if ((over > 0) and (under > 0)) or (over == under == 0):
        return 0

    if (over > under):
        return -1
    else:
        return 1


def _optimize_feature(step_function, fit_function):
    dir = _get_direction(step_function, fit_function)
    if dir == 0:
        raise ValueError()  # Feature is at minima

    # Step in direction while fit is getting smaller
    prev_fit = fit_function()
    step_function(dir)
    fit = fit_function()
    diff = _tol(prev_fit, fit)
    while (diff > 0):
        prev_fit = fit
        step_function(dir)
        fit = fit_function()
        diff = _tol(prev_fit, fit)

    if diff < 0:
        # take back last step
        step_function(-dir)


def optimize(fit_method: Callable[[], float]):
    features_at_minima = 0

    for feature_index in range(100_000):
        if features_at_minima > len(FEATURES) * 2:
            break  # All features at minima

        try:
            _optimize_feature(_get_step_function(feature_index), fit_method)
        except ValueError:
            features_at_minima += 1
        else:
            features_at_minima = 0  # We optimized a feature, so all features may have shifted

        if (feature_index % 1000 == 0):
            print(f"optimized {feature_index} features. fit: {calculate()}")


if __name__ == '__main__':

    optimize(calculate)

    pprint({k: v.to_json() for (k, v) in FEATURES.items()})

    calculate(should_print=True)

    games = [
        # 16
        ('Netherlands', 'USA'),
        ('Argentina', 'Australia'),
        ('Japan', 'Croatia'),
        ('Brazil', 'Korea'),
        ('France', 'Poland'),
        ('England', 'Senegal'),
        ('Morocco', 'Spain'),
        ('Portugal', 'Switzerland'),
        # QF
        ('Netherlands', 'Argentina'),
        ('Croatia', 'Brazil'),
        ('France', 'England'),
        ('Morocco', 'Switzerland'),
        # SF
        ('Argentina', 'Brazil'),
        ('France', 'Morocco'),
        # F
        ('Argentina', 'France'),
    ]

    print("Guessing next rounds:")
    for a, b in games:
        score = TEAMS[a].play(TEAMS[b])
        print(
            f'{a:16} {b:16}\t{tuple(map(round, score))}\t{_winner(score) == 1 and a or b}')
