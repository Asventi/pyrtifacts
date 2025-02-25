from dataclasses import dataclass
from datetime import datetime
from pyrtifacts_wrapper.enums import CooldownReason
from typing import Union


@dataclass
class CooldownSchema:
    total_seconds: int
    remaining_seconds: int
    started_at: str
    expiration: str
    reason: str