from typing import Dict, Tuple, Union, Sequence, TypedDict, List, Optional
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
    table: str
    data: dict


Type_Data_List = List[TypeData]
Type_Add_Data = Union[Dict, Sequence[Dict]]
Type_Add_Return = Union[TypeData, List[TypeData]]
Type_Update_Return = Union[TypeData, None]
Type_Delete_Return = Union[TypeData, None]
Type_Find_One_Return = Union[TypeData, None]
Type_Find_All_Return = List[TypeData]

# Functions


def get_next_id(table: str = "default") -> int:
    """Get the next id for the table"""
    global database

    # Get all IDs for the table and find the maximum
    table_ids = [row["id"] for row in database if row["table"] == table]
    if not table_ids:
        return 1
    return max(table_ids) + 1


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
        try:
            load(my_file_name)
        except Exception as e:
            # If loading fails, create empty database
            database = []
            save(my_file_name)
    else:
        # Create the database
        database = []
        save(my_file_name)
    FILE = my_file_name
    return my_file_name


def save(file_name: str = "") -> bool:
    """Save the database
    Args:
            file_name (str, optional): The file to save to. Defaults to "".
    Returns:
            bool: True if the data was saved, False otherwise
    """
    global FILE
    global database
    my_file_name = file_name if file_name != "" else FILE
    try:
        with open(my_file_name, "w") as f:
            json.dump(database, f, indent=2)
        return True
    except Exception:
        return False


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
        try:
            with open(my_file_name, "r") as f:
                text = f.read()
                if text != "":
                    loaded_data = json.loads(text)
                    # Validate loaded data structure
                    if isinstance(loaded_data, list):
                        database = loaded_data
                    else:
                        database = []
                else:
                    database = []
        except (json.JSONDecodeError, IOError):
            raise FileNotFoundError("File corrupted or cannot be read")
    else:
        raise FileNotFoundError("File not found")
    return is_exists


def get_database() -> Type_Data_List:
    """Get the data
    Returns:
            list[dict]: The data
    """
    global database
    return database


def get_pos_by_id(id: int, table: str = "default") -> Optional[int]:
    """Get the position of the latest revision by id and table
    Args:
            id (int): The id of the data
            table (str, optional): The table to search in. Defaults to "default".
    Returns:
            int: The position of the data
    """
    global database

    # Find the latest revision for this id and table
    latest_pos = None
    latest_rev = 0

    for i, row in enumerate(database):
        if row["id"] == id and row["table"] == table and row["rev"] > latest_rev:
            latest_pos = i
            latest_rev = row["rev"]

    return latest_pos


def add(new_data: Type_Add_Data, table: str = "default") -> Type_Add_Return:
    """Add data to the database
    Args:
            new_data (dict|list): The data to add
            table (str, optional): The table to add to. Defaults to "default".
    Returns:
            dict|list[dict]: The data added
    """
    global database

    # Input validation
    if not isinstance(new_data, (dict, list)):
        raise TypeError("new_data must be a dict or list")

    if isinstance(new_data, dict):
        if not new_data:  # Empty dict validation
            raise ValueError("Cannot add empty dictionary")
        new_row = {
            "id": get_next_id(table),
            "rev": 1,
            "table": table,
            "data": deepcopy(new_data),
        }
        database.append(new_row)
        return new_row
    elif isinstance(new_data, list):
        if not new_data:  # Empty list validation
            raise ValueError("Cannot add empty list")
        added_rows = []
        for row in new_data:
            if not isinstance(row, dict):
                raise TypeError("All items in list must be dictionaries")
            if not row:  # Empty dict in list
                raise ValueError("Cannot add empty dictionary in list")
            new_row = {
                "id": get_next_id(table),
                "rev": 1,
                "table": table,
                "data": deepcopy(row),
            }
            database.append(new_row)
            added_rows.append(new_row)
        return added_rows


def update(
    id: int, new_data: dict, table: str = "default", force: bool = False
) -> Type_Update_Return:
    """Update data in the database
    Args:
            id (int): The id of the data to update.
            new_data (dict): The data to update
            table (str, optional): The table to update. Defaults to "default".
            force (bool, optional): Force the update. Defaults to False.
    Returns:
            dict or None: The data updated
    """
    global database

    # Input validation
    if not isinstance(id, int) or id <= 0:
        raise ValueError("id must be a positive integer")
    if not isinstance(new_data, dict):
        raise TypeError("new_data must be a dictionary")

    # Get the position of the latest revision
    key = get_pos_by_id(id, table)
    if key is not None:
        row = deepcopy(database[key])
        my_new_data = deepcopy(new_data)
        if force:
            row["data"] = my_new_data
        else:
            # Handle None values to delete keys
            for k, v in my_new_data.items():
                if v is None:
                    if k in row["data"]:
                        del row["data"][k]
                else:
                    row["data"][k] = v
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
            table (str, optional): The table to delete from. Defaults to "default".
    Returns:
            dict: The data deleted
    """
    # Input validation
    if not isinstance(id, int) or id <= 0:
        raise ValueError("id must be a positive integer")

    return update(id=id, new_data={}, table=table, force=True)


def get_latest_revision(id: int, table: str = "default") -> Optional[TypeData]:
    """Get the latest revision of a record"""
    global database

    # Filter records by id and table, then get the one with highest rev
    matching_records = [
        row for row in database if row["id"] == id and row["table"] == table
    ]
    if not matching_records:
        return None

    return max(matching_records, key=lambda x: x["rev"])


def get_revision(id: int, rev: int, table: str = "default") -> Optional[TypeData]:
    """Get a specific revision of a record"""
    global database

    if rev < 0:
        # Handle negative revision numbers
        latest = get_latest_revision(id, table)
        if not latest:
            return None
        target_rev = latest["rev"] + rev + 1
        if target_rev <= 0:
            return None
    else:
        target_rev = rev

    # Find the exact revision
    for row in database:
        if row["id"] == id and row["table"] == table and row["rev"] == target_rev:
            return row

    return None


def match_data_filter(record_data: dict, filter_data: dict) -> bool:
    """Check if record_data matches all criteria in filter_data"""
    if not isinstance(filter_data, dict):
        return False

    for key, value in filter_data.items():
        if key not in record_data or record_data[key] != value:
            return False
    return True


def find_one(
    id: int = 0, data: dict = {}, table: str = "default", rev: int = 0
) -> Type_Find_One_Return:
    """Find one data in the database
    Args:
            id (int, optional): The id of the data to find. Defaults to 0.
            data (dict, optional): Filter the data to find. Defaults to {}.
            table (str, optional): The table to find in. Defaults to "default".
            rev (int, optional): The revision of the data to find. Defaults to 0.
    Returns:
            dict or None: The data found
    """
    global database

    # Input validation
    if not isinstance(id, int):
        raise TypeError("id must be an integer")
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    # If searching by id
    if id > 0:
        if rev != 0:
            # Find specific revision
            return get_revision(id, rev, table)
        else:
            # Find latest revision
            return get_latest_revision(id, table)

    # If searching by data filter
    elif data:
        # Get all latest revisions for each id in the specified table
        latest_records = {}
        search_table = table if table else ""

        for row in database:
            if search_table and row["table"] != search_table:
                continue

            key = (row["id"], row["table"])
            if key not in latest_records or row["rev"] > latest_records[key]["rev"]:
                latest_records[key] = row

        # Search through latest records
        for record in latest_records.values():
            if match_data_filter(record["data"], data):
                return record

    return None


def find_all(data: dict = {}, table: str = "default") -> Type_Find_All_Return:
    """Find all data in the database
    Args:
            data (dict, optional): Filter the data to find. Defaults to {}.
            table (str, optional): The table to find in. Defaults to "default".
    Returns:
            list[dict]: The data found
    """
    global database

    # Input validation
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    # Get all latest revisions for each id in the specified table
    latest_records = {}
    search_table = table if table else ""

    for row in database:
        if search_table and row["table"] != search_table:
            continue

        key = (row["id"], row["table"])
        if key not in latest_records or row["rev"] > latest_records[key]["rev"]:
            latest_records[key] = row

    # Filter records based on data criteria
    results = []
    for record in latest_records.values():
        if not data or match_data_filter(record["data"], data):
            results.append(record)

    # Sort by id for consistent ordering
    results.sort(key=lambda x: (x["table"], x["id"]))
    return results
