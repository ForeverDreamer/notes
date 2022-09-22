from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from constants import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING, echo=True, future=True)

with Session(engine) as session:
    result = session.execute(text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y"), {"y": 6})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")

with Session(engine) as session:
    print('========================================')
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}]
    )
    session.commit()
