from typing import Generic, TypeVar, Optional
from pydantic.generics import GenericModel

T = TypeVar("T")

class ApiResponse(GenericModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None

    @staticmethod
    def success(data: Optional[T] = None, message: str = "Success"):
        return ApiResponse(success=True, message=message, data=data)

    @staticmethod
    def error(message: str = "Error"):
        return ApiResponse(success=False, message=message)
