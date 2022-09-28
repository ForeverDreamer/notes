from sqlalchemy import insert, select, bindparam

from utils import engine, init_core, init_orm


user_table, address_table = init_core()

with engine.connect() as conn:
    result = conn.execute(insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants"))
    conn.commit()

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
