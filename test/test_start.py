import os
import shutil
from fiable_db import start, get_database


def test_create_new_file():
    """Create a new file with a different name"""
    filename = "test.json"
    start(filename)
    assert os.path.isfile(filename), "The file does not exist"
    # Remove the file
    os.remove(filename)


def test_create_default_file():
    """Create a new file with the default name"""
    filename = "fiabledb.json"
    start()
    assert os.path.isfile(filename), "The file does not exist"
    # Remove the file
    os.remove(filename)


def test_read_file_default():
    """Read the default file"""
    input_file = "test/example.json"
    output_file = "fiabledb.json"
    shutil.copy(input_file, output_file)
    start()
    data = get_database()
    assert data == [
        {"id": 2, "rev": 1, "data": {"name": "Noelia", "age": 34, "height": 165}},
        {"id": 3, "rev": 1, "data": {"name": "Juan", "age": 41, "height": 187}},
        {"id": 4, "rev": 1, "data": {"name": "Valentina", "age": 12, "height": 142}},
    ], "The data is not the same: " + str(data)
    os.remove(output_file)


def test_read_file_custom_name():
    """Read a file with a custom name"""
    filename = "test/example.json"
    start(filename)
    data = get_database()
    assert data == [
        {"id": 2, "rev": 1, "data": {"name": "Noelia", "age": 34, "height": 165}},
        {"id": 3, "rev": 1, "data": {"name": "Juan", "age": 41, "height": 187}},
        {"id": 4, "rev": 1, "data": {"name": "Valentina", "age": 12, "height": 142}},
    ], "The data is not the same: " + str(data)
