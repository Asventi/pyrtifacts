from dataclasses import dataclass
from typing import List
from pyrtifacts_wrapper.schemas import DropSchema

@dataclass
class SkillInfoSchema:
    xp: int
    items: List[DropSchema]