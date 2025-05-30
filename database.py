from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Створення SQLite бази
engine = create_engine('sqlite:///university.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()  # ← це має бути

Base = declarative_base()


