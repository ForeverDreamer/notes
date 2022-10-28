from sqlalchemy import select, text, literal_column, func, Column, Integer, String

from utils import engine, init_core, populate_core_data, print_separator


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

print_separator()
subq = (
    select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
    .group_by(address_table.c.user_id)
    .subquery()
)
print(subq)

print_separator()
print(select(subq.c.user_id, subq.c.count))

print_separator()
stmt = select(user_table.c.name, user_table.c.fullname, subq.c.count).join_from(
    user_table, subq
)
print(stmt)

print_separator()
subq = (
    select(func.count(address_table.c.id).label("count"), address_table.c.user_id)
    .group_by(address_table.c.user_id)
    .cte()
)
stmt = select(user_table.c.name, user_table.c.fullname, subq.c.count).join_from(
    user_table, subq
)
print(stmt)

print_separator()
subq = select(func.count(address_table.c.id)).\
            where(user_table.c.id == address_table.c.user_id).\
            scalar_subquery()
print(subq)
stmt = select(user_table.c.name, subq.label("address_count"))
print(stmt)
with engine.connect() as conn:
    print_separator()
    for row in conn.execute(stmt):
        print(row)

print_separator()
subq = select(func.count(address_table.c.id)).\
            where(user_table.c.id == address_table.c.user_id).\
            scalar_subquery().correlate(user_table)
print(subq)
with engine.connect() as conn:
    stmt = select(
        user_table.c.name,
        address_table.c.email_address,
        subq.label("address_count")
    ).\
        join_from(user_table, address_table).\
        order_by(user_table.c.id, address_table.c.id)
    print_separator()
    print(stmt)
    result = conn.execute(stmt)
    print_separator()
    print(result.all())

print_separator()
subq = (
  select(
      func.count(address_table.c.id).label("address_count"),
      address_table.c.email_address,
      address_table.c.user_id
  ).
      where(user_table.c.id == address_table.c.user_id).
      lateral()
)
stmt = select(
    user_table.c.name,
    subq.c.address_count,
    subq.c.email_address
). \
    join_from(user_table, subq). \
    order_by(user_table.c.id, subq.c.email_address)
print(stmt)

print_separator()
from sqlalchemy import union_all
stmt1 = select(user_table).where(user_table.c.name == 'sandy')
stmt2 = select(user_table).where(user_table.c.name == 'spongebob')
u = union_all(stmt1, stmt2)
print(u)
with engine.connect() as conn:
    print_separator()
    result = conn.execute(u)
    print(result.all())

print_separator()
u_subq = u.subquery()
print(u_subq)
stmt = (
    select(u_subq.c.name, address_table.c.email_address).
    join_from(address_table, u_subq).
    order_by(u_subq.c.name, address_table.c.email_address)
)
print_separator()
print(stmt)
with engine.connect() as conn:
    print_separator()
    result = conn.execute(stmt)
    print(result.all())

print_separator()
subq = (
    select(func.count(address_table.c.id)).
    where(user_table.c.id == address_table.c.user_id).
    group_by(address_table.c.user_id).
    having(func.count(address_table.c.id) > 0)
).exists()
print(subq)
with engine.connect() as conn:
    print_separator()
    result = conn.execute(
        select(user_table.c.name).where(subq)
    )
    print(result.all())

print_separator()
subq = (
    select(address_table.c.id).
    where(user_table.c.id == address_table.c.user_id)
).exists()
print(subq)
with engine.connect() as conn:
    result = conn.execute(
        select(user_table.c.name).where(~subq)
    )
    print(result.all())

# Working with SQL Functions
print_separator()
print(select(func.count()).select_from(user_table))

print_separator()
print(select(func.lower("A String With Much UPPERCASE")))

print_separator()
stmt = select(func.now())
print(stmt)
with engine.connect() as conn:
    print_separator()
    result = conn.execute(stmt)
    print(result.all())

print_separator()
print(select(func.some_crazy_function(user_table.c.name, 17)))

print_separator()
from sqlalchemy.dialects import postgresql
print(select(func.now()).compile(dialect=postgresql.dialect()))
print_separator()
from sqlalchemy.dialects import oracle
print(select(func.now()).compile(dialect=oracle.dialect()))

# Functions Have Return Types
print_separator()
print(func.now().type)

print_separator()
from sqlalchemy import JSON
function_expr = func.json_object('{a, 1, b, "def", c, 3.5}', type_=JSON)
stmt = select(function_expr["def"])
print(stmt)

# Built-in Functions Have Pre-Configured Return Types
print_separator()
m1 = func.max(Column("some_int", Integer))
print(m1.type)

print_separator()
m2 = func.max(Column("some_str", String))
print(m2.type)

print_separator()
print(func.now().type)
print(func.current_date().type)

print_separator()
print(func.concat("x", "y").type)

print_separator()
print(func.upper("lowercase").type)

print_separator()
print(select(func.upper("lowercase") + " suffix"))

# Advanced SQL Function Techniques
# Using Window Functions
print_separator()
stmt = select(
    func.row_number().over(partition_by=user_table.c.name),
    user_table.c.name,
    address_table.c.email_address
).select_from(user_table).join(address_table)
print(stmt)
with engine.connect() as conn:
    print_separator()
    result = conn.execute(stmt)
    print(result.all())

print_separator()
stmt = select(
    func.count().over(order_by=user_table.c.name),
    user_table.c.name,
    address_table.c.email_address).select_from(user_table).join(address_table)
print(stmt)
with engine.connect() as conn:
    print_separator()
    result = conn.execute(stmt)
    print(result.all())

# Table-Valued Functions
from sqlalchemy import select, func
print_separator()
stmt = select(func.json_array_elements('["one", "two"]').column_valued("x"))
print(stmt)

from sqlalchemy.dialects import oracle
print_separator()
stmt = select(func.scalar_strings(5).column_valued("s"))
print(stmt.compile(dialect=oracle.dialect()))

# Data Casts and Type Coercion
from sqlalchemy import cast
print_separator()
stmt = select(cast(user_table.c.id, String))
print(stmt)
with engine.connect() as conn:
    print_separator()
    result = conn.execute(stmt)
    print(result.all())

from sqlalchemy import JSON
print_separator()
print(cast("{'a': 'b'}", JSON)["a"])

# type_coerce() - a Python-only “cast”
import json
from sqlalchemy import JSON
from sqlalchemy import type_coerce
from sqlalchemy.dialects import mysql
print_separator()
s = select(
    type_coerce(
        {'some_key': {'foo': 'bar'}}, JSON
    )['some_key']
)
print(s.compile(dialect=mysql.dialect()))


# Updating and Deleting Rows with Core
# The update() SQL Expression Construct
from sqlalchemy import update
stmt = (
    update(user_table)
    .where(user_table.c.name == "patrick")
    .values(fullname="Patrick the Star")
)
print_separator()
print(stmt)

print_separator()
stmt = update(user_table).values(fullname="Username: " + user_table.c.name)
print(stmt)

print_separator()
from sqlalchemy import bindparam
stmt = (
    update(user_table)
    .where(user_table.c.name == bindparam("oldname"))
    .values(name=bindparam("newname"))
)
print(stmt)
with engine.begin() as conn:
    print_separator()
    conn.execute(
        stmt,
        [
            {"oldname": "jack", "newname": "ed"},
            {"oldname": "wendy", "newname": "mary"},
            {"oldname": "jim", "newname": "jake"},
        ],
    )

# Correlated Updates
scalar_subq = (
    select(address_table.c.email_address)
    .where(address_table.c.user_id == user_table.c.id)
    .order_by(address_table.c.id)
    .limit(1)
    .scalar_subquery()
)
update_stmt = update(user_table).values(fullname=scalar_subq)
print_separator()
print(update_stmt)

# UPDATE..FROM
update_stmt = (
    update(user_table)
    .where(user_table.c.id == address_table.c.user_id)
    .where(address_table.c.email_address == "patrick@aol.com")
    .values(fullname="Pat")
)
print_separator()
print(update_stmt)

update_stmt = (
    update(user_table)
    .where(user_table.c.id == address_table.c.user_id)
    .where(address_table.c.email_address == "patrick@aol.com")
    .values(
        {user_table.c.fullname: "Pat", address_table.c.email_address: "pat@aol.com"}
    )
)
from sqlalchemy.dialects import mysql
print_separator()
print(update_stmt.compile(dialect=mysql.dialect()))

# Parameter Ordered Updates
# update_stmt = update(some_table).ordered_values(
#     (some_table.c.y, 20), (some_table.c.x, some_table.c.y + 10)
# )
# print(update_stmt)

# The delete() SQL Expression Construct
from sqlalchemy import delete
stmt = delete(user_table).where(user_table.c.name == "patrick")
print_separator()
print(stmt)

# Multiple Table Deletes
delete_stmt = (
    delete(user_table)
    .where(user_table.c.id == address_table.c.user_id)
    .where(address_table.c.email_address == "patrick@aol.com")
)
from sqlalchemy.dialects import mysql
print_separator()
print(delete_stmt.compile(dialect=mysql.dialect()))

# Getting Affected Row Count from UPDATE, DELETE
with engine.begin() as conn:
    print_separator()
    result = conn.execute(
        update(user_table)
        .values(fullname="Patrick McStar")
        .where(user_table.c.name == "patrick")
    )
    print(result.rowcount)

# Using RETURNING with UPDATE, DELETE
update_stmt = (
    update(user_table)
    .where(user_table.c.name == "patrick")
    .values(fullname="Patrick the Star")
    .returning(user_table.c.id, user_table.c.name)
)
print_separator()
print(update_stmt)


delete_stmt = (
    delete(user_table)
    .where(user_table.c.name == "patrick")
    .returning(user_table.c.id, user_table.c.name)
)
print_separator()
print(delete_stmt)


