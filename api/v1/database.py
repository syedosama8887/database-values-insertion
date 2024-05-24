from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import mysql.connector

# Create a new router
router = APIRouter()

# Define a Pydantic model for the request body
class Staff(BaseModel):
    id: int
    name: str
    age: int
    email: str

def insert_records(staff: Staff):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="data_test"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO staff (id, name, age, email) VALUES (%s, %s, %s, %s)"
        val = (staff.id, staff.name, staff.age, staff.email)
        mycursor.execute(sql, val)

        mydb.commit()
        return {"message": "Record inserted successfully"}

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    finally:
        mycursor.close()
        mydb.close()

@router.post("/insert_staff")
async def insert_staff(staff: Staff):
    return insert_records(staff)



