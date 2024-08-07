"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assistantmessage import AssistantMessage, AssistantMessageTypedDict
from .responseformat import ResponseFormat, ResponseFormatTypedDict
from .systemmessage import SystemMessage, SystemMessageTypedDict
from .tool import Tool, ToolTypedDict
from .toolmessage import ToolMessage, ToolMessageTypedDict
from .usermessage import UserMessage, UserMessageTypedDict
from mistralai_azure.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from mistralai_azure.utils import get_discriminator
from pydantic import Discriminator, Tag, model_serializer
from typing import List, Literal, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


ToolChoice = Literal["auto", "none", "any"]

class ChatCompletionStreamRequestTypedDict(TypedDict):
    messages: List[MessagesTypedDict]
    r"""The prompt(s) to generate completions for, encoded as a list of dict with role and content."""
    model: NotRequired[Nullable[str]]
    r"""The ID of the model to use for this request."""
    temperature: NotRequired[float]
    r"""What sampling temperature to use, between 0.0 and 1.0. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or `top_p` but not both."""
    top_p: NotRequired[float]
    r"""Nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or `temperature` but not both."""
    max_tokens: NotRequired[Nullable[int]]
    r"""The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length."""
    min_tokens: NotRequired[Nullable[int]]
    r"""The minimum number of tokens to generate in the completion."""
    stream: NotRequired[bool]
    stop: NotRequired[StopTypedDict]
    r"""Stop generation if this token is detected. Or if one of these tokens is detected when providing an array"""
    random_seed: NotRequired[Nullable[int]]
    r"""The seed to use for random sampling. If set, different calls will generate deterministic results."""
    response_format: NotRequired[ResponseFormatTypedDict]
    tools: NotRequired[Nullable[List[ToolTypedDict]]]
    tool_choice: NotRequired[ToolChoice]
    safe_prompt: NotRequired[bool]
    r"""Whether to inject a safety prompt before all conversations."""
    

class ChatCompletionStreamRequest(BaseModel):
    messages: List[Messages]
    r"""The prompt(s) to generate completions for, encoded as a list of dict with role and content."""
    model: OptionalNullable[str] = "azureai"
    r"""The ID of the model to use for this request."""
    temperature: Optional[float] = 0.7
    r"""What sampling temperature to use, between 0.0 and 1.0. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or `top_p` but not both."""
    top_p: Optional[float] = 1
    r"""Nucleus sampling, where the model considers the results of the tokens with `top_p` probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or `temperature` but not both."""
    max_tokens: OptionalNullable[int] = UNSET
    r"""The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length."""
    min_tokens: OptionalNullable[int] = UNSET
    r"""The minimum number of tokens to generate in the completion."""
    stream: Optional[bool] = True
    stop: Optional[Stop] = None
    r"""Stop generation if this token is detected. Or if one of these tokens is detected when providing an array"""
    random_seed: OptionalNullable[int] = UNSET
    r"""The seed to use for random sampling. If set, different calls will generate deterministic results."""
    response_format: Optional[ResponseFormat] = None
    tools: OptionalNullable[List[Tool]] = UNSET
    tool_choice: Optional[ToolChoice] = "auto"
    safe_prompt: Optional[bool] = False
    r"""Whether to inject a safety prompt before all conversations."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["model", "temperature", "top_p", "max_tokens", "min_tokens", "stream", "stop", "random_seed", "response_format", "tools", "tool_choice", "safe_prompt"]
        nullable_fields = ["model", "max_tokens", "min_tokens", "random_seed", "tools"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

StopTypedDict = Union[str, List[str]]
r"""Stop generation if this token is detected. Or if one of these tokens is detected when providing an array"""


Stop = Union[str, List[str]]
r"""Stop generation if this token is detected. Or if one of these tokens is detected when providing an array"""


MessagesTypedDict = Union[SystemMessageTypedDict, UserMessageTypedDict, AssistantMessageTypedDict, ToolMessageTypedDict]


Messages = Annotated[Union[Annotated[AssistantMessage, Tag("assistant")], Annotated[SystemMessage, Tag("system")], Annotated[ToolMessage, Tag("tool")], Annotated[UserMessage, Tag("user")]], Discriminator(lambda m: get_discriminator(m, "role", "role"))]

