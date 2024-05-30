from fastapi import APIRouter, HTTPException
from typing import List
import mysql.connector
from pydantic import BaseModel

# Create a new router
router = APIRouter()

# Define a Pydantic model for the request body
class Staff(BaseModel):
    id: int
    name: str
    age: int
    email: str

# Define your MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Replace with your MySQL password
    'database': 'data_test',
}

# Function to fetch data from database
def fetch_data_from_db():
    try:
        # Connect to MySQL database
        mydb = mysql.connector.connect(**db_config)

        # Create cursor
        mycursor = mydb.cursor()

        # Query to fetch data
        sql = "SELECT id, name, age, email FROM staff"
        mycursor.execute(sql)

        # Fetch all rows
        result = mycursor.fetchall()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        return result

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

# Endpoint to fetch all data from database
@router.get("/fetch_data")
async def fetch_data():
    return {"data": fetch_data_from_db()}

# Endpoint to fetch data for a specific ID
@router.get("/fetch_data/{id}")
async def fetch_data_by_id(id: int):
    try:
        # Connect to MySQL database
        mydb = mysql.connector.connect(**db_config)

        # Create cursor
        mycursor = mydb.cursor()

        # Query to fetch data for specific ID
        sql = "SELECT id, name, age, email FROM staff WHERE id = %s"
        mycursor.execute(sql, (id,))

        # Fetch the row
        result = mycursor.fetchone()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        if not result:
            raise HTTPException(status_code=404, detail="Data not found")

        return {"data": result}

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

# Function to update records in database
def update_record_in_db(staff: Staff):
    try:
        # Connect to MySQL database
        mydb = mysql.connector.connect(**db_config)

        # Create cursor
        mycursor = mydb.cursor()

        # Update query
        sql = "UPDATE staff SET name = %s, age = %s, email = %s WHERE id = %s"
        val = (staff.name, staff.age, staff.email, staff.id)
        mycursor.execute(sql, val)

        # Commit changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        return {"message": "Record updated successfully"}

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))
# Function to insert a new record into database
def insert_record_in_db(staff: Staff):
    try:
        # Connect to MySQL database
        mydb = mysql.connector.connect(**db_config)

        # Create cursor
        mycursor = mydb.cursor()

        # Insert query
        sql = "INSERT INTO staff (name, age, email) VALUES (%s, %s, %s)"
        val = (staff.name, staff.age, staff.email)
        mycursor.execute(sql, val)

        # Commit changes
        mydb.commit()

        # Close cursor and connection
        mycursor.close()
        mydb.close()

        return {"message": "Record inserted successfully"}

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

# Endpoint to insert a new record into database
@router.post("/insert_staff")
async def insert_staff(staff: Staff):
    return insert_record_in_db(staff)

# Endpoint to update records in database
@router.put("/update_staff/{id}")
async def update_staff(id: int, staff: Staff):
    staff.id = id  # Ensure the ID from path parameter is used
    return update_record_in_db(staff)



# from fastapi import FastAPI, APIRouter, HTTPException
# from typing import List
# import mysql.connector
# from pydantic import BaseModel

# # Create a FastAPI app instance
# app = FastAPI()

# # Create a new router
# router = APIRouter()

# # Define your MySQL database configuration
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '',  # Replace with your MySQL password
#     'database': 'data_test',
# }

# # Define a Pydantic model for the request body
# class Staff(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str

# # Function to fetch data from database
# def fetch_data_from_db():
#     try:
#         # Connect to MySQL database
#         mydb = mysql.connector.connect(**db_config)

#         # Create cursor
#         mycursor = mydb.cursor()

#         # Query to fetch data
#         sql = "SELECT id, name, age, email FROM staff"
#         mycursor.execute(sql)

#         # Fetch all rows
#         result = mycursor.fetchall()

#         # Close cursor and connection
#         mycursor.close()
#         mydb.close()

#         return result

#     except mysql.connector.Error as err:
#         raise HTTPException(status_code=500, detail=str(err))

# # Function to insert records into database
# def insert_records_into_db(staff: Staff):
#     try:
#         # Connect to MySQL database
#         mydb = mysql.connector.connect(**db_config)

#         # Create cursor
#         mycursor = mydb.cursor()

#         # Insert query
#         sql = "INSERT INTO staff (id, name, age, email) VALUES (%s, %s, %s, %s)"
#         val = (staff.id, staff.name, staff.age, staff.email)
#         mycursor.execute(sql, val)

#         # Commit changes
#         mydb.commit()

#         # Close cursor and connection
#         mycursor.close()
#         mydb.close()

#         return {"message": "Record inserted successfully"}

#     except mysql.connector.Error as err:
#         raise HTTPException(status_code=500, detail=str(err))

# # Function to update records in database
# def update_record_in_db(staff: Staff):
#     try:
#         # Connect to MySQL database
#         mydb = mysql.connector.connect(**db_config)

#         # Create cursor
#         mycursor = mydb.cursor()

#         # Update query
#         sql = "UPDATE staff SET name = %s, age = %s, email = %s WHERE id = %s"
#         val = (staff.name, staff.age, staff.email, staff.id)
#         mycursor.execute(sql, val)

#         # Commit changes
#         mydb.commit()

#         # Close cursor and connection
#         mycursor.close()
#         mydb.close()

#         return {"message": "Record updated successfully"}

#     except mysql.connector.Error as err:
#         raise HTTPException(status_code=500, detail=str(err))

# # Endpoint to fetch data from database
# @router.get("/fetch_data")
# async def fetch_data():
#     return {"data": fetch_data_from_db()}

# # Endpoint to insert records into database
# @router.post("/insert_staff")
# async def insert_staff(staff: Staff):
#     return insert_records_into_db(staff)

# # Endpoint to update records in database
# @router.put("/update_staff")
# async def update_staff(staff: Staff):
#     return update_record_in_db(staff)

# # Include the router in your main FastAPI app
# app.include_router(router)












# from fastapi import APIRouter, HTTPException
# from typing import List
# import mysql.connector
# from pydantic import BaseModel

# # Create a new router
# router = APIRouter()

# # Define a Pydantic model for the request body
# class Staff(BaseModel):
#     id: int
#     name: str
#     age: int
#     email: str

# # Define your MySQL database configuration
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '',  # Replace with your MySQL password
#     'database': 'data_test',
# }

# # Function to fetch data from database
# def fetch_data_from_db():
#     try:
#         # Connect to MySQL database
#         mydb = mysql.connector.connect(**db_config)

#         # Create cursor
#         mycursor = mydb.cursor()

#         # Query to fetch data
#         sql = "SELECT id, name, age, email FROM staff"
#         mycursor.execute(sql)

#         # Fetch all rows
#         result = mycursor.fetchall()

#         # Close cursor and connection
#         mycursor.close()
#         mydb.close()

#         return result

#     except mysql.connector.Error as err:
#         raise HTTPException(status_code=500, detail=str(err))

# # Endpoint to fetch data from database
# @router.get("/fetch_data")
# async def fetch_data():
#     return {"data": fetch_data_from_db()}

# # Function to insert records into database
# def insert_records_into_db(staff: Staff):
#     try:
#         # Connect to MySQL database
#         mydb = mysql.connector.connect(**db_config)

#         # Create cursor
#         mycursor = mydb.cursor()

#         # Insert query
#         sql = "INSERT INTO staff (id, name, age, email) VALUES (%s, %s, %s, %s)"
#         val = (staff.id, staff.name, staff.age, staff.email)
#         mycursor.execute(sql, val)

#         # Commit changes
#         mydb.commit()

#         # Close cursor and connection
#         mycursor.close()
#         mydb.close()

#         return {"message": "Record inserted successfully"}

#     except mysql.connector.Error as err:
#         raise HTTPException(status_code=500, detail=str(err))

# # Endpoint to insert records into database
# @router.post("/insert_staff")
# async def insert_staff(staff: Staff):
#     return insert_records_into_db(staff)



# # from fastapi import APIRouter, HTTPException
# # from pydantic import BaseModel
# # from typing import List
# # import mysql.connector

# # # Create a new router
# # router = APIRouter()

# # # Define a Pydantic model for the request body
# # class Staff(BaseModel):
# #     id: int
# #     name: str
# #     age: int
# #     email: str

# # def insert_records(staff: Staff):
# #     try:
# #         mydb = mysql.connector.connect(
# #             host="127.0.0.1",
# #             user="root",
# #             password="",
# #             database="data_test"
# #         )

# #         mycursor = mydb.cursor()

# #         sql = "INSERT INTO staff (id, name, age, email) VALUES (%s, %s, %s, %s)"
# #         val = (staff.id, staff.name, staff.age, staff.email)
# #         mycursor.execute(sql, val)

# #         mydb.commit()
# #         return {"message": "Record inserted successfully"}

# #     except mysql.connector.Error as err:
# #         raise HTTPException(status_code=500, detail=str(err))

# #     finally:
# #         mycursor.close()
# #         mydb.close()

# # @router.post("/insert_staff")
# # async def insert_staff(staff: Staff):
# #     return insert_records(staff)



