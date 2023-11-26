# **Apache Log Analyzer**
# Overview
This is a simple GUI Desktop application built using Python and SQLite3. The Graphical User Interface is designed using the customtkinter Library. The application enables users to enter an Apache server access log file and view the structured log in a tabular form, along with data visualization.



# Features

### User Authentication:

- Users can log in with their username and password.
- If they forget their password, they can recover it by providing their mobile number and email.

### User Registration:

- Users can create new accounts by providing a username, password, mobile number, and email.
- Registration data is stored in an SQLite database.

### Data Management:

- Users can add, update, and delete temperature data for specific days.
- Data is stored in a database for analysis and prediction.

### Data Visualization:

- Users can view temperature data on a line graph using Matplotlib.
- Graphs help users visualize temperature trends.

# Project Structure

- **database.py:** Contains functions for database management, including user registration, data addition, and more.
- **plot.py:** Visualizes data using matplotlib.
- **UI.py** The main script for the GUI application.

# Installation
- Make sure you have Python 3.x installed on your system.
- Install required dependencies using: 
    `pip install matplotlib customtkinter captcha`
- Clone the project using:
    `git clone https://github.com/human-V-oid/log-analyzer.git`

# Usage
- Change directory to project dir:
    `cd log-analyzer`
- Run UI.py to start the application:
    `python UI.py`

# Developers words
- This is not the final version of this software, future versions may include modifications or feature updates.

# Contribution
#### Special thanks to *Priyanshu-Batham* for the origin repo.
- Anyone can contribute to this repository by submitting a pull request.