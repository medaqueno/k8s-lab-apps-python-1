"""
Configuration module for the application
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()


class Settings:
    """Application settings"""

    # Application
    APP_NAME: str = os.getenv("APP_NAME", "API-1")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG").upper()

    # Server
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # Future: Add more configuration
    # DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    # REDIS_URL: str = os.getenv("REDIS_URL", "")
    # SECRET_KEY: str = os.getenv("SECRET_KEY", "")

    @classmethod
    def validate(cls):
        """Validate required configuration"""
        required_vars = []  # Add required vars here

        missing = [var for var in required_vars if not getattr(cls, var)]
        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}")


# Singleton instance
settings = Settings()

# Validate on import
settings.validate()
