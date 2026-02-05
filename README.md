# Utilities for developing EHR utilities

Even utilities need utilities!

## Functions

* `fake_files` - provides test doubles for tsv files
* `fake_tables` - provides test doubles for SQLite tables

## Installation

```bash
pip install ehr-utils-utils
```

## Usage

### `fake_files`
The `fake_files` context manager takes tables (`list[list[str]]`), produces temporary tsv files from them, and yields the filenames. The temporary files will be deleted when the context is exited. 

Example usage:
```python
from ehr_utils_utils import fake_files

def test_my_parse_fcn():
    table = [["a", "b"], ["1", "2"]]
    with fake_files(table) as filenames:
        my_parse_fcn(filenames[0])
        ...
```

### `fake_tables`
The `fake_tables` context manager takes a dictionary mapping table names to their contents (`dict[str, list[list[Any]]]`), produces an in-memory SQLite database, and yields the connection. When the context is exited, connection will be closed, and the memory will be recycled. 

Example usage:
```python
from ehr_utils_utils import fake_tables

def test_my_sql_query():
    test_table = [["a", "b"], ["1", "2"], ["3", "4"]]
    with fake_tables({"my_table": test_table}) as connection:
        result = connection.execute("SELECT a FROM my_table WHERE b = '2'").fetchone()
        assert result == ("1",)
```

Alternatively, you can also use dynamic keyword arguments to specify the table name(s):
```python
from ehr_utils_utils import fake_tables

def test_my_sql_query():
    test_table = [["a", "b"], ["1", "2"], ["3", "4"]]
    with fake_tables(my_table=test_table) as connection:
        result = connection.execute("SELECT a FROM my_table WHERE b = '2'").fetchone()
        assert result == ("1",)
```

## Development

We welcome contributions! Before opening a pull request, please confirm that existing regression tests pass:

```python
python -m pytest tests/
```
