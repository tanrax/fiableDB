from fiable_db import start, add, delete, get_database


def test_delete_simple():
    """Test delete in the default table."""
    start()
    add(
        [
            {"name": "Noelia", "age": 34, "height": 165},
            {"name": "Juan", "age": 41, "height": 187},
            {"name": "Valentina", "age": 12, "height": 142},
        ]
    )
    delete(1)
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
        {"id": 1, "rev": 2, "table": "default", "data": {}},
    ]


def test_delete_multiple():
    """Test delete two rows"""
    start()
    add(
        [
            {"name": "Noelia", "age": 34, "height": 165},
            {"name": "Juan", "age": 41, "height": 187},
            {"name": "Valentina", "age": 12, "height": 142},
        ]
    )
    delete(2)
    delete(3)
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
        {"id": 2, "rev": 2, "table": "default", "data": {}},
        {"id": 3, "rev": 2, "table": "default", "data": {}},
    ]


def test_delete_with_table():
    """Test delete two rows"""
    start()
    add(
        [
            {"name": "Noelia", "age": 34, "height": 165},
            {"name": "Juan", "age": 41, "height": 187},
            {"name": "Valentina", "age": 12, "height": 142},
        ],
        table="people",
    )
    add(
        [
            {"name": "Mortadelo", "age": 22, "height": 184},
            {"name": "Filemon", "age": 25, "height": 185},
        ],
    )
    delete(2, table="people")
    delete(1)
    assert get_database() == [
        {
            "id": 1,
            "rev": 1,
            "table": "people",
            "data": {"name": "Noelia", "age": 34, "height": 165},
        },
        {
            "id": 2,
            "rev": 1,
            "table": "people",
            "data": {"name": "Juan", "age": 41, "height": 187},
        },
        {
            "id": 3,
            "rev": 1,
            "table": "people",
            "data": {"name": "Valentina", "age": 12, "height": 142},
        },
        {
            "id": 1,
            "rev": 1,
            "table": "default",
            "data": {"name": "Mortadelo", "age": 22, "height": 184},
        },
        {
            "id": 2,
            "rev": 1,
            "table": "default",
            "data": {"name": "Filemon", "age": 25, "height": 185},
        },
        {"id": 2, "rev": 2, "table": "people", "data": {}},
        {"id": 1, "rev": 2, "table": "default", "data": {}},
    ]
