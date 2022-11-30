from fiable_db import add, get_database


def test_add_one():
    """Add one item to the database."""
    add({"name": "John", "age": 42})
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}}
    ]


def test_add_two():
    """Add two items to the database."""
    add({"name": "John", "age": 12})
    add({"name": "Jane", "age": 34})
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 3, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
    ]


def test_add_list():
    """Add a list of items to the database."""
    add(
        [
            {"name": "John", "age": 12},
            {"name": "Jane", "age": 34},
        ]
    )
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 3, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 4, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 5, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
    ]


def test_add_list_with_one():
    """Add a list with one item to the database."""
    add([{"name": "John", "age": 42}])
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 3, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 4, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 5, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 6, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
    ]


def test_add_empty():
    """Add an empty list to the database."""
    add([])
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 3, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 4, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 5, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 6, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
    ]


def test_add_in_table_foo():
    """Add an item to the database in the table foo."""
    add({"name": "John", "age": 42}, table="foo")
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 3, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 4, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 5, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 6, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 1, "rev": 1, "table": "foo", "data": {"name": "John", "age": 42}},
    ]
    add({"name": "Simone", "age": 33}, table="foo")
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 3, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 4, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 5, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 6, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 1, "rev": 1, "table": "foo", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "foo", "data": {"name": "Simone", "age": 33}},
    ]
    add({"name": "Jose", "age": 25})
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 3, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 4, "rev": 1, "table": "default", "data": {"name": "John", "age": 12}},
        {"id": 5, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 34}},
        {"id": 6, "rev": 1, "table": "default", "data": {"name": "John", "age": 42}},
        {"id": 1, "rev": 1, "table": "foo", "data": {"name": "John", "age": 42}},
        {"id": 2, "rev": 1, "table": "foo", "data": {"name": "Simone", "age": 33}},
        {"id": 7, "rev": 1, "table": "default", "data": {"name": "Jose", "age": 25}},
    ]
