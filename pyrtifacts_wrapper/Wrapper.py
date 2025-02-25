from dacite import from_dict

from pyrtifacts_wrapper.schemas import SkillDataSchema
from pyrtifacts_wrapper.RestAdapter import RestAdapter


class Wrapper:
    def __init__(self, adapter: RestAdapter):
        """
        Wrapper constructor.
        :param adapter: The RestAdapter to use.
        """
        self._adapter = adapter

    def action_gather(self) -> SkillDataSchema:
        """
        Gather on current map.
        :return SkillDataSchema:
        """
        res = self._adapter.post('my/asventi/action/gathering')
        return from_dict(SkillDataSchema, res.data)