from sqlalchemy import select, text, literal_column, func

from utils import engine, init_core, populate_core_data


user_table, address_table = init_core()

populate_core_data(user_table, address_table)

print('================================================')
stmt = select(user_table).where(user_table.c.name == 'spongebob')
print(stmt)

print('================================================')
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

print('================================================')
print(select(user_table))
print(select(user_table.c.name, user_table.c.fullname))

print('================================================')
stmt = (
    select(
        ("Username: " + user_table.c.name).label("username"),
    ).order_by(user_table.c.name)
)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.username}")

print('================================================')
stmt = (
    select(
        text("'some phrase'"), user_table.c.name
    ).order_by(user_table.c.name)
)
with engine.connect() as conn:
    print(conn.execute(stmt).all())


print('================================================')
stmt = (
    select(
        literal_column("'some phrase'").label("p"), user_table.c.name
    ).order_by(user_table.c.name)
)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.p}, {row.name}")

print('================================================')
print(user_table.c.name == 'squidward')
print(address_table.c.user_id > 10)

print('================================================')
print(select(user_table).where(user_table.c.name == 'squidward'))

print('================================================')
print(
    select(address_table.c.email_address).
    where(user_table.c.name == 'squidward').
    where(address_table.c.user_id == user_table.c.id)
)

print('================================================')
print(
    select(address_table.c.email_address).
    where(
         user_table.c.name == 'squidward',
         address_table.c.user_id == user_table.c.id
    )
)

print('================================================')
print(select(user_table.c.name))

print('================================================')
print(select(user_table.c.name, address_table.c.email_address))

print('================================================')
print(
    select(user_table.c.name, address_table.c.email_address).
    join_from(user_table, address_table)
)

print('================================================')
print(
    select(user_table.c.name, address_table.c.email_address).
    join(address_table)
)

print('================================================')
print(
    select(address_table.c.email_address).
    select_from(user_table).join(address_table)
)

print('================================================')
print(
    select(func.count('*')).select_from(user_table)
)

print('================================================')
print(
    select(address_table.c.email_address).
    select_from(user_table).
    join(address_table, user_table.c.id == address_table.c.user_id)
)

# There is also a method Select.outerjoin() that is equivalent to using .join(..., isouter=True).
# SQL also has a “RIGHT OUTER JOIN”. SQLAlchemy doesn’t render this directly;
# instead, reverse the order of the tables and use “LEFT OUTER JOIN”.
print('================================================')
print(
    select(user_table).join(address_table, isouter=True)
)

print('================================================')
print(
    select(user_table).join(address_table, full=True)
)

print('================================================')
print(select(user_table).order_by(user_table.c.name))

print('================================================')
count_fn = func.count(user_table.c.id)
print(count_fn)

print('================================================')
user_alias_1 = user_table.alias()
user_alias_2 = user_table.alias()
stmt = (
    select(user_alias_1.c.name, user_alias_2.c.name).
    join_from(user_alias_1, user_alias_2, user_alias_1.c.id > user_alias_2.c.id)
)
print(stmt)
with engine.connect() as conn:
    print('================================================')
    for row in conn.execute(stmt):
        print(row)