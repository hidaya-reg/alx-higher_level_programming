from sqlalchemy import create_engine
from user import User, Base

engine = create_engine("mysql+mysqldb://root:root@localhost/test_user")
Base.metadata.create_all(engine)
print(User.__table__)
