from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Fix imports to be relative to the current package
from auth_service.app.api import auth
from auth_service.app.config import settings
from auth_service.app.db.database import engine
from auth_service.app.models.user import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ERP Authentication Service",
    description="Authentication microservice for ERP system",
    version="0.1.0",
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])

@app.get("/health", tags=["health"])
def health_check():
    """
    Health check endpoint to verify the service is running
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("auth_service.app.main:app", host="0.0.0.0", port=8000, reload=True)
