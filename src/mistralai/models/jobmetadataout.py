"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class JobMetadataOutTypedDict(TypedDict):
    expected_duration_seconds: NotRequired[Nullable[int]]
    cost: NotRequired[Nullable[float]]
    cost_currency: NotRequired[Nullable[str]]
    train_tokens_per_step: NotRequired[Nullable[int]]
    train_tokens: NotRequired[Nullable[int]]
    data_tokens: NotRequired[Nullable[int]]
    estimated_start_time: NotRequired[Nullable[int]]
    

class JobMetadataOut(BaseModel):
    expected_duration_seconds: OptionalNullable[int] = UNSET
    cost: OptionalNullable[float] = UNSET
    cost_currency: OptionalNullable[str] = UNSET
    train_tokens_per_step: OptionalNullable[int] = UNSET
    train_tokens: OptionalNullable[int] = UNSET
    data_tokens: OptionalNullable[int] = UNSET
    estimated_start_time: OptionalNullable[int] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expected_duration_seconds", "cost", "cost_currency", "train_tokens_per_step", "train_tokens", "data_tokens", "estimated_start_time"]
        nullable_fields = ["expected_duration_seconds", "cost", "cost_currency", "train_tokens_per_step", "train_tokens", "data_tokens", "estimated_start_time"]
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
        
