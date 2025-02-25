from pyrtifacts_wrapper import RestAdapter
from pyrtifacts_wrapper.schemas import SkillDataSchema
import logging
import sys

if __name__ == '__main__':
    logger = logging.getLogger("RestAdapter")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s'))
    logger.addHandler(handler)
    adapter = RestAdapter('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imphcm5hY3BpZXJyZW9mZkBnbWFpbC5jb20iLCJwYXNzd29yZF9jaGFuZ2VkIjoiIn0.u6mXAnIAHMxnfrcTX_37f6Wkg7VFSEBa82z84wS96J0', logger=logger)
    res = adapter.post('my/asventi/action/gathering')
    skill = SkillDataSchema(**res.data)
    print(skill.cooldown.remaining_seconds)
    #res = adapter.post('my/asventi/action/move', data={"x": 2, "y": 0})
