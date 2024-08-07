"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from mistralai.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class TrainingParametersTypedDict(TypedDict):
    training_steps: NotRequired[Nullable[int]]
    learning_rate: NotRequired[float]
    epochs: NotRequired[Nullable[float]]
    fim_ratio: NotRequired[Nullable[float]]
    

class TrainingParameters(BaseModel):
    training_steps: OptionalNullable[int] = UNSET
    learning_rate: Optional[float] = 0.0001
    epochs: OptionalNullable[float] = UNSET
    fim_ratio: OptionalNullable[float] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["training_steps", "learning_rate", "epochs", "fim_ratio"]
        nullable_fields = ["training_steps", "epochs", "fim_ratio"]
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
        
