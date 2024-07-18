from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator


class POSTRequest(BaseModel):
    field1: Optional[str]
    field2: int = Field(gt=-1, description="Field 2 must be greater than or equal to 0")

    # Test validator, change to your needs
    @validator("field1", pre=True, always=True)
    def validate_rut(cls, field1):
        msg = ""
        if not field1 or field1 == "":
            msg = "Field1 is required."

        elif len(field1) > 10:
            msg = "Field1 must be less than 10 characters."

        elif len(field1) < 3:
            msg = "Field1 must be greater than 2 characters."

        elif field1 == "INCORRECT":
            msg = "Field1 is INCORRECT, but it should be another string."

        return field1
