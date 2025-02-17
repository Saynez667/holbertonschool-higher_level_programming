# RESTful API Project 🌐

## Introduction 🚀

Welcome to the RESTful API project! In today's software development landscape, efficient data communication between systems is crucial. This project explores RESTful APIs, the backbone of modern web services. REST (Representational State Transfer) ensures scalable, stateless, and cacheable communication, facilitating seamless integration across diverse applications.

## Learning Objectives 🎯

*   **HTTP/HTTPS Basics**: 🔑 Understand web communication protocols and secure vs. non-secure data transfer.
*   **API Consumption with Command Line**: 💻 Interact with APIs using command-line tools like `curl`.
*   **API Consumption with Python**: 🐍 Enhance data fetching skills using Python libraries.
*   **API Development with `http.server`**: 🛠️ Build basic APIs using Python's built-in modules.
*   **API Development with Flask**: 🧪 Develop more advanced APIs using the Flask framework.
*   **API Security & Authentication**: 🛡️ Secure APIs to protect data and ensure authorized access.
*   **API Standards & Documentation with OpenAPI**: 📚 Document APIs for usability and maintainability.

## Importance 💡

RESTful APIs are vital for integrating systems in our interconnected world. They act as intermediaries, translating requests, fetching data, and triggering actions. APIs are everywhere, from social media sharing data to industrial systems automating processes.

This project equips you with the skills to consume, develop, secure, and document APIs, blending technical understanding with design considerations for efficient digital communication.

## REST API Conceptual Diagram 🗺️
```sh
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```

**Components:**

*   **Client**: 📱 The service requester (e.g., web browser or application).
*   **Web Server**: ⚙️ Handles incoming requests and routes them to the API server.
*   **API Server**: 🧠 Processes requests and determines necessary actions.
*   **Database**: 🗄️ Stores data fetched or modified by the API.

**Flow:**

1.  Client sends an HTTP/HTTPS request to the Web Server.
2.  Web Server forwards the request to the API Server.
3.  API Server processes the request and interacts with the database if needed.
4.  API Server returns the processed response to the Web Server.
5.  Web Server sends the final HTTP/HTTPS response to the client.

## Tasks 📝

### 0. Basics of HTTP/HTTPS

*   **Objective**: Understand the differences between HTTP and HTTPS, HTTP structure, methods, and status codes.
*   **Instructions**:
    1.  Read about HTTP and HTTPS.
    2.  Note the main differences, especially regarding security.
    3.  (Optional) Use Wireshark to observe HTTP/HTTPS traffic.
    4.  Inspect website network requests in your browser's developer tools.
    5.  List and explain common HTTP methods and status codes with use cases.
*   **Expected Output**:
    *   Summary of HTTP vs. HTTPS differences.
    *   Outline of HTTP request/response structure.
    *   Lists of HTTP methods and status codes with descriptions and use cases.

### 1. Consume data from an API using command line tools (curl)

*   **Objective**: Install and use `curl` to make API requests.
*   **Instructions**:
    1.  Install `curl`.
    2.  Verify installation with `curl --version`.
    3.  Fetch a webpage with `curl http://example.com`.
    4.  Retrieve posts from JSONPlaceholder API: `curl https://jsonplaceholder.typicode.com/posts`
    5.  Fetch headers only: `curl -I https://jsonplaceholder.typicode.com/posts`
    6.  Make a POST request: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`
*   **Expected Output**:
    *   `curl --version` output.
    *   JSON output of posts from JSONPlaceholder.
    *   Headers from the API request.
    *   Response from the POST request.

### 2. Consuming and processing data from an API using Python

*   **Objective**: Use the `requests` library to interact with APIs and process data.
*   **Instructions**:
    1.  Install `requests`: `pip install requests`.
    2.  Write a Python script to fetch posts from JSONPlaceholder using `requests.get()`.
    3.  Create function `fetch_and_print_posts()` to print status code (200) and titles.
    4.  Create function `fetch_and_save_posts()` to save data to `posts.csv`.
*   **Expected Output**:
    *   Status code 200.
    *   Printed titles of posts.
    *   `posts.csv` file with post data.
*   **Repo**:
    *   GitHub repository: `holbertonschool-higher_level_programming`
    *   Directory: `restful-api`
    *   File: `task_02_requests.py`

### 3. Develop a simple API using Python with the `http.server` module

*   **Objective**: Set up a basic web server using `http.server`.
*   **Instructions**:
    1.  Create a subclass of `http.server.BaseHTTPRequestHandler`.
    2.  Implement `do_GET` method to handle GET requests.
    3.  Start the server on port 8000.
    4.  Serve JSON data at the `/data` endpoint.
    5.  Add a `/status` endpoint.
    6.  Implement error handling for undefined endpoints (404).
*   **Expected Output**:
    *   "Hello, this is a simple API!" on visiting `http://localhost:8000`.
    *   JSON response at `/data`.
    *   "OK" response at `/status`.
    *   404 error for undefined endpoints.

## Authors
[Saynez667](https://github.com/Saynez667)
