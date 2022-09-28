from sqlalchemy import insert, select, bindparam
from sqlalchemy.orm import Session

from utils import engine, init_orm, populate_orm_data

User, Address = init_orm()

print('================================================')
populate_orm_data(User, Address)

print('================================================')
stmt = select(User).where(User.name == 'spongebob')
print(stmt)

print('================================================')
with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)

print('================================================')
print(select(User))
print('================================================')
with Session(engine) as session:
    row = session.execute(select(User)).first()
    print(row)
    print(row[0])
    print('================================================')
    user = session.scalars(select(User)).first()
    print(user)

print('================================================')
print(select(User.name, User.fullname))
print('================================================')
with Session(engine) as session:
    row = session.execute(select(User.name, User.fullname)).first()
    print(row)

print('================================================')
with Session(engine) as session:
    rows = session.execute(
        select(User.name, Address).
        where(User.id == Address.user_id).
        order_by(Address.id)
    ).all()
    print(rows)
