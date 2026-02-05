"""Test fake tables."""

from ehr_utils_utils import fake_tables


def test_fake_tables_positional():
    my_table = [["a", "b"], ["1", "2"], ["3", "4"]]
    with fake_tables({"my_table": my_table}) as connection:
        result = connection.execute("SELECT a FROM my_table WHERE b = '2'").fetchone()
    assert result == ("1",)


def test_fake_tables_kwarg():
    my_table = [["a", "b"], ["1", "2"], ["3", "4"]]
    with fake_tables(my_table=my_table) as connection:
        result = connection.execute("SELECT a FROM my_table WHERE b = '2'").fetchone()
    assert result == ("1",)


def test_fake_tables_both():
    my_table = [["a", "b"], ["1", "2"], ["3", "4"]]
    my_second_table = [["c", "d"], ["5", "6"], ["7", "8"]]
    with fake_tables(
        {"my_table": my_table}, my_second_table=my_second_table
    ) as connection:
        a_result = connection.execute("SELECT a FROM my_table WHERE b = '2'").fetchone()
        c_result = connection.execute(
            "SELECT c FROM my_second_table WHERE d = '8'"
        ).fetchone()
    assert a_result == ("1",)
    assert c_result == ("7",)
