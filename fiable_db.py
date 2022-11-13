FILE = "fiabledb.json"
data = {}


def start(filename: str = "") -> str:
    """Start the database
    Args:
        file (str, optional): The file to use. Defaults to FILE.
    Returns:
        str: The file used
    """
    file_name = filename if filename else FILE
    print("Function not implemented yet")
    return file_name


def save(filename: str = "", data: list[str, list[int, int, dict]] = {}) -> bool:
    """Save the database
    Args:
        filename (str, optional): The file to save to. Defaults to "".
        data (list[str, list[int, int, dict]], optional): The data to save. Defaults to {}.
    Returns:
        bool: True if the data was saved, False otherwise
    """
    print("Function not implemented yet")


def load(filename: str = "") -> list[str, list[int, int, dict]]:
    """Load the database
    Args:
        filename (str, optional): The file to load from. Defaults to "".
    Returns:
        list[str, list[int, int, dict]]: The data loaded
    """
    print("Function not implemented yet")


def add(
    new_data: dict | list, table: str = ""
) -> dict[int, int, dict] | list[dict[int, int, dict]]:
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
    new_data: dict | list, table: str = "", force: bool = False
) -> dict[int, int, dict]:
    """Update data in the database
    Args:
        new_data (dict|list): The data to update
        table (str, optional): The table to update. Defaults to "".
        force (bool, optional): Force the update. Defaults to False.
    Returns:
        dict[int, int, dict]: The data updated
    """
    print("Function not implemented yet")


def delete(id: int, data: dict, table: str = "") -> dict[int, int, dict]:
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
) -> dict[int, int, dict]:
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


def find_all(data: dict = {}, table: str = "") -> list[dict[int, int, dict]]:
    """Find all data in the database
    Args:
        data (dict, optional): Filter the data to find. Defaults to {}.
        table (str, optional): The table to find in. Defaults to "".
    Returns:
        list[dict[int, int, dict]]: The data found
    """
    print("Function not implemented yet")
