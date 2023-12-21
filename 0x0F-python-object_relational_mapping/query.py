from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User, Base

engine = create_engine("mysql+mysqldb://root:root@localhost/test_user")
Session = sessionmaker(bind=engine)

session = Session()

results = session.query(User).order_by(User.id)

for instance in results:
    print(instance.name, instance.age)

session.commit()

session.close()
