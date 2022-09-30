from pprint import pprint as pp

from sqlalchemy import insert, select, bindparam, and_, or_, func, desc
from sqlalchemy.orm import Session, aliased

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

print('================================================')
print(
    select(Address.email_address).
    where(
        and_(
            or_(User.name == 'squidward', User.name == 'sandy'),
            Address.user_id == User.id
        )
    )
)

print('================================================')
print(
    select(User).filter_by(name='spongebob', fullname='Spongebob Squarepants')
)

print('================================================')
print(select(User).order_by(User.fullname.desc()))

print('================================================')
with Session(engine) as session:
    scalar_subq = (
        select(User.id).
        where(User.name == bindparam('username')).
        scalar_subquery()
    )
    session.execute(
        insert(Address).values(user_id=scalar_subq),
        [
            {"username": 'sandy', "email_address": "sandy@gmail.org"},
            {"username": 'patrick', "email_address": "patrick@gmail.org"},
        ]
    )
    session.commit()
with Session(engine) as session:
    result = session.execute(
        select(User.name, Address.id, Address.email_address, Address.user_id).join(Address)
    )
    pp(result.all())
    print('================================================')
    result = session.execute(
        select(User.name, func.count(Address.id).label("count")).
        join(Address).
        group_by(User.name).
        having(func.count(Address.id) > 1)
    )
    print(result.all())


print('================================================')
stmt = (
    select(Address.user_id, func.count(Address.id).label('num_addresses')).
    group_by("user_id").
    order_by("user_id", desc("num_addresses"))
)
print(stmt)
with Session(engine) as session:
    print('================================================')
    result = session.execute(stmt)
    print(result.all())

print('================================================')
address_alias_1 = aliased(Address)
address_alias_2 = aliased(Address)

with Session(engine) as session:
    print('================================================')
    result = session.execute(
        select(User).
        join_from(User, address_alias_1).
        join_from(User, address_alias_2)
    )
    pp(result.all())

stmt = (
    select(User).
    join_from(User, address_alias_1).
    where(address_alias_1.email_address == 'patrick@sqlalchemy.org').
    join_from(User, address_alias_2).
    where(address_alias_2.email_address == 'patrick@gmail.org')
)
print(stmt)
with Session(engine) as session:
    print('================================================')
    result = session.execute(stmt)
    pp(result.all())
