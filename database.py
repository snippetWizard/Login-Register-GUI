import sqlalchemy
from model.users import User 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()



if __name__ == "__main__":
	u = User()

	sesh = sessionmaker(bind=create_engine('mysql://root@127.0.0.1/test?'))

	with sesh() as s:
		s.add(u)
		s.commit()