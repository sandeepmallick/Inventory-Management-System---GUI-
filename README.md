# Inventory Management System  (GUI using Tkinter and MySQL and Export To Excel)

# Overview
This is a **GUI-based Inventory Management System** built using **Python, Tkinter, and MySQL**. The application provides an interactive interface to manage inventory records, making it easy to add, update, delete, select, and export inventory data stored in a MySQL database.

# Features
- **Graphical User Interface (GUI)** built using Tkinter.
- **Inventory record management**, including Item ID, Name, Price, Quantity, and Category.
- **Automatic unique Item ID generation** using a combination of numbers and letters.
- **Database connectivity** with MySQL to store and retrieve data.
- **Edit and delete existing records** with ease.
- **Export inventory data** to a CSV file for reporting.
- **User-friendly buttons and interface** for smooth interaction.

# Prerequisites
Before running this project, ensure the following are installed:
- Python (version 3.x recommended)
- MySQL Database
- Required Python libraries: `pymysql`, `tkinter`, `random`, `csv`

You can install the required libraries using:
```sh
pip install pymysql
```

# How to Run the Project
1. **Start MySQL Database** and create an `inventory` database.
2. **Run the Python script** to launch the GUI.
3. The **application window** will open, allowing you to manage inventory records through the interface.


# Step-by-Step How Its Work

# 1. GUI Window Setup
The application uses Tkinter to create a simple, user-friendly window. The main window is configured with a title and size.

# 2. Connecting to MySQL
A connection function is defined to establish a link between the application and the MySQL database, allowing data storage and retrieval.

# 3. Generating Unique Item IDs
The system automatically generates a random Item ID using a combination of numbers and an uppercase letter.

# 4. Managing Inventory Data
The GUI provides the following functionalities:
- **Adding new inventory items** to the database.
- **Updating existing records** with new values.
- **Deleting unwanted inventory entries** from the database.
- **Selecting and displaying specific records** in the input fields for modification.

# 5. Exporting Data
Users can export the inventory data into a CSV file, making it easy to generate reports or backup records.

# 6. User Interface Elements
- **Buttons** for saving, updating, deleting, selecting, and exporting data.
- **Input fields** for entering and displaying inventory details.
- **Dropdown menu** to choose categories.
- **Table (Treeview)** to display inventory records in a structured format.

# 7. Running the Application
Once all elements are set up, the application runs using Tkinter’s main event loop, making it interactive and responsive.

# Conclusion
This **Inventory Management System** is a simple yet powerful tool for tracking inventory efficiently. The GUI makes it easy for users to interact with the database, while MySQL ensures data persistence. The ability to export data further enhances its usability for reporting and analysis.

This project can be expanded with additional features such as **barcode scanning, user authentication, or advanced filtering options** to make it even more robust. 🚀

