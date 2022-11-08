Immutable NoSQL database that works on a single plain text file

## Features

- **Information is never lost**. Even if you make updates or deletions, you will be able to recover any information at any time.
- There are **no restrictions on the data structure or columns**, since dictionaries are used without limitations on nesting. Similar to MongoDB Documents.
- All the information is **stored in a JSON file**.
- Extremely fastb since it has no queue or locking limitations.
- **Minimalistic** to implement and use.

## Advantages of using an immutable database

- **High level of consistency and accuracy of data**, such as a hospital patient's chronology or banking data. It cannot be modified once it has been aggregated.
- They **simplify the process of backing up and restoring data**, because you can always **revert to the original version** of the data if necessary.
- **Very secure**, modifying existing data will be detected and rejected.

## Install

```python
pip3 install --user advance-touch
```

## Documentation

All documentation can be read as a sequential tutorial.

### Start

```python
import fiable_db

db = fiable_db.start()
```

### Agregation

Only one:

```python
db.add({"name": "Noelia", "age": 34, "height": 165})
// {"id": 1, "rev": 1, "data": {"name": "Miguel", "age": 54, "height": 155}}
```

Various:

```python
db.add(
    [
        {"name": "Noelia", "age": 34, "height": 165},
        {"name": "Juan", "age": 41, "height": 187},
        {"name": "Valentina", "age": 12, "height": 142},
    ]
)
//  [
//      {"id": 2, "rev": 1, "data": {{"name": "Noelia", "age": 34, "height": 165}},
//      {"id": 3, "rev": 1, "data": {{"name": "Juan", "age": 41, "height": 187}},
//      {"id": 4, "rev": 1, "data": {{"name": "Valentina", "age": 83, "height": 172}},
//  ]
```

### Update

Update a key:

```python
db.update(4, {"age": 21})
// {"id": 4, "rev": 2, "data": {{"name": "Valentina", "age": 21, "height": 172}}
```

Add new key:

```python
db.update(4, {"is_active": True})
// {"id": 4, "rev": 3, "data": {{"name": "Valentina", "age": 21, "height": 172, "is_active": True}}
```

Delete key:

```python
db.update(4, {"height": None})
// {"id": 4, "rev": 4, "data": {{"name": "Valentina", "age": 21, "is_active": True}}
```

Forcing new structure.

```python
db.update(4, {"name": "Javier", "email": "foo@example.com"}, force=True)
// {"id": 4, "rev": 5, "data": {{"name": "Javier", "email": "foo@example.com"}}
```

### Delete

### Find all

### Find one

