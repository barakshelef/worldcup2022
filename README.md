# World Cup 2022 Predictions
This script caculates the offensive and defensive raitings of teams in the 2022 FIFA world cup.

It does so by assuming their ability and football has something to do with their flag.

This is obivously not true... or is it?

## Method
### Flag features
I broke down each flag to its constituent parts: colors, shapes, images, directions, and whatever I saw fit.
You can see the list of features in [`features.py`](./features.py) and how they are assigned to the teams in [`teams.py`](./teams.py).

The reasoning behind the choice of features is arbitrary, and is drawn from my years of experience is making things up.

Each feature has two ratings:
 * __offensive raiting__ - how much does having this feature help your team score goals
 * __defensive raiting__ - how much does this feature help your team keep goal out of their net

I'm assuming linearity in features. Because, why not. So once you add up all the features of a single team you can compare it to the rival in the match and calculate this games score.

Team A vs. Team B will have a score of `a.offensive_value - b.defensive_value` to `b.offensive_value - a.defensive_value`.

The keen eyed reader will notice that this allows having a negative score. I decided I don't mind that. I've seen some games where I think a team deserved to have a negative score. I see this is an analytic continuation of the sport.

### Metric
I'm using a geometric average to measure the quality of the fit. Difference is score of each side, squared, summed, square rooted, and halved.

### Optimization
Having done some function optimization work in the past during my B.A. in Physics, and vaguly remember the concepts used in this numeric approach.

My bad memory, and fact that I only just managed to scrape a passing grade in my statistics course did the rest of the "work".

I go over each feature twice, each time trying to find a small increment for the offensive and defensive raitings which reduce the metric closer to 0.

## Results and predictions
The optimized features are seen in [`features.py`](./features.py). Here are some noteworthy results:
 * Having angles in your flag really helps with defensive raiting of +3.116. Sadly for Qatar, having the color maroon in your flag is the worst for defense at -4.649.
 * They key for having a good offensive raiting is clearly the light blue color (+2.021), and birds (+1.879). Birds however, aren't really useful for your defense (-2.172).
 * If you think your team isn't giving it all on offense, it's probably the color brown (-2.438).
 * And apparently having stars doesn't really do anything. +0.017 on defense and -0.029 on offense.

I've used these parameters to calculate predictions for the playoffs:
### Round of 16
* Netherlands will beat the USA. Expecting 0-0 and Netherlands winning -- I guess by penelty shootout?
    * _Actual: 3-1. **Calculated winner correctly**, wrong score._
* Argentina will beat Australia 2-1.
    * _Actual: 2-1. **Calculated winner and score correctly.**_
* Croatia will beat Japan in penelty shootout. Expecting 0-0.
    * _Actual: 1-1. **Calculated winner and goal difference correctly**. Wrong score._
* Brazil will beat Korea in penelty shootout. Expecting 0-0.
    * _Actual: 4-1. **Calculated winner correctly**, wrong score._
* France will beat Poland 2-0.
    * _Actual: 3-1. **Calculated winner and goal difference correctly**, wrong score.
    **until the 91st minute it was still 2-0!**_
* England will beat Senegal in penelty shootout. Expecting 2-2.
    * _Actual: 3-0. **Calculated winner correctly**, wrong score._
* Morocco will beat Spain 2-1.
    * _Actual: 0-0. **Calculated winner correctly**, wrong score._
* Switzerland will beat Portugal 2-1.
    * _Actual: 1-6. Completely incorrect calculation._

#### Round of 16 overview
7/8 outcomes predicted correctly. 3 instances down to the goal difference. once with exact score.

I've recalculated the features and results for the upcoming quarter finals.This changed some results from the original calculation:
* Portugal-Morocco with the previous features was calculated as 2-2 with Portugal winning the penelty shootout. It is now predicted to be 2-1 for Portugal. So it seems they saved themselves a penelty shootout! Good job!
* Brazil will beat Croatia 1-0 instead of 0-minus 1 (_mathematically speaking_). So no real change here.

In the semis we see 1 change:
* France-Portugal with the previous features was calculated as 3-1. It is now predicted to be 2-2 with Portugal taking the penelty shootout. So we get a Messi-Ronaldo final!

In the final we see a slight change:
* Argentina-Portugal with the previous features was calculated as 3-1. It is now predicted to be 2-2 with Argentina winning the penelty shootout.


### Quarter Final
* Argentina will beat the Netherlands 2-0.
* Brazil will beat Croatia 1-0
* France will beat England 2-1
* Portugal will beat Morocco 2-1

### Semi Final
* Argentina will beat Brazil 1-0.
* Portugal will beat France in penelty shootout. Expecting 2-2.

### Finals
* Argentina will beat Portugal in penelty shootout. Expecting 2-2.

**I will update this section with results and recalculate predictions using the same feature parameters if any prediction is wrong**

## Summary
Football is a really random game. But at least we can make some sense of it all by looking at flags. Or maybe we can't. I don't really care.
