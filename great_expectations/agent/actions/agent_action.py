from abc import abstractmethod
from typing import Generic, Sequence, TypeVar, Optional

from pydantic import BaseModel

from great_expectations.agent.models import CreatedResource, Event
from great_expectations.data_context import CloudDataContext


class ActionDetails(BaseModel):
    value: Sequence[str]


class ActionResult(BaseModel):
    id: str
    type: str
    created_resources: Sequence[CreatedResource]
    details: Optional[ActionDetails] = None


_EventT = TypeVar("_EventT", bound=Event)


class AgentAction(Generic[_EventT]):
    def __init__(self, context: CloudDataContext):
        self._context = context

    @abstractmethod
    def run(self, event: _EventT, id: str) -> ActionResult:
        ...
