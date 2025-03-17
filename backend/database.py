from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///mangaai.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    from models.scenario import Scenario
    from models.character import Character
    from models.layout import Layout
    Base.metadata.create_all(bind=engine)
    print("📌 Base de données initialisée avec succès !")

if __name__ == "__main__":
    init_db()
