"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import io
from mistralai.types import BaseModel
from mistralai.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import Final, IO, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class FileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]
    

class File(BaseModel):
    file_name: Annotated[str, pydantic.Field(alias="file"), FieldMetadata(multipart=True)]
    content: Annotated[Union[bytes, IO[bytes], io.BufferedReader], pydantic.Field(alias=""), FieldMetadata(multipart=MultipartFormMetadata(content=True))]
    content_type: Annotated[Optional[str], pydantic.Field(alias="Content-Type"), FieldMetadata(multipart=True)] = None
    

class FilesAPIRoutesUploadFileMultiPartBodyParamsTypedDict(TypedDict):
    file: FileTypedDict
    r"""The File object (not file name) to be uploaded.
    To upload a file and specify a custom file name you should format your request as such:
    ```bash
    file=@path/to/your/file.jsonl;filename=custom_name.jsonl
    ```
    Otherwise, you can just keep the original file name:
    ```bash
    file=@path/to/your/file.jsonl
    ```
    """
    

class FilesAPIRoutesUploadFileMultiPartBodyParams(BaseModel):
    file: Annotated[File, pydantic.Field(alias=""), FieldMetadata(multipart=MultipartFormMetadata(file=True))]
    r"""The File object (not file name) to be uploaded.
    To upload a file and specify a custom file name you should format your request as such:
    ```bash
    file=@path/to/your/file.jsonl;filename=custom_name.jsonl
    ```
    Otherwise, you can just keep the original file name:
    ```bash
    file=@path/to/your/file.jsonl
    ```
    """
    PURPOSE: Annotated[Final[Optional[str]], pydantic.Field(alias="purpose"), FieldMetadata(multipart=True)] = "fine-tune" # type: ignore
    
