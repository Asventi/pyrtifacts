from dataclasses import dataclass

@dataclass
class InventorySlot:
    slot: int
    code: str
    quantity: int