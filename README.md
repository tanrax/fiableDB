# fiableDB

<p align="center">
    <img src="assets/logo.png" alt="fiableDB logo">
</p>

A simple, reliable, immutable database that stores all data revisions in JSON format.

## Features

- **Information is never lost**. Even if you make updates or deletions, you will be able to recover any information at any time.
- There are **no restrictions on the data structure or columns**, since dictionaries are used without limitations on nesting. Similar to MongoDB Documents.
- All the information is **stored in a JSON file**.
- **Extremely fast** since it has no queue or locking limitations.
- **Minimalistic** to implement and use.

## Why use fiableDB instead of other relational databases?

- **High level of consistency and accuracy of data**, such as a hospital patient's chronology or banking data. It cannot be modified once it has been aggregated.
- They **simplify the process of backing up and restoring data**, because you can always **revert to the original version** of the data if necessary.
- **Very secure**, modifying existing data will be detected and rejected.

## Install

Python version: >=3.8

```python
pip3 install --user fiable_db
```

## Documentation

All documentation can be read as a sequential tutorial.

### Step 1: Start

To load the database you must import `fiable_db` and start it.

```python
import fiable_db

fiable_db.start()
```

It will create a file named `fiabledb.json` in the current directory. If you want to change the name of the file, you can do it by passing the name as a parameter.

```python
fiable_db.start("my_db.json")
# Returns: "my_db.json"
```

If the file already exists, it will be loaded. Nothing is deleted here!

**Error handling:**
```python
try:
    fiable_db.start("my_db.json")
except Exception as e:
    print(f"Database initialization failed: {e}")
    # Creates empty database if file is corrupted
```

### Step 2: Aggregation

**Add a single record:**

```python
result = fiable_db.add({"name": "Miguel", "age": 41, "height": 189})
print(result)
# {"id": 1, "rev": 1, "table": "default", "data": {"name": "Miguel", "age": 41, "height": 189}}
```

**Add multiple records:**

```python
result = fiable_db.add([
    {"name": "Noelia", "age": 34, "height": 165},
    {"name": "Juan", "age": 41, "height": 187},
    {"name": "Valentina", "age": 12, "height": 142},
])
print(result)
# [
#     {"id": 2, "rev": 1, "table": "default", "data": {"name": "Noelia", "age": 34, "height": 165}},
#     {"id": 3, "rev": 1, "table": "default", "data": {"name": "Juan", "age": 41, "height": 187}},
#     {"id": 4, "rev": 1, "table": "default", "data": {"name": "Valentina", "age": 12, "height": 142}},
# ]
```

**Input validation:**
```python
# These will raise errors
try:
    fiable_db.add({})  # ValueError: Cannot add empty dictionary
    fiable_db.add([])  # ValueError: Cannot add empty list
    fiable_db.add("invalid")  # TypeError: new_data must be a dict or list
except (ValueError, TypeError) as e:
    print(f"Invalid input: {e}")
```

### Step 3: Update

**Update a field:**

```python
result = fiable_db.update(4, {"age": 21})
print(result)
# {"id": 4, "rev": 2, "table": "default", "data": {"name": "Valentina", "age": 21, "height": 142}}
```

**Add new fields:**

```python
result = fiable_db.update(4, {"is_active": True})
print(result)
# {"id": 4, "rev": 3, "table": "default", "data": {"name": "Valentina", "age": 21, "height": 142, "is_active": True}}
```

**Delete a field (set to None):**

```python
result = fiable_db.update(4, {"height": None})
print(result)
# {"id": 4, "rev": 4, "table": "default", "data": {"name": "Valentina", "age": 21, "is_active": True}}
```

**Force overwrite (replace entire data):**

```python
result = fiable_db.update(4, {"name": "Javier", "email": "foo@example.com"}, force=True)
print(result)
# {"id": 4, "rev": 5, "table": "default", "data": {"name": "Javier", "email": "foo@example.com"}}
```

**Handle non-existent records:**

```python
result = fiable_db.update(999, {"name": "Ghost"})
print(result)
# None
```

**Input validation:**
```python
try:
    fiable_db.update(-1, {"name": "Invalid"})  # ValueError: id must be a positive integer
    fiable_db.update(1, "not_dict")  # TypeError: new_data must be a dictionary
except (ValueError, TypeError) as e:
    print(f"Invalid input: {e}")
```

### Step 4: Delete

You can delete by using the `id`. This creates a new revision with empty data.

```python
result = fiable_db.delete(id=4)
print(result)
# {"id": 4, "rev": 6, "table": "default", "data": {}}
```

**Input validation:**
```python
try:
    fiable_db.delete(-1)  # ValueError: id must be a positive integer
    fiable_db.delete("invalid")  # TypeError: id must be an integer
except (ValueError, TypeError) as e:
    print(f"Invalid input: {e}")
```

### Step 5: Find One

**Search by ID (gets latest revision):**

```python
result = fiable_db.find_one(id=2)
print(result)
# {"id": 2, "rev": 1, "table": "default", "data": {"name": "Noelia", "age": 34, "height": 165}}
```

**Search by data filter (first match):**

```python
result = fiable_db.find_one(data={"name": "Noelia"})
print(result)
# {"id": 2, "rev": 1, "table": "default", "data": {"name": "Noelia", "age": 34, "height": 165}}
```

**Search by multiple criteria:**

```python
result = fiable_db.find_one(data={"name": "Noelia", "age": 34})
print(result)
# {"id": 2, "rev": 1, "table": "default", "data": {"name": "Noelia", "age": 34, "height": 165}}
```

**No results return None:**

```python
result = fiable_db.find_one(data={"name": "NonExistent"})
print(result)
# None
```

**Input validation:**
```python
try:
    fiable_db.find_one(id="invalid")  # TypeError: id must be an integer
    fiable_db.find_one(data="invalid")  # TypeError: data must be a dictionary
except TypeError as e:
    print(f"Invalid input: {e}")
```

### Step 6: Find All

**Find all records in default table:**

```python
result = fiable_db.find_all()
print(result)
# Returns all active records (latest revisions) sorted by table and id
```

**Filter by data:**

```python
result = fiable_db.find_all(data={"age": 41})
print(result)
# [
#      {"id": 1, "rev": 1, "table": "default", "data": {"name": "Miguel", "age": 41, "height": 189}},
#      {"id": 3, "rev": 1, "table": "default", "data": {"name": "Juan", "age": 41, "height": 187}},
# ]
```

**No results return empty list:**

```python
result = fiable_db.find_all(data={"age": 999})
print(result)
# []
```

**Input validation:**
```python
try:
    fiable_db.find_all(data="invalid")  # TypeError: data must be a dictionary
except TypeError as e:
    print(f"Invalid input: {e}")
```

### Step 7: View Previous Revisions

At any time you can view the previous information of any row using the `rev` parameter.

**Get specific revision:**

```python
result = fiable_db.find_one(id=4, rev=3)
print(result)
# {"id": 4, "rev": 3, "table": "default", "data": {"name": "Valentina", "age": 21, "height": 142, "is_active": True}}
```

**Use negative numbers for relative revisions:**

`-1` will be the previous state, `-2` is 2 states back, etc.

```python
# Get previous revision
result = fiable_db.find_one(id=4, rev=-1)
print(result)
# {"id": 4, "rev": 5, "table": "default", "data": {"name": "Javier", "email": "foo@example.com"}}

# Get 2 revisions back
result = fiable_db.find_one(id=4, rev=-2)
print(result)
# {"id": 4, "rev": 4, "table": "default", "data": {"name": "Valentina", "age": 21, "is_active": True}}
```

**Non-existent revisions return None:**

```python
result = fiable_db.find_one(id=4, rev=999)
print(result)
# None

result = fiable_db.find_one(id=4, rev=-999)
print(result)
# None
```

### Step 8: Working with Tables/Collections

You can create as many tables as you want. The default table is called `default`. Use the `table` parameter in any function to work with different tables.

**Add to specific table:**

```python
result = fiable_db.add({"name": "Luciano", "age": 54, "height": 165}, table="users")
print(result)
# {"id": 1, "rev": 1, "table": "users", "data": {"name": "Luciano", "age": 54, "height": 165}}
```

**Find in specific table:**

```python
# Find in "users" table
result = fiable_db.find_one(id=1, table="users")
print(result)
# {"id": 1, "rev": 1, "table": "users", "data": {"name": "Luciano", "age": 54, "height": 165}}

# Find in "default" table
result = fiable_db.find_one(id=1, table="default")
print(result)
# {"id": 1, "rev": 1, "table": "default", "data": {"name": "Miguel", "age": 41, "height": 189}}
```

**Update in specific table:**

```python
result = fiable_db.update(1, {"age": 10}, table="users")
print(result)
# {"id": 1, "rev": 2, "table": "users", "data": {"name": "Luciano", "age": 10, "height": 165}}
```

**Delete in specific table:**

```python
result = fiable_db.delete(1, table="users")
print(result)
# {"id": 1, "rev": 3, "table": "users", "data": {}}
```

**Find all in specific table:**

```python
result = fiable_db.find_all(table="users")
print(result)
# Returns all records from "users" table
```

**Cross-table search (leave table empty):**

```python
result = fiable_db.find_one(data={"name": "Luciano"}, table="")
print(result)
# Searches across all tables
```

### Step 9: Save Changes

Save the database to the current file.

```python
success = fiable_db.save()
print(success)  # True if saved successfully, False if error occurred
```

**Save to specific file:**

```python
success = fiable_db.save("backup.json")
print(success)  # True if saved successfully
```

### Other Helper Functions

#### Get All Data

Get the complete database (all revisions, all tables).

```python
all_data = fiable_db.get_database()
print(len(all_data))  # Total number of records (including all revisions)
```

#### Load File

Load a file into the database.

```python
try:
    success = fiable_db.load("backup.json")
    print(f"File loaded: {success}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

## Error Handling

fiableDB includes comprehensive error handling:

### Common Exceptions

- `TypeError`: Invalid data types passed to functions
- `ValueError`: Invalid values (negative IDs, empty data)
- `FileNotFoundError`: Database file not found or corrupted
- `json.JSONDecodeError`: Corrupted JSON file

### Best Practices

```python
import fiable_db

try:
    # Initialize database
    fiable_db.start("myapp.json")
    
    # Add data with validation
    if user_data and isinstance(user_data, dict):
        result = fiable_db.add(user_data, table="users")
        
    # Always check for None results
    user = fiable_db.find_one(id=user_id, table="users")
    if user is not None:
        print(f"Found user: {user['data']['name']}")
    else:
        print("User not found")
        
    # Save changes
    if not fiable_db.save():
        print("Warning: Could not save database")
        
except (TypeError, ValueError) as e:
    print(f"Invalid input: {e}")
except FileNotFoundError as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Data Structure

Each record in fiableDB has the following structure:

```python
{
    "id": 1,           # Unique identifier within table
    "rev": 3,          # Revision number (increments with each update)
    "table": "users",  # Table/collection name
    "data": {          # Your actual data
        "name": "John",
        "age": 30
    }
}
```

## Performance Notes

- **IDs are auto-generated** starting from 1 for each table
- **All operations are O(n)** where n is the total number of records
- **Memory usage grows** with each revision (immutable design)
- **File I/O is synchronous** - consider frequency of save() calls
- **Best for small to medium datasets** (< 100k records)

## Implementations in Other Languages

- [Clojure](https://github.com/Toni-zgz/db_inmutable)
- [Haskell](https://github.com/FabianVegaA/SafeDB)

---

Thanks to the power of 🐍 Python 🐍