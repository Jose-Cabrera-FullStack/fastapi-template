from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel


class POSTResponse(BaseModel):
    status: str
    data: Optional[List[Dict[str, Any]]]
