from sqlalchemy import insert, select, bindparam

from utils import init_core


engine, user_table, address_table = init_core()

print('================================================')
stmt = insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants")
print(stmt)
compiled = stmt.compile()
print(compiled.params)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
    print(result.inserted_primary_key)
    print(result.inserted_primary_key.id)

with engine.connect() as conn:
    print('================================================')
    result = conn.execute(
        insert(user_table),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"}
        ]
    )
    conn.commit()
    print(result.is_insert)
    print(result.rowcount)

scalar_subq = (
    select(user_table.c.id).
    where(user_table.c.name == bindparam('username')).
    scalar_subquery()
)

with engine.connect() as conn:
    print('================================================')
    result = conn.execute(
        insert(address_table).values(user_id=scalar_subq),
        [
            {"username": 'spongebob', "email_address": "spongebob@sqlalchemy.org"},
            {"username": 'sandy', "email_address": "sandy@sqlalchemy.org"},
            {"username": 'sandy', "email_address": "sandy@squirrelpower.org"},
        ]
    )
    conn.commit()
    print(result.is_insert)
    print(result.rowcount)

print('================================================')
select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
)
print(insert_stmt)
with engine.connect() as conn:
    result = conn.execute(insert_stmt)
    conn.commit()
    print(result.is_insert)
    print(result.rowcount)
