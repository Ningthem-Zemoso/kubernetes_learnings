from fastapi import FastAPI
from .api.v1.endpoints import router as api_router
from .api.v1.celery_endpoints import router as celery_router
from .core.config import settings
from .database.base import Base, engine
import logging

logger = logging.getLogger(__name__)

# Create database tables
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")
except Exception as e:
    logger.error(f"Error creating database tables: {e}")
    raise

app = FastAPI(title="Product API")

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(celery_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Hello, Kubernetes!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
