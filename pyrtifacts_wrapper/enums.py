from enum import Enum

class CooldownReason(Enum):
    MOVEMENT = 'movement'
    FIGHT = 'fight'
    CRAFTING = 'crafting'
    GATHERING = 'gathering'
    BUY_GE = 'buy_ge'
    SELL_GE = 'sell_ge'
    DELETE_ITEM = 'delete_item'
    DEPOSIT_BANK = 'deposit_bank'
    WITHDRAW_BANK = 'withdraw_bank'
    EQUIP = 'equip'
    UNEQUIP = 'unequip'
    TASK = 'task'
    RECYCLING = 'recycling'