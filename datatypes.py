
from dataclasses import dataclass


Score = tuple[float, float]
TeamName = str
Match = tuple[TeamName, TeamName]


@dataclass
class Feature:
    name: str
    offensive_value: float
    defensive_value: float

    def __add__(self, other: 'Feature'):
        return Feature(name=self.name + "+" + other.name,
                       offensive_value=self.offensive_value + other.offensive_value,
                       defensive_value=self.defensive_value + other.defensive_value)

    def play(self, other: 'Feature') -> Score:
        return (self.offensive_value - other.defensive_value,
                other.offensive_value - self.defensive_value)

    def to_json(self) -> dict:
        return {self.name: {"offensive_value": round(self.offensive_value, 3), "defensive_value": round(self.defensive_value, 3)}}

    @staticmethod
    def from_json(json: dict) -> 'Feature':
        name = list(json.keys())[0]
        return Feature(name=name, **json[name])


@dataclass
class Team:
    name: TeamName
    features: list[Feature]

    @property
    def feature(self) -> Feature:
        return sum(self.features[1:], self.features[0])

    def play(self, other: 'Team') -> Score:
        return self.feature.play(other.feature)

    def to_json(self) -> dict:
        return {'name': self.name, 'feature_names': [f.name for f in self.features]}

    @staticmethod
    def from_json(team: dict, features: dict[str, Feature]) -> 'Team':
        return Team(name=team['name'], features=[features[n] for n in team['feature_names']])
