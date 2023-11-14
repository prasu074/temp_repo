from typing import Any, Optional

from pydantic import BaseModel


class DefaultResponse(BaseModel):
    status: str = "success"
    message: str
    data: Optional[Any]
