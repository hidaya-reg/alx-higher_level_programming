from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User, Base

engine = create_engine("mysql+mysqldb://root:root@localhost/test_user")
Session = sessionmaker(bind=engine)

session = Session()
ed = User(name='ed', age=65)
print(ed.name)
session.add(ed)
session.add_all([
    User(name='wendy', age=42),
    User(name='mary', age=25)])
session.commit()

session.close()
