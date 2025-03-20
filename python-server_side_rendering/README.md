# ⚙️ Server-Side Rendering (SSR) Project with Flask and Jinja

## 📝 Description

This project explores server-side rendering (SSR) with Python, Flask, and Jinja. It demonstrates how to generate dynamic web pages on the server to improve the efficiency, SEO, and maintainability of web applications.  With SSR, web pages are generated on the server and sent to the client as fully formed HTML, as opposed to client-side rendering where the browser builds the web page using JavaScript and dynamic data.

## 🎯 Learning Objectives

*   Understand the concepts of server-side rendering and how it differs from client-side rendering.
*   Learn the benefits of using server-side rendering in web development.
*   Implement SSR in Python using the Flask framework.
*   Utilize the Jinja templating engine to dynamically generate HTML pages.
*   Read and display data from various sources, including JSON, CSV, and SQLite databases.
*   Handle dynamic content and user inputs in web applications.

## 📚 Resources

*   [MDN Web Docs on Server-Side Web Development](MDN Server-Side Web Development)
*   [Client-side vs. Server-side vs. Pre-rendering for Web Apps: Templating Engines in Web Development](https://www.alura.com.br/artigos/front-end-client-side-server-side-rendering)
*   [Flask Documentation](Flask Official Documentation)
*   [Python JSON Documentation](Python JSON Documentation)
*   [Python CSV Documentation](Python CSV Documentation)
*   [Python SQLite Documentation](Python SQLite Documentation)
*   [Jinja2 Documentation](Jinja2 Documentation)

## ✅ Tasks

### 0. Creating a Simple Templating Program (Mandatory)

*   **Objective:** Use string templating in Python to generate personalized invitation files from a template with placeholders and a list of objects.  Each output file should be named sequentially, starting from 1. Implement specific error handling for various edge cases.
*   **Instructions:**
    *   Use the provided `template.txt` file with placeholders for name, event_title, event_date, and event_location.
    *   Use the provided list of objects as your data source.
    *   Define a function named `generate_invitations` that takes two parameters: `template` and `attendees`.
    *   Check Input Types:  Verify that `template` is a string and `attendees` is a list of dictionaries.  If not, log an error and terminate the function.
    *   Handle Empty Inputs: Check if the template and the `attendees` list are empty and log an error if they are.
    *   Process Each Attendee: Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.  If a value is missing, replace it with “N/A”.
    *   Generate Output Files: Write the processed template to output files named `output_X.txt`, where X is the index of the attendee starting from 1.
*   **Specific Error Handling Behaviors:**
    *   **Empty Template:** Log the error message: `Template is empty, no output files generated.` and terminate without creating any files.
    *   **Empty List of Objects:** Log the message: `No data provided, no output files generated.` and terminate without creating any files.
    *   **Missing Data in Object:** Replace the missing data with the text `N/A` in the output file. For example, if `event_date` is missing, it should appear as `event_date: N/A` in the output.
    *   **Invalid Input Types:** Log an error message indicating the type of invalid input and terminate the function.
*   **Files:** `template.txt`, data for testing (example provided in the description), and `task_00_intro.py`

### 1. Creating a Basic HTML Template in Flask (Mandatory)

*   **Objective:** Build a basic Flask application that serves a web page using a Jinja template. Create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask. Additionally, learn to create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.
*   **Instructions:**
    *   Ensure Python is installed. Install Flask using `pip install Flask`.
    *   In your project directory, create a Python file named `task_01_jinja.py`. Write a basic Flask application with a route that renders an HTML template.
    *   In a `templates` folder within your project directory, create an HTML file named `index.html`. Design a simple HTML page with a heading (`<h1>`), a paragraph (`<p>`), and an unordered list (`<ul>` with `<li>` items).
    *   Use Flask’s `render_template` function to render the HTML template when the corresponding route is accessed.
    *   In the `templates` folder, create two new HTML files: `header.html` and `footer.html`. Design simple but distinct layouts for the header and footer, and include navigation links (Home, About, Contact) to all pages into `header.html`.
    *   Create additional HTML pages `about.html` and `contact.html`. In each of these pages (`index.html`, `about.html` and `contact.html`), include the header and footer templates without duplicating their code. Add specific tags for each page: In `about.html`, include an `<h1>` tag with the text "About Us" and a paragraph (`<p>`) with content describing the page. In `contact.html`, include an `<h1>` tag with the text "Contact Us" and a paragraph (`<p>`) with content for the contact page.
    *   Add new routes in your Flask application corresponding to the additional pages you created.
*   **Files:** `task_01_jinja.py`, `templates/index.html`, `templates/header.html`, `templates/footer.html`, `templates/about.html`, `templates/contact.html`

### 2. Creating a Dynamic Template with Loops and Conditions in Flask (Mandatory)

*   **Objective:** Enhance the Flask application by integrating dynamic content into HTML templates using Jinja’s loop and conditional constructs.  Read a list of items from a JSON file and display them dynamically on a web page.
*   **Instructions:**
    *   Continue using the Flask application you created in the previous exercises. Ensure you have a basic understanding of Jinja’s templating syntax.
    *   In your `templates` folder, create a new HTML template named `items.html` with “Items List” for the title. This template should include a loop to iterate over a list of items and display each item. Items must be displayed as an unordered list. Add a conditional statement to display a message “No items found” if the list is empty.
    *   In your project directory, create a file named `items.json`. Populate `items.json` with a list of items. Experiment with different lists, including an empty list, to see how your template responds.
    *   Create a new route `/items` in your Flask application to render the `items.html` template with the list of items. Use Python’s `json` module to read the data from `items.json`. Pass the list of items to the template for rendering.
*   **Data for Testing:**
    ```
    {
        "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
    }
    ```
*   **Files:** `templates/items.html`, `items.json`, `task_02_logic.py`

### 3. Displaying Data from JSON or CSV Files in Flask (Mandatory)

*   **Objective:** Build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV. Create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL. Add functionality to your Flask application to filter product data based on an optional `id` query parameter. Additionally, handle edge cases such as invalid `source` parameter values or when the specified `id` is not found in the data.
*   **Instructions:**
    *   Create a JSON file (`products.json`) containing a list of products, each with an `id`, `name`, `category`, and `price`.
    *   Create a CSV file (`products.csv`) with similar data, using columns for `id`, `name`, `category`, and `price`.
    *   In your `templates` folder, create an HTML template `product_display.html` for displaying the product data. Design the template to display the data in a table format with headings for Name, Category, and Price.
    *   In `task_03_files.py`, create a route in your Flask application that accepts a `source` query parameter (values `json` or `csv`) and an optional `id`. Depending on the `source` parameter, read and parse data from the corresponding file. Implement logic to filter data by the specified `id` if provided. If `id` is not provided, display all products.
    *   Write functions to read and parse data from both JSON and CSV files. Ensure the data is converted into a format that can be easily displayed by the template.
    *   If `source` is neither `json` nor `csv`, return a `Wrong source` error message in the template. If `id` is provided but not found in the file, display a `Product not found` error message in the template. Modify the `product_display.html` template to handle and display error messages if necessary.
*   **Files:** `products.json`, `products.csv`, `templates/product_display.html`, `task_03_files.py`

## 🛠️ Installation

1.  Clone the repository: `git clone [Repository URL]`
2.  Navigate to the project directory: `cd python-server_side_rendering`
3.  Install dependencies: `pip install Flask Jinja2`

## ⚙️ Usage

1.  Run the Flask application: `python task_XX_filename.py` (replace `task_XX_filename.py` with the appropriate task file)
2.  Open a browser and access the URL indicated (usually `http://127.0.0.1:5000/`).

## Author
[Saynez667](https://github.com/Saynez667)

