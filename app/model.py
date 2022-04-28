from lib2to3.pytree import Base
from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "Some title about animals",
                "content": "Some content about animals"
            }
        }
        
        
class UserSchema(BaseModel):
    fullname: str = Field(default = None)
    email: EmailStr = Field(default = None)
    password: str = Field(default = None)
    
    class Config:
        schema_extra = {
            "user_demo": {
                "name": "Luis F",
                "email": "luisf@email.com",
                "password": "123"
            }
        }
        
        
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default = None)
    password: str = Field(default = None)
    
    class Config:
        schema_extra = {
            "user_demo": {
                "email": "luisf@email.com",
                "password": "123"
            }
        }