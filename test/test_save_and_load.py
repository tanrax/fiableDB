import os
from fiable_db import start, add, save, get_database, load

filename = "fiabledb.json"


def delete_file():
    """Delete the database file."""
    if os.path.exists(filename):
        os.remove(filename)


def test_empty():
    """Test that save() works when the database is empty."""
    delete_file()
    start()
    save()
    load()
    assert get_database() == []


def test_one():
    """Test that save() works when the database has one entry."""
    delete_file()
    start()
    add({"name": "John", "age": 30})
    save()
    load()
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 30}}
    ]


def test_two():
    """Test that save() works when the database has two entries."""
    delete_file()
    start()
    add({"name": "John", "age": 30})
    add({"name": "Jane", "age": 28})
    save()
    load()
    assert get_database() == [
        {"id": 1, "rev": 1, "table": "default", "data": {"name": "John", "age": 30}},
        {"id": 2, "rev": 1, "table": "default", "data": {"name": "Jane", "age": 28}},
    ]
