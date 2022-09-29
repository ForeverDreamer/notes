from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, bindparam
from sqlalchemy.orm import registry, relationship, Session
from constants import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING, echo=True, future=True)


def init_core():
    metadata_obj = MetaData()

    user_table = Table(
        "user_account",
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('name', String(30)),
        Column('fullname', String(50))
    )

    address_table = Table(
        "address",
        metadata_obj,
        Column('id', Integer, primary_key=True),
        Column('user_id', ForeignKey('user_account.id'), nullable=False),
        Column('email_address', String(50), nullable=False)
    )

    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)

    return user_table, address_table


def populate_core_data(user_table, address_table):
    with engine.connect() as conn:
        conn.execute(
            insert(user_table),
            [
                {"name": "spongebob", "fullname": "Spongebob Squarepants"},
                {"name": "sandy", "fullname": "Sandy Cheeks"},
                {"name": "patrick", "fullname": "Patrick Star"}
            ]
        )
        scalar_subq = (
            select(user_table.c.id).
                where(user_table.c.name == bindparam('username')).
                scalar_subquery()
        )
        conn.execute(
            insert(address_table).values(user_id=scalar_subq),
            [
                {"username": 'spongebob', "email_address": "spongebob@sqlalchemy.org"},
                {"username": 'sandy', "email_address": "sandy@sqlalchemy.org"},
                {"username": 'patrick', "email_address": "patrick@sqlalchemy.org"},
            ]
        )
        conn.commit()


def init_orm():
    mapper_registry = registry()
    Base = mapper_registry.generate_base()

    class User(Base):
        __tablename__ = 'user_account'

        id = Column(Integer, primary_key=True)
        name = Column(String(30))
        fullname = Column(String(50))
        addresses = relationship("Address", back_populates="user")

        def __repr__(self):
            return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

    class Address(Base):
        __tablename__ = 'address'

        id = Column(Integer, primary_key=True)
        email_address = Column(String(50), nullable=False)
        user_id = Column(Integer, ForeignKey('user_account.id'))
        user = relationship("User", back_populates="addresses")

        def __repr__(self):
            return f"Address(id={self.id!r}, email_address={self.email_address!r})"

    mapper_registry.metadata.drop_all(engine)
    mapper_registry.metadata.create_all(engine)

    return User, Address


def populate_orm_data(User, Address):
    with Session(engine) as session:
        session.execute(
            insert(User),
            [
                {"name": "spongebob", "fullname": "Spongebob Squarepants"},
                {"name": "sandy", "fullname": "Sandy Cheeks"},
                {"name": "patrick", "fullname": "Patrick Star"}
            ]
        )
        scalar_subq = (
            select(User.id).
                where(User.name == bindparam('username')).
                scalar_subquery()
        )
        session.execute(
            insert(Address).values(user_id=scalar_subq),
            [
                {"username": 'spongebob', "email_address": "spongebob@sqlalchemy.org"},
                {"username": 'sandy', "email_address": "sandy@sqlalchemy.org"},
                {"username": 'patrick', "email_address": "patrick@sqlalchemy.org"},
            ]
        )
        session.commit()
