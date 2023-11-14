from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy.types import Integer, Text, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy import Column

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    """User account."""

    __tablename__ = "user"

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

    def __repr__(self):
        return f"<User {self.username}>"


engine = create_engine('sqlite:///sample.db',echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


user = User(
    username="admin",
    password="Please don't set passwords like this",
    email="admin@example.com",
    first_name="Todd",
    last_name="Birchard",
    bio="I write tutorials on the internet.",
    avatar_url="https://example.com/avatar.jpg"
)

session.add(user)  # Add the user
session.commit()  # Commit the change
