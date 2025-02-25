from dataclasses import dataclass
from pyrtifacts_wrapper.schemas import CooldownSchema, SkillInfoSchema, CharacterSchema

@dataclass
class SkillDataSchema:
    cooldown: CooldownSchema
    details: SkillInfoSchema
    character: CharacterSchema