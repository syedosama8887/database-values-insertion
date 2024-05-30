from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

# Create FastAPI instance
router= FastAPI()

# Define a Pydantic model for the request body
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

# Define your MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Replace with your MySQL password
    'database': 'data_test',
}

def insert_record_in_db(user: UserCreate):
    try:
        # Connect to MySQL database
        mydb = mysql.connector.connect(**db_config)

        # Create cursor
        mycursor = mydb.cursor()

        # Insert query into `uses` table
        sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        val = (user.name, user.email, user.password)
        mycursor.execute(sql, val)

        # Commit changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        return {"message": "Record inserted successfully"}

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

# Endpoint to insert a new user record into the `uses` table
@router.post("/insert_user")
async def insert_user(user: UserCreate):
    return insert_record_in_db(user)


# from fastapi import APIRouter, HTTPException, Depends
# from typing import List
# import mysql.connector
# from pydantic import BaseModel
# from passlib.context import CryptContext

# # Create a new router
# router = APIRouter()

# # Password context for hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Define a Pydantic model for the request body
# class UserCreate(BaseModel):
#     name: str
#     email: str
#     password: str

# class UserLogin(BaseModel):
#     email: str
#     password: str

# # Define your MySQL database configuration
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '',  # Replace with your MySQL password
#     'database': 'data_test',
# }

# def insert_record_in_db(user: UserCreate):
#     try:
#         # Connect to MySQL database
#         mydb = mysql.connector.connect(**db_config)

#         # Create cursor
#         mycursor = mydb.cursor()

#         # Hash the password
#         hashed_password = pwd_context.hash(user.password)

#         # Insert query
#         sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
#         val = (user.name, user.email, hashed_password)
#         mycursor.execute(sql, val)

#         # Commit changes
#         mydb.commit()

#         # Close cursor and connection
#         mycursor.close()
#         mydb.close()

#         return {"message": "Record inserted successfully"}

#     except mysql.connector.Error as err:
#         raise HTTPException(status_code=500, detail=str(err))

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def authenticate_user(email: str, password: str):
#     try:
#         # Connect to MySQL database
#         mydb = mysql.connector.connect(**db_config)

#         # Create cursor
#         mycursor = mydb.cursor(dictionary=True)

#         # Select query
#         sql = "SELECT * FROM users WHERE email = %s"
#         mycursor.execute(sql, (email,))
#         user = mycursor.fetchone()

#         # Close cursor and connection
#         mycursor.close()
#         mydb.close()

#         if user and verify_password(password, user['password']):
#             return user
#         else:
#             return None

#     except mysql.connector.Error as err:
#         raise HTTPException(status_code=500, detail=str(err))

# # Endpoint to insert a new record into the database
# @router.post("/insert_user")
# async def insert_user(user: UserCreate):
#     return insert_record_in_db(user)

# # Endpoint for user login
# @router.post("/login")
# async def login(user: UserLogin):
#     authenticated_user = authenticate_user(user.email, user.password)
#     if authenticated_user:
#         return {"message": "Login successful", "user": authenticated_user}
#     else:
#         raise HTTPException(status_code=400, detail="Invalid email or password")

# @router.get("/signup")
# async def signup():
#     return {"message": "Sign up endpoint"}
