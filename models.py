# # models.py
# from sqlalchemy import create_engine, Column, Integer, Text, String, DateTime, func
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class User(Base):
#     """User account."""

#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True, autoincrement="auto")
#     username = Column(String(255), unique=True, nullable=False)
#     password = Column(Text, nullable=False)
#     email = Column(String(255), unique=True, nullable=False)
#     first_name = Column(String(255))
#     last_name = Column(String(255))
#     bio = Column(Text)
#     avatar_url = Column(Text)
#     created_at = Column(DateTime, server_default=func.now())
#     updated_at = Column(DateTime, server_default=func.now())

#     def __repr__(self):
#         return f"<User {self.username}>"


from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Text, Integer, String, DateTime, func
from sqlalchemy import create_engine
import sqlalchemy

Base = sqlalchemy.orm.declarative_base()

class User(Base):
    """User account."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    bio = Column(Text)
    avatar_url = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())


if __name__ == "__main__":
	u = User()

	sesh = sessionmaker(bind=create_engine('sqlite:///pets.db'))

	with sesh() as s:
		s.add(u)
		s.commit()
