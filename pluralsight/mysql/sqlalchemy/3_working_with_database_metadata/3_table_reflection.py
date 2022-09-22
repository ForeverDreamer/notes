from sqlalchemy import create_engine, Table, text
from sqlalchemy.orm import registry

from constants import CONNECTION_STRING

mapper_registry = registry()

engine = create_engine(CONNECTION_STRING, echo=True, future=True)

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
#     )
#     conn.commit()

some_table = Table("some_table", mapper_registry.metadata, autoload_with=engine)
print('========================================')
print(repr(some_table))
