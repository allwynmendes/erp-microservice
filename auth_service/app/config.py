import os
from typing import List

class Settings:
    # API configuration
    API_V1_STR: str = "/api/v1"
    
    # CORS configuration - domains that can access our API
    CORS_ORIGINS: List[str] = ["*"]
    
    # Database configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./erp_auth.db")

# Create settings instance
settings = Settings()
