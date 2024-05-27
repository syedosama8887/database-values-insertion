from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import databasevalues# Import your router

# Create a FastAPI instance
app = FastAPI(
    title="First Project",
    version="1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Include your router(s)
app.include_router(databasevalues)

# Run the app if this script is executed directly
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
    