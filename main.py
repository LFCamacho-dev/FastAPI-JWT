import uvicorn
from fastapi import Body, FastAPI, Depends
from app.model import PostSchema, UserLoginSchema, UserSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

posts = [
    {
        "id": 1,
        "title": "penguins",
        "content": "Penguins are a group of aquatic flightless birds."
    },
    {
        "id": 2,
        "title": "tigers",
        "content": "Tigers are the largest living cat species and members of the genus panthera."
    },
    {
        "id": 3,
        "title": "koalas",
        "content": "Koalas are arboreal herbivorous marsupials native to Australia."
    }
]

users = []

app = FastAPI()



def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# GET for testing
@app.get('/', tags=["test"])
def greet():
    return {"hello": "World"}


# GET Posts
@app.get('/posts', tags=["Posts"])
def get_posts():
    return {"data": posts}
    

# GET Posts by ID
@app.get('/posts/{id}', tags=["Posts"])
def get_one_post(id : int):
    if id > len(posts):
        return{
            "Error": "Post with this ID does not exist."
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


#POST for creating new entry
@app.post('/posts', dependencies=[Depends(jwtBearer())], tags=["Posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "Info": "Post added successfuly"
    }


# POST Create new user
@app.post('/user/signup', tags=["User"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


  
# POST User Login
@app.post('/user/login', tags=["User"])
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login credentials."
        }      
        

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    
    