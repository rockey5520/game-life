from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Individual:
    gender: str
    age: int
    personality: str
    nationality: str
    identity: str
    growth_environment: str
    skin_color: str
    hair_color: str
    eye_color: str

    def to_dict(self):
        return asdict(self)


class Project:
    def __init__(self, name: str):
        self.name = name
        self.individuals: List[Individual] = []

    def add_individual(self, individual: Individual):
        self.individuals.append(individual)

    def get(self, index: int) -> Individual:
        return self.individuals[index]

    def list_all(self) -> List[Individual]:
        return self.individuals

    def size(self) -> int:
        return len(self.individuals)

    def to_dict(self):
        return [ind.to_dict() for ind in self.individuals]

    def load_from_list(self, data: List[dict]):
        self.individuals = [Individual(**d) for d in data]
