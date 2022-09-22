from sqlalchemy import create_engine, text

from constants import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING, echo=True, future=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print('========================================')
    print(result.all())

# "commit as you go"
with engine.connect() as conn:
    print('========================================')
    conn.execute(text("DROP TABLE IF EXISTS some_table;"))
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    conn.commit()

# "begin once"
with engine.begin() as conn:
    print('========================================')
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
    )

# Fetching Rows
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    print('========================================')
    # Tuple Assignment
    for x, y in result:
        print(f"x: {x}  y: {y}")
    result = conn.execute(text("SELECT x, y FROM some_table"))
    print('========================================')
    # Integer Index
    for row in result:
        print(f"x: {row[0]}  y: {row[1]}")
    result = conn.execute(text("SELECT x, y FROM some_table"))
    print('========================================')
    # Attribute Name
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
    result = conn.execute(text("SELECT x, y FROM some_table"))
    print('========================================')
    # Mapping Access
    for row in result.mappings():
        print(f"x: {row['x']}  y: {row['y']}")

# Sending Parameters
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT x, y FROM some_table WHERE y > :y"),
        {"y": 2}
    )
    print('========================================')
    for row in result:
        print(f"x: {row.x}  y: {row.y}")

# Sending Multiple Parameters
with engine.connect() as conn:
    print('========================================')
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
    )
    conn.commit()
