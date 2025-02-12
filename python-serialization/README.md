# Marshaling and Serialization in Python, C, and OOP 🧑‍💻

## Introduction 🚀
Welcome to our exploration of **marshaling** and **serialization**, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will dive deep into how data can be transformed and communicated between different parts of a system, or even across different systems. By the end, you'll gain practical experience with data handling in **Python**, **C**, and **Object-Oriented Programming (OOP)**.

## What is Marshaling? 📦
**Marshaling** is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is essential in distributed systems and remote procedure calls (RPCs), where objects need to be represented in a standardized way across different computing platforms.

## What is Serialization? 🔄
**Serialization** involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal of serialization is to preserve the state of an object so it can be recreated in an identical state elsewhere. This is especially important in **data persistence**, **distributed computing**, and **data sharing** between different software components.

### Learning Objectives 🎯
By working on this project, you'll:
- Understand the differences and similarities between marshaling and serialization.
- Implement serialization in Python with various data formats like JSON, XML, and binary.
- Gain hands-on experience with object serialization (pickling) in Python.
- Convert data from one format to another (e.g., CSV to JSON).
- Explore performance implications of different serialization formats.

## Resources 📚
- [Real Python - Serialization](https://realpython.com/python-serialization/)
- [Working With JSON Data in Python](https://realpython.com/python-json/)
- [Python's `pickle` Documentation](https://docs.python.org/3/library/pickle.html)
- [CSV to JSON in Python](https://realpython.com/python-csv/)
- [XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Socket Programming Guide](https://realpython.com/python-sockets/)

---

## Tasks 🛠️

### Task 0: Basic Serialization 📄
Create a basic serialization module that can serialize a Python dictionary to a JSON file and deserialize it back into a dictionary.

#### Instructions:
1. Write a Python module named `task_00_basic_serialization.py` with the following functions:
   - `serialize_and_save_to_file(data, filename)`
   - `load_and_deserialize(filename)`

2. **serialize_and_save_to_file** will take two parameters: `data` (Python dictionary) and `filename` (the JSON file to save the data).
3. **load_and_deserialize** will load and deserialize the data from the provided JSON file back into a Python dictionary.

#### Example:
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file
data_to_serialize = {"name": "John", "age": 30, "city": "New York"}
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")
deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:", deserialized_data)
text

---

### Task 1: Pickling Custom Classes 🥒
Learn how to serialize and deserialize custom Python objects using the `pickle` module.

#### Instructions:
1. Create a custom class `CustomObject` with attributes `name`, `age`, and `is_student`.
2. Implement the methods:
   - `serialize(self, filename)` - Serialize the instance to the provided file using `pickle`.
   - `@classmethod deserialize(cls, filename)` - Deserialize the object from the file.

#### Example:
```python
#!/usr/bin/env python3
from task_01_pickle import CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
print("Deserialized Object:", new_obj.display())
```

---

### Task 2: Converting CSV Data to JSON 📊 → 📄
Convert CSV data into JSON format using serialization techniques.

#### Instructions:
1. Import `csv` and `json` modules.
2. Write the function `convert_csv_to_json(csv_file)` that reads a CSV file and writes the JSON data to `data.json`.

#### Example:
```python
#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json
csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
```

---

### Task 3: Serializing and Deserializing with XML 📝
Explore serialization and deserialization using XML as an alternative format to JSON.

#### Instructions:
1. Use `xml.etree.ElementTree` to implement the following:
   - `serialize_to_xml(dictionary, filename)` - Serialize a Python dictionary into an XML file.
   - `deserialize_from_xml(filename)` - Deserialize XML data back into a Python dictionary.

#### Example:
```python
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml
sample_dict = {"name": "John", "age": 28, "city": "New York"}
xml_file = "data.xml"
serialize_to_xml(sample_dict, xml_file)
print(f"Dictionary serialized to {xml_file}")
deserialized_data = deserialize_from_xml(xml_file)
print("Deserialized Data:", deserialized_data)
```

---

## Repo Structure 📁
```bash
holbertonschool-higher_level_programming/
├── python-serialization/
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
└── task_03_xml.py
```
## Authors
[Saynez667](https://github.com/Saynez667)