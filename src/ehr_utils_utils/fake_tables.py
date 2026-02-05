from contextlib import contextmanager
import sqlite3
from typing import Any, Generator


@contextmanager
def fake_tables(
    tables: dict[str, list[list[Any]]] | None = None, **kwargs: list[list[Any]]
) -> Generator[sqlite3.Connection, None, None]:
    """Generate fake tables from data arrays."""
    if tables is None:
        tables = {}
    tables |= kwargs
    with sqlite3.connect(":memory:") as connection:
        for name, data in tables.items():
            connection.execute(f"CREATE TABLE {name}({{}})".format(", ".join(data[0])))
            connection.executemany(
                f"INSERT INTO {name} VALUES({{}})".format(
                    ", ".join(f":{column}" for column in data[0])
                ),
                [dict(zip(data[0], row)) for row in data[1:]],
            )
            connection.commit()
        yield connection
