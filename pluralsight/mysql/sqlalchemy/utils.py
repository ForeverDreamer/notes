from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

from constants import CONNECTION_STRING


def init_core(echo=True):
    engine = create_engine(CONNECTION_STRING, echo=echo, future=True)

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

    return engine, user_table, address_table
