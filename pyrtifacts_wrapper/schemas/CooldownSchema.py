from dataclasses import dataclass
from datetime import datetime
from pyrtifacts_wrapper.enums import CooldownReason

@dataclass
class CooldownSchema:
    total_seconds: int
    remaining_seconds: int
    started_at: datetime
    expiration: datetime
    reason: CooldownReason
