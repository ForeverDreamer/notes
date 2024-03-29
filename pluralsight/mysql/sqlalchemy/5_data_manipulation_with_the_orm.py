from pprint import pprint as pp

from sqlalchemy import insert, select, bindparam, and_, or_, func, desc, update, delete
from sqlalchemy.orm import Session, aliased

from utils import engine, init_orm, populate_orm_data, print_separator

User, Address = init_orm()

print_separator()
populate_orm_data(User, Address)

# Inserting Rows with the ORM
# Instances of Classes represent Rows
squidward = User(name="squidward", fullname="Squidward Tentacles")
print_separator()
print(squidward)
krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")
print_separator()
print(krabs)

# Adding objects to a Session
print_separator()
session = Session(engine)
session.add(squidward)
session.add(krabs)
print_separator()
print(session.new)

# Flushing
print_separator()
session.flush()

# Autogenerated primary key attributes
print_separator()
print(squidward.id)
print(krabs.id)

# Getting Objects by Primary Key from the Identity Map
print_separator()
some_squidward = session.get(User, 4)
print(some_squidward)
print(some_squidward is squidward)
print_separator()
session.commit()

# Updating ORM Objects
print_separator()
sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()
print_separator()
print(sandy)
print_separator()
sandy.fullname = "Sandy Squirrel"
print_separator()
print(sandy in session.dirty)
print_separator()
sandy_fullname = session.execute(select(User.fullname).where(User.id == 2)).scalar_one()
print_separator()
print(sandy_fullname)
print_separator()
print(sandy in session.dirty)

# ORM-enabled UPDATE statements
print_separator()
session.execute(
    update(User)
    .where(User.name == "sandy")
    .values(fullname="Sandy Squirrel Extraordinaire")
)
print_separator()
print(sandy.fullname)

# Deleting ORM Objects
print_separator()
patrick = session.get(User, 3)
print_separator()
session.delete(patrick)
print_separator()
session.execute(select(User).where(User.name == "patrick")).first()
print_separator()
print(patrick in session)

# ORM-enabled DELETE Statements
# refresh the target object for demonstration purposes
# only, not needed for the DELETE
print_separator()
squidward = session.get(User, 4)
print_separator()
session.execute(delete(User).where(User.name == "squidward"))
print_separator()
print(squidward in session)

# Rolling Back
print_separator()
session.rollback()
print_separator()
print(sandy.__dict__)
print_separator()
print(sandy.fullname)
print_separator()
print(patrick in session)
print_separator()
print(session.execute(select(User).where(User.name == "patrick")).scalar_one() is patrick)

# Closing a Session
print_separator()
session.close()
# print_separator()
# sqlalchemy.orm.exc.DetachedInstanceError: Instance <User at 0x23170b59550> is not bound to a Session;
# attribute refresh operation cannot proceed (Background on this error at: https://sqlalche.me/e/14/bhk3)
# print(squidward.name)
print_separator()
session.add(squidward)
print_separator()
print(squidward.name)
