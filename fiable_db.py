from os import path
import json
from typing import Dict, Tuple, Union, Sequence, TypedDict

# Variables
FILE = "fiabledb.json"
database = {}

# Type aliases
class TypeData(TypedDict):
    id: int
    rev: int
    data: dict


Type_Data_List = Tuple[TypeData]
Type_Add_Data = Union[Dict, Sequence[Dict]]
Type_Add_Return = Union[Tuple[int, int, Dict], Tuple[Tuple[int, int, Dict]], None]
Type_Update_Return = Union[Tuple[Tuple[int, int, Dict]]]

Type_Delete_Return = Union[Tuple[Tuple[int, int, Dict]]]
Type_Find_One_Return = TypeData
Type_Find_All_Return = Tuple[Type_Find_One_Return]


def start(file_name: str = "") -> str:
    """Start the database
    Args:
        file (str, optional): The file to use. Defaults to FILE.
    Returns:
        str: The file used
    """
    global database
    my_file_name = file_name if file_name else FILE
    if path.exists(my_file_name):
        # Load the database
        load(my_file_name)
    else:
        # Create the database
        save(my_file_name, database)
    return my_file_name


def save(file_name: str = "", data: TypeData = {}) -> bool:
    """Save the database
    Args:
        file_name (str, optional): The file to save to. Defaults to "".
        data (list[str, list[int, int, dict]], optional): The data to save. Defaults to {}.
    Returns:
        bool: True if the data was saved, False otherwise
    """
    global database
    my_file_name = file_name if file_name else FILE
    with open(my_file_name, "w") as f:
        database = json.dump({}, f)
    return True


def load(file_name: Union[str, None] = None) -> bool:
    """Load the database
    Args:
        file_name (str, optional): The file to load from. Defaults to "".
    Returns:
        Bool - The data loaded
    """
    global database
    my_file_name = file_name if file_name else FILE
    is_exists = path.exists(my_file_name)
    if is_exists:
        with open(my_file_name, "r") as f:
            text = f.read()
            if text != "":
                database = json.loads(text)
            else:
                database = []
    else:
        raise FileNotFoundError("File not found")
    return is_exists


def get_database() -> Type_Data_List:
    """Get the data
    Returns:
        list[dict[int, int, dict]]: The data
    """
    global database
    return database


def add(new_data: Type_Add_Data, table: str = "") -> Type_Add_Return:
    """Add data to the database
    Args:
        new_data (dict|list): The data to add
        table (str, optional): The table to add to. Defaults to "".
    Returns:
        dict[int, int, dict]|list[dict[int, int, dict]]: The data added
    """
    if isinstance(new_data, dict):
        return _add(new_data, table)
    elif isinstance(new_data, list):
        return [_add(entry, table) for entry in new_data]
    else:
        raise TypeError("new_data must be a dict or list")
    print("Function not implemented yet")


def update(
    id: int, new_data: dict, table: str = "", force: bool = False
) -> Type_Update_Return:
    """Update data in the database
    Args:
        id (int): The id of the data to update.
        new_data (dict): The data to update
        table (str, optional): The table to update. Defaults to "".
        force (bool, optional): Force the update. Defaults to False.
    Returns:
        dict[int, int, dict]: The data updated
    """
    print("Function not implemented yet")


def delete(id: int, data: dict, table: str = "") -> Type_Delete_Return:
    """Delete data from the database
    Args:
        id (int): The id of the data to delete
        data (dict): Filter the data to delete
        table (str, optional): The table to delete from. Defaults to "".
    Returns:
        dict[int, int, dict]: The data deleted
    """
    print("Function not implemented yet")


def find_one(
    id: int = 0, data: dict = {}, table: str = "", rev: int = 0
) -> Type_Find_One_Return:
    """Find one data in the database
    Args:
        id (int, optional): The id of the data to find. Defaults to 0.
        data (dict, optional): Filter the data to find. Defaults to {}.
        table (str, optional): The table to find in. Defaults to "".
        rev (int, optional): The revision of the data to find. Defaults to 0.
    Returns:
        dict[int, int, dict]: The data found
    """
    print("Function not implemented yet")


def find_all(data: dict = {}, table: str = "") -> Type_Find_All_Return:
    """Find all data in the database
    Args:
        data (dict, optional): Filter the data to find. Defaults to {}.
        table (str, optional): The table to find in. Defaults to "".
    Returns:
        list[dict[int, int, dict]]: The data found
    """
    print("Function not implemented yet")
