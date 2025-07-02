from pydantic import BaseModel
import warnings
from typing import Literal


class FileFormat(BaseModel):
    format: Literal["pdf", "doc", "docx"] = "doc"