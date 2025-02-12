# 🐍 Python Serialization Project 💾

## 📝 Description

This project explores the fundamental concepts of **marshaling** and **serialization** in computer science. You'll learn how to efficiently store and transmit data by transforming it into formats suitable for various applications. This project enhances your understanding and practical skills in handling data in real-world scenarios.

## 🎯 Learning Objectives

*   Understand the concepts of marshaling and serialization.
*   Implement serialization techniques in Python.
*   Apply serialized data in web applications, databases, and network communications.
*   Evaluate the performance implications of different serialization formats (JSON, XML, pickle).

## 🛠️ Tasks

### 0. 📦 Basic Serialization (JSON)

*   **File**: `task_00_basic_serialization.py`
*   **Description**: Create a module to serialize a Python dictionary to a JSON file and deserialize the JSON file back into a Python dictionary.

    ```
    def serialize_and_save_to_file(data, filename):
        """Serializes a Python dictionary to a JSON file."""
        pass

    def load_and_deserialize(filename):
        """Deserializes a JSON file to a Python dictionary."""
        pass
    ```

    *   `serialize_and_save_to_file(data, filename)`: Serializes the `data` dictionary to a JSON file named `filename`. Overwrites the file if it exists.
    *   `load_and_deserialize(filename)`: Loads and deserializes data from the JSON file `filename`, returning a Python dictionary.

    **Example Usage:**

    ```
    from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

    # Sample data
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize and save to file
    serialize_and_save_to_file(data_to_serialize, 'data.json')
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize
    deserialized_data = load_and_deserialize('data.json')
    print("Deserialized Data:")
    print(deserialized_data)
    ```

### 1. 🥒 Pickling Custom Classes

*   **File**: `task_01_pickle.py`
*   **Description**: Learn to serialize and deserialize custom Python objects using the `pickle` module.

    1.  **Create a class `CustomObject`**:
        *   Attributes: `name` (string), `age` (integer), `is_student` (boolean).
        *   Method `display()`: Prints object attributes.
        *   Method `serialize(filename)`: Serializes the object to a file using `pickle`.
        *   Class method `deserialize(filename)`: Deserializes an object from a file using `pickle`.

    ```
    class CustomObject:
        def __init__(self, name, age, is_student):
            self.name = name
            self.age = age
            self.is_student = is_student

        def display(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Is Student: {self.is_student}")

        def serialize(self, filename):
            """Serializes the object to a file."""
            pass

        @classmethod
        def deserialize(cls, filename):
            """Deserializes an object from a file."""
            pass
    ```

    **Example Usage:**

    ```
    from task_01_pickle import CustomObject

    # Create an instance
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()
    ```

### 2. 🔄 Converting CSV Data to JSON Format

*   **File**: `task_02_csv.py`
*   **Description**: Convert data from CSV format to JSON format.

    ```
    import csv
    import json

    def convert_csv_to_json(csv_file):
        """Converts a CSV file to a JSON file."""
        pass
    ```

    *   `convert_csv_to_json(csv_file)`: Reads data from `csv_file` and writes it to `data.json` in JSON format.  Returns `True` on success, `False` on failure (e.g., file not found).

    **Example Usage:**

    ```
    from task_02_csv import convert_csv_to_json

    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print(f"Failed to convert {csv_file} to data.json")
    ```

    **Example `data.csv`:**

    ```
    name,age,city
    John,28,New York
    Alice,24,Los Angeles
    Bob,22,Chicago
    Eve,30,San Francisco
    ```

    **Resulting `data.json`:**

    ```
    [
        {"name": "John", "age": "28", "city": "New York"},
        {"name": "Alice", "age": "24", "city": "Los Angeles"},
        {"name": "Bob", "age": "22", "city": "Chicago"},
        {"name": "Eve", "age": "30", "city": "San Francisco"}
    ]
    ```

### 3.  XML Serialization/Deserialization ⚙️

*   **File**: `task_03_xml.py`
*   **Description**: Implement serialization and deserialization using XML.

    ```
    import xml.etree.ElementTree as ET

    def serialize_to_xml(dictionary, filename):
        """Serializes a dictionary to an XML file."""
        pass

    def deserialize_from_xml(filename):
        """Deserializes an XML file to a dictionary."""
        pass
    ```

    *   `serialize_to_xml(dictionary, filename)`: Serializes the input `dictionary` to an XML file named `filename`.
    *   `deserialize_from_xml(filename)`: Reads XML data from `filename` and returns a deserialized Python dictionary.

    **Example Usage:**

    ```
    from task_03_xml import serialize_to_xml, deserialize_from_xml

    def main():
        sample_dict = {
            'name': 'John',
            'age': '28',
            'city': 'New York'
        }

        xml_file = "data.xml"
        serialize_to_xml(sample_dict, xml_file)
        print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(deserialized_data)

    if __name__ == "__main__":
        main()
    ```

    **Example `data.xml`:**

    ```
    <data>
        <name>John</name>
        <age>28</age>
        <city>New York</city>
    </data>
    ```

## 🚀 Setup

1.  Clone the repository:

    ```
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create and activate a virtual environment (optional but recommended):

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install any dependencies (if needed):

    ```
    pip install any_required_packages
    ```

## ⚙️ Repository Structure
```bash
holbertonschool-higher_level_programming/
└── python-serialization/
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
├── task_03_xml.py
└── README.md
```

## 📚 Resources

*   [Real Python Serialization](https://realpython.com/python-serialization/)
*   [Real Python: Working With JSON Data in Python](https://realpython.com/working-with-json-data-in-python/)
*   [Python’s pickle documentation](https://docs.python.org/3/library/pickle.html)
*   [Corey Schafer on Pickle](https://www.youtube.com/watch?v=2Tw39k60lag)
*   [CSV to JSON in Python](https://www.geeksforgeeks.org/convert-csv-to-json-using-python/)
*   [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)

## 📜 Authors
(Saynez667)[https://github.com/Saynez667]
