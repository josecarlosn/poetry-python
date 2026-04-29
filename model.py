

from sqlalchemy import create_engine, Column, UUID, String, Boolean
from sqlalchemy.orm import declarative_base

db = create_engine("http://localhost:5432")
base = declarative_base()

def User(base):
    __table__ = "users"

    id = Column("id", UUID, nullable=False, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False)
    password = Column("password", String, nullable=False)
    active = Column("active", Boolean, nullable=False, default=True)
    admin = Column("admin", Boolean, nullable=False, default=False)

    def __init__(self,  name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin
