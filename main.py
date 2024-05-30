from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.v1 import databasevalues,loginvalues

# Create a FastAPI instance
app = FastAPI(
    title="First Project",
    version="1.0",
)

# Define CORS settings
origins = [
    "http://127.0.0.1:5500",  # Update with your frontend URL
    "http://localhost:5500",  # Add additional origins if needed
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Add other methods as needed
    allow_headers=["*"],
)

# Include your router(s)
app.include_router(databasevalues)
app.include_router(loginvalues.router)
# Run the app if this script is executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
