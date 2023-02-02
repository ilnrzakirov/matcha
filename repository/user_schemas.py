from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """
        Класс юзера возврщ
    """
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    age: int
    gender: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    """
        Класс юзера для создания
    """
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    age: int
    gender: str


class UserUpdate(schemas.BaseUserUpdate):
    """
        Класс юзера для обновления
    """
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    age: int
    gender: str
