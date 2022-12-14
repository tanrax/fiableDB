from typing import Dict, Tuple, Union, Sequence, TypedDict
from functools import reduce
import json
from os import path
from copy import deepcopy

# Variables
FILE = "fiabledb.json"
database = []

# Type aliases


class TypeData(TypedDict):
    id: int
    rev: int
    data: dict


Type_Data_List = Tuple[TypeData]
Type_Add_Data = Union[Dict, Sequence[Dict]]
Type_Add_Return = Union[Tuple[int, int, Dict], Tuple[Tuple[int, int, Dict]], None]
Type_Update_Return = Union[Tuple[Tuple[int, int, Dict]], None]
Type_Delete_Return = Union[Tuple[Tuple[int, int, Dict]], None]
Type_Find_One_Return = TypeData
Type_Find_All_Return = Tuple[Type_Find_One_Return]

# Functions


def get_next_id(table: str = "default") -> int:
    """Get the next id for the table"""
    global database

    # Get the last id for the table
    def get_id(current_id, row: TypeData) -> int:
        if current_id == None and table == row["table"]:
            return row["id"]
        else:
            return current_id

    last_id = reduce(get_id, database[::-1], None)
    # Return the next id, or 1 if there is no last id
    return last_id + 1 if last_id else 1


def start(file_name: str = "") -> str:
    """Start the database
    Args:
        file (str, optional): The file to use. Defaults to FILE.
    Returns:
        str: The file used
    """
    global FILE
    global database
    my_file_name = file_name if file_name != "" else FILE
    if path.exists(my_file_name):
        # Load the database
        load(my_file_name)
    else:
        # Create the database
        database = []
        save(my_file_name)
    return my_file_name


def save(file_name: str = "") -> bool:
    """Save the database
    Args:
        file_name (str, optional): The file to save to. Defaults to "".
        data (list[str, list[int, int, dict]], optional): The data to save. Defaults to {}.
    Returns:
        bool: True if the data was saved, False otherwise
    """
    global FILE
    global database
    my_file_name = file_name if file_name != "" else FILE
    with open(my_file_name, "w") as f:
        json.dump(database, f)
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


def get_pos_by_id(id: int, table: str = "") -> int:
    """Get the position of the data by id
    Args:
        id (int): The id of the data
        table (str, optional): The table to search in. Defaults to "".
    Returns:
        int: The position of the data
    """
    global database

    def get_key(
        current_key: Union[TypeData, None], key_and_row: TypeData
    ) -> Union[int, None]:
        """Function to get the key of the data"""
        if (
            current_key is None
            and key_and_row[1]["id"] == id
            and key_and_row[1]["table"] == table
        ):
            return key_and_row[0]
        return current_key

    return reduce(get_key, list(enumerate(database))[::-1], None)


def add(new_data: Type_Add_Data, table: str = "default") -> Type_Add_Return:
    """Add data to the database
    Args:
        new_data (dict|list): The data to add
        table (str, optional): The table to add to. Defaults to "".
    Returns:
        dict[int, int, dict]|list[dict[int, int, dict]]: The data added
    """
    global database
    if isinstance(new_data, dict):
        new_row = {"id": get_next_id(table), "rev": 1, "table": table, "data": new_data}
        database.append(new_row)
        return new_row
    elif isinstance(new_data, list):
        for row in new_data:
            new_row = {"id": get_next_id(table), "rev": 1, "table": table, "data": row}
            database.append(new_row)
    else:
        raise TypeError("new_data must be a dict or list")


def update(
    id: int, new_data: dict, table: str = "default", force: bool = False
) -> Type_Update_Return:
    """Update data in the database
    Args:
        id (int): The id of the data to update.
        new_data (dict): The data to update
        table (str, optional): The table to update. Defaults to "".
        force (bool, optional): Force the update. Defaults to False.
    Returns:
        dict[int, int, dict] or None: The data updated
    """
    global database
    # Get the key to update
    key = get_pos_by_id(id, table)
    if key is not None:
        row = deepcopy(database[key])
        my_new_data = deepcopy(new_data)
        if force:
            row["data"] = my_new_data
        else:
            row["data"].update(my_new_data)
        new_rev = row["rev"] + 1
        new_data_to_row = row["data"]
        new_row = {"id": id, "rev": new_rev, "table": table, "data": new_data_to_row}
        database.append(new_row)
        return new_row
    return None


def delete(id: int, table: str = "default") -> Type_Delete_Return:
    """Delete data from the database
    Args:
        id (int): The id of the data to delete
        data (dict): Filter the data to delete
        table (str, optional): The table to delete from. Defaults to "".
    Returns:
        dict[int, int, dict]: The data deleted
    """
    return update(id=id, new_data={}, table=table, force=True)


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
