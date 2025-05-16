from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker  # Removed unused import
from src.models import Base
from src.config import settings


def init_db():
    # Create database engine
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

    # Create all tables
    Base.metadata.create_all(bind=engine)

    # Create session factory
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    print("Database tables created successfully!")


if __name__ == "__main__":
    init_db()
