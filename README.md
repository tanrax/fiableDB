
<p align="center">
    <img src="assets/logo.png" alt="fiableDB logo">
</p>

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

```python
pip3 install --user fiable_db
```

## Docs

All documentation can be read as a sequential tutorial.

### Step1: Start

To load the database you must import `fiable_db` and start it.

```python
import fiable_db

fiable_db.start()
```

It will create a file named `fiable_db.json` in the current directory. If you want to change the name of the file, you can do it by passing the name as a parameter.

```python
fiable_db.start(file="my_db.json")
```

If the file already exists, it will be loaded. Nothing is deleted here!

### Step 2: Agregation

Only one:

```python
fiable_db.add({"name": "Miguel", "age": 41, "height": 189})
# {"id": 1, "rev": 1, "data": {"name": "Miguel", "age": 41, "height": 189}}
```

Various:

```python
fiable_db.add(
    [
        {"name": "Noelia", "age": 34, "height": 165},
        {"name": "Juan", "age": 41, "height": 187},
        {"name": "Valentina", "age": 12, "height": 142},
    ]
)
# [
#     {"id": 2, "rev": 1, "data": {{"name": "Noelia", "age": 34, "height": 165}},
#     {"id": 3, "rev": 1, "data": {{"name": "Juan", "age": 41, "height": 187}},
#     {"id": 4, "rev": 1, "data": {{"name": "Valentina", "age": 12, "height": 142}},
# ]
```

### Step 3: Update

Update a key:

```python
fiable_db.update(4, {"age": 21})
# {"id": 4, "rev": 2, "data": {{"name": "Valentina", "age": 21, "height": 172}}
```

If the key does not exist, it will be added:

```python
fiable_db.update(4, {"is_active": True})
# {"id": 4, "rev": 3, "data": {{"name": "Valentina", "age": 21, "height": 172, "is_active": True}}
```

To delete a key you only have to give it a value `None`.

```python
fiable_db.update(4, {"height": None})
# {"id": 4, "rev": 4, "data": {{"name": "Valentina", "age": 21, "is_active": True}}
```

To overwrite the dictionary, use the `force=True`:

```python
fiable_db.update(4, {"name": "Javier", "email": "foo@example.com"}, force=True)
# {"id": 4, "rev": 5, "data": {{"name": "Javier", "email": "foo@example.com"}}
```

### Step 4: Delete

You can be specific by using the `id`.

```python
fiable_db.delete(id=4)
# {"id": 4, "rev": 6, "data": None}
```

And you can delete by performing a search for their values:

```python
fiable_db.delete(data={"name": "Javier"})
# {"id": 4, "rev": 6, "data": None}
```

### Step 5: Find one

Search by id.

```python
fiable_db.find_one(id=2)
# {"id": 2, "rev": 1, "data": {{"name": "Noelia", "age": 34, "height": 165}}
```

Search by value. It will give you the first match.

```python
fiable_db.find_one(data={"name": "Noelia"})
# {"id": 2, "rev": 1, "data": {{"name": "Noelia", "age": 34, "height": 165}}
```

Search by several values.

```python
fiable_db.find_one(data={"name": "Noelia", "age": 34})
# {"id": 2, "rev": 1, "data": {{"name": "Noelia", "age": 34, "height": 165}}
```

If there are no results it will return a None.

```python
fiable_db.find_one(data={"name": "Noelia", "is_active": False})
# None
```

### Step 6: Find all


```python
fiable_db.find_all(data={"age": 41})
# [
#      {"id": 1, "rev": 1, "data": {{"name": "Miguel", "age": 41, "height": 189}},
#      {"id": 3, "rev": 1, "data": {{"name": "Juan", "age": 41, "height": 187}},
# ]
```

If no results are found it will return an empty list.

```python
fiable_db.find_all(data={"age": 88})
# []
```

### Step 7: See previous revisions

At any time you can view the previous information of any row using the `rev` parameter.

Example: Previous version to be deleted.

```python
fiable_db.find_one(id=4, rev=3)
# {"id": 4, "rev": 3, "data": {{"name": "Valentina", "age": 21, "height": 172, "is_active": True}}
```

For convenience, you can use negative numbers. `-1` will be the previous state, `-2` is 2 states back, etc.

```python
fiable_db.find_one(id=4, rev=-1)
# {"id": 4, "rev": 3, "data": {{"name": "Valentina", "age": 21, "height": 172, "is_active": True}}

fiable_db.find_one(id=4, rev=-2)
# {"id": 4, "rev": 2, "data": {{"name": "Valentina", "age": 21, "height": 172}}
```

### Step 8: Working with tables or collections.

You can create as many tables as you want. The default table is called `default`. If you want to work in another table, just use the `table` attribute in any of the above functions.

```python
fiable_db.add({"name": "Luciano", "age": 54, "height": 165}, table="users")
# {"id": 1, "rev": 1, "data": {"name": "Luciano", "age": 54, "height": 165}}

fiable_db.find_one(id=1, table="users") # "users" table
# {"id": 1, "rev": 1, "data": {"name": "Luciano", "age": 54, "height": 165}}

fiable_db.find_one(id=1) # Default table
# {"id": 1, "rev": 1, "data": {"name": "Miguel", "age": 41, "height": 189}}
```

---

Thanks to the power of 🐍 Python 🐍
