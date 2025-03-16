import sys
import os
import uvicorn

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    uvicorn.run("auth_service.app.main:app", host="0.0.0.0", port=8002, reload=True)
