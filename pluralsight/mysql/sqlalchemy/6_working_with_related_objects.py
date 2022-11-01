from sqlalchemy import insert, select, bindparam, and_, or_, func, desc, update, delete
from sqlalchemy.orm import Session, aliased

from utils import engine, init_orm, populate_orm_data, print_separator

User, Address = init_orm()


# Persisting and Loading Relationships
print_separator()
u1 = User(name="pkrabs", fullname="Pearl Krabs")
print(u1.addresses)
a1 = Address(email_address="pearl.krabs@gmail.com")
u1.addresses.append(a1)
print_separator()
print(u1.addresses)
print_separator()
print(a1.user)
a2 = Address(email_address="pearl@aol.com", user=u1)
# equivalent effect as a2 = Address(user=u1)
# a2.user = u1
print_separator()
print(u1.addresses)

# Cascading Objects into the Session
session = Session(engine)
print_separator()
session.add(u1)
print(u1 in session)
print(a1 in session)
print(a2 in session)
print_separator()
print(u1.id)
print(a1.user_id)
print_separator()
session.commit()

# Loading Relationships
print_separator()
print(u1.id)
print_separator()
print(u1.addresses)
print_separator()
# We may access u1.addresses again as well as add or remove items and this will not incur any new SQL calls
print(u1.addresses)
print(a1)
print(a2)

# Using Relationships in Queries
# Using Relationships to Join
print_separator()
print(select(Address.email_address).select_from(User).join(User.addresses))
print_separator()
print(select(Address.email_address).join_from(User, Address))

# Joining between Aliased targets
print_separator()
address_alias_1 = aliased(Address)
address_alias_2 = aliased(Address)
print(
    select(User)
    .join(User.addresses.of_type(address_alias_1))
    .where(address_alias_1.email_address == "patrick@aol.com")
    .join(User.addresses.of_type(address_alias_2))
    .where(address_alias_2.email_address == "patrick@gmail.com")
)
print_separator()
user_alias_1 = aliased(User)
print(select(user_alias_1.name).join(user_alias_1.addresses))

# Augmenting the ON Criteria
stmt = select(User.fullname).join(
    User.addresses.and_(Address.email_address == "pearl.krabs@gmail.com")
)
print_separator()
print(stmt)
print_separator()
print(session.execute(stmt).all())

# EXISTS forms: has() / any()
stmt = select(User.fullname).where(
    User.addresses.any(Address.email_address == "pearl.krabs@gmail.com")
)
print_separator()
print(stmt)
print_separator()
print(session.execute(stmt).all())

stmt = select(User.fullname).where(~User.addresses.any())
print_separator()
print(stmt)
print(session.execute(stmt).all())

stmt = select(Address.email_address).where(Address.user.has(User.name == "pkrabs"))
print_separator()
print(stmt)
print_separator()
print(session.execute(stmt).all())

# Common Relationship Operators
# many to one equals comparison
print_separator()
print(select(Address).where(Address.user == u1))
# many to one not equals comparison
print_separator()
print(select(Address).where(Address.user != u1))
# object is contained in a one-to-many collection
print_separator()
print(select(User).where(User.addresses.contains(a1)))
# An object has a particular parent from a one-to-many perspective
from sqlalchemy.orm import with_parent
print_separator()
stmt = select(Address).where(with_parent(u1, User.addresses))
print(stmt)
print_separator()
print(session.execute(stmt).all())

# Loader Strategies
# Selectin Load
from sqlalchemy.orm import selectinload
# stmt = select(User).order_by(User.id)
stmt = select(User).options(selectinload(User.addresses)).order_by(User.id)
print_separator()
print(stmt)
print_separator()
for row in session.execute(stmt):
    print(
        f"{row.User.name}  ({', '.join(a.email_address for a in row.User.addresses)})"
    )

# Joined Load
from sqlalchemy.orm import joinedload
stmt = (
    select(Address)
    .options(joinedload(Address.user, innerjoin=True))
    .order_by(Address.id)
)
print_separator()
print(stmt)
print_separator()
for row in session.execute(stmt):
    print(f"{row.Address.email_address} {row.Address.user.name}")

# Explicit Join + Eager load
# 略
# Augmenting Loader Strategy Paths
# 略
# Raiseload
# 略
