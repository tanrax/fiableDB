from fiable_db import start, add, update, get_database


def test_update_simple():
    """Test update in the default table."""
    start()
    add(
        [
            {"name": "Noelia", "age": 34, "height": 165},
            {"name": "Juan", "age": 41, "height": 187},
            {"name": "Valentina", "age": 12, "height": 142},
        ]
    )
    update(2, {"age": 99})
    assert get_database() == [
        {
            "id": 1,
            "rev": 1,
            "table": "default",
            "data": {"name": "Noelia", "age": 34, "height": 165},
        },
        {
            "id": 2,
            "rev": 1,
            "table": "default",
            "data": {"name": "Juan", "age": 41, "height": 187},
        },
        {
            "id": 3,
            "rev": 1,
            "table": "default",
            "data": {"name": "Valentina", "age": 12, "height": 142},
        },
        {
            "id": 2,
            "rev": 2,
            "table": "default",
            "data": {"name": "Juan", "age": 99, "height": 187},
        },
    ]
    update(2, {"name": "Cristo"})
    assert get_database() == [
        {
            "id": 1,
            "rev": 1,
            "table": "default",
            "data": {"name": "Noelia", "age": 34, "height": 165},
        },
        {
            "id": 2,
            "rev": 1,
            "table": "default",
            "data": {"name": "Juan", "age": 41, "height": 187},
        },
        {
            "id": 3,
            "rev": 1,
            "table": "default",
            "data": {"name": "Valentina", "age": 12, "height": 142},
        },
        {
            "id": 2,
            "rev": 2,
            "table": "default",
            "data": {"name": "Juan", "age": 99, "height": 187},
        },
        {
            "id": 2,
            "rev": 3,
            "table": "default",
            "data": {"name": "Cristo", "age": 99, "height": 187},
        },
    ]
    update(1, {"height": 150})
    assert get_database() == [
        {
            "id": 1,
            "rev": 1,
            "table": "default",
            "data": {"name": "Noelia", "age": 34, "height": 165},
        },
        {
            "id": 2,
            "rev": 1,
            "table": "default",
            "data": {"name": "Juan", "age": 41, "height": 187},
        },
        {
            "id": 3,
            "rev": 1,
            "table": "default",
            "data": {"name": "Valentina", "age": 12, "height": 142},
        },
        {
            "id": 2,
            "rev": 2,
            "table": "default",
            "data": {"name": "Juan", "age": 99, "height": 187},
        },
        {
            "id": 2,
            "rev": 3,
            "table": "default",
            "data": {"name": "Cristo", "age": 99, "height": 187},
        },
        {
            "id": 1,
            "rev": 2,
            "table": "default",
            "data": {"name": "Noelia", "age": 34, "height": 150},
        },
    ]


def test_update_table():
    """Test update in a table."""
    add({"name": "Antony", "age": 77, "height": 188}, table="users")
    update(1, {"age": 99}, table="users")
    assert get_database() == [
        {
            "id": 1,
            "rev": 1,
            "table": "default",
            "data": {"name": "Noelia", "age": 34, "height": 165},
        },
        {
            "id": 2,
            "rev": 1,
            "table": "default",
            "data": {"name": "Juan", "age": 41, "height": 187},
        },
        {
            "id": 3,
            "rev": 1,
            "table": "default",
            "data": {"name": "Valentina", "age": 12, "height": 142},
        },
        {
            "id": 2,
            "rev": 2,
            "table": "default",
            "data": {"name": "Juan", "age": 99, "height": 187},
        },
        {
            "id": 2,
            "rev": 3,
            "table": "default",
            "data": {"name": "Cristo", "age": 99, "height": 187},
        },
        {
            "id": 1,
            "rev": 2,
            "table": "default",
            "data": {"name": "Noelia", "age": 34, "height": 150},
        },
        {
            "id": 1,
            "rev": 1,
            "table": "users",
            "data": {"name": "Antony", "age": 77, "height": 188},
        },
        {
            "id": 1,
            "rev": 2,
            "table": "users",
            "data": {"name": "Antony", "age": 99, "height": 188},
        },
    ]
  
def test_update_table_not_exists():
    """Test update in a table that not exists."""
    pass

def test_update_id_not_exists():
    """Test update with an id that not exists."""
    pass

def test_update_multiple_values_default():
    """Test update multiple values in the default table."""
    pass

def test_update_multiple_values_table():
    """Test update multiple values in a table."""
    pass

def test_update_with_keys_not_exists():
    """Test update with keys that not exists."""
    pass

def test_update_with_force():
    """Test update with force."""
    pass
