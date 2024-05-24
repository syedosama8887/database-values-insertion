from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import databasevalues  # Import your router here

# Create a FastAPI instance
app = FastAPI(
    title="First Project",
    version="1.0",
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Allow both GET and POST methods
    allow_headers=["*"],
)

# Include your router
app.include_router(databasevalues)

# Run the app if this script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)

