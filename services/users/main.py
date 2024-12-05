import uvicorn
from fastapi import FastAPI, Depends, status, HTTPException
import schemas
import models
import utils
import database
import oauth2
from sqlalchemy.orm import get_db, Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

# TODO test with local database
# TODO async?

users_app = FastAPI()


@users_app.post(
    "/register/",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(user: schemas.UserRegister, db: Session = Depends(database.get_db)):
    hashed_password = utils.hash_password(user.password)
    new_user = models.User(user.email, hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@users_app.get("/user/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = None
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No User Found"
        )
    return user


"""
@users_app.post("/login")
def login(user_cerd: schemas.UserLogin, db: Session = Depends(database.get_db)) -> str:
    user = db.query(models.User).filter(models.User.email == user_cerd.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )
    if not utils.verify_password(user_cerd.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )
    return "Success"
"""


@users_app.post("/login")
def login(
    user_cerd: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = db.query(models.User).filter(models.User.email == user_cerd.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )
    if not utils.verify_password(user_cerd.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


@users_app.post("/login/refresh")
def login_refresh():
    raise NotImplementedError


if __name__ == "__main__":
    uvicorn.run(users_app, host="0.0.0.0", port=8000)
