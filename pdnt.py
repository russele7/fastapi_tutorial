from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
    "email": "abc@mail.com",
    "bio": 'MY BIO STORY',
    "age": 12,
    'gender': 'male',
    'birthday': '2022'
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)
    age: int = Field(ge=0, le=130)

    model_config = ConfigDict(extra='forbid')


# user = UserSchema(**data)
# print(repr(user))

users = []


@app.post('/users')
def add_user(user: UserSchema):
    users.append(user)
    return {'ok': True, 'msg': 'User added'}


@app.get('/users')
def list_users() -> list[UserSchema]:
    return users


if __name__ == '__main__':
    uvicorn.run('pdnt:app', reload=True)