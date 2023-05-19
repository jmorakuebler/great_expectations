from typing import Literal, Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class EventBase(BaseModel):
    type: str


class RunDataAssistantEvent(EventBase):
    type: Literal[
        "onboarding_data_assistant_request.received"
    ] = "onboarding_data_assistant_request.received"


class ShutdownEvent(EventBase):
    type: Literal["shutdown"] = "shutdown"


Event = Annotated[
    Union[RunDataAssistantEvent, ShutdownEvent], Field(discriminator="type")
]
