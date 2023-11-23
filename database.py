import sqlite3
import re
from datetime import datetime

# --------------------------------------------------------------->>>>>>>>>>>
def createTable():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS userInfo (
        id INTEGER PRIMARY KEY,
        email TEXT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def createAccount(username, password, email):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    insert_query = '''
    INSERT INTO userInfo ( username, password, email)
    VALUES (?, ?, ?, ?)
    '''
    try:
        cursor.execute(insert_query, (username, password, email))
        conn.commit()
    except sqlite3.Error as e:
        print("Error:",e)

    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def showUserData():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    fetch_query = '''
    SELECT * FROM userInfo;
    '''
    try:
        cursor.execute(fetch_query)
        data = cursor.fetchall()
        print(data)
    except:
        print("Couldn't Fetch Results")
        
    conn.commit()
    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def isUserPresent(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    login_query = '''
    SELECT * FROM userInfo 
    WHERE username = ? AND password = ?
    '''
    cursor.execute(login_query,(username, password))
    data = cursor.fetchall()

    conn.commit()
    conn.close()

    return True if data else False
# --------------------------------------------------------------->>>>>>>>>>>

def isCredentialsCorrect(username, email):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    credential_query = '''
    SELECT * FROM userInfo 
    WHERE username = ? AND email = ?
    '''
    cursor.execute(credential_query,(username, email))
    data = cursor.fetchall()

    conn.commit()
    conn.close()

    return True if data else False
# --------------------------------------------------------------->>>>>>>>>>>

def changePassword(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    change_query = '''
    UPDATE userInfo 
    SET password = ? 
    WHERE username = ?
    '''
    try:
        cursor.execute(change_query,(password, username))
        print(cursor.rowcount)
        print("password changed successfully")
    except:
        print("Couldn't Change Password")
    conn.commit()
    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def clearUserInfo():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM userInfo;")
    
    conn.commit()
    conn.close()

# -------------------------------------------------------------------------------------->>>>>>>>
# -----------------------------------DATASET--QUERIES----------------------------------->>>>>>>>
# -------------------------------------------------------------------------------------->>>>>>>>

def createDataset():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS dataset (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address TEXT,
        timestamp TEXT,
        request TEXT,
        status_code INTEGER,
        user_agent TEXT        
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
# --------------------------------------------------------------->>>>>>>>>>>

def getData():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = '''
    SELECT * FROM dataset;
    '''
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return data
# --------------------------------------------------------------->>>>>>>>>>>

def parse_apache_log_line(log_line):
    # Regular expression for common Apache log format
    log_pattern = re.compile(r'(?P<ip_address>\S+) \S+ \S+ \[.*?\] "(?P<method>\S+) (?P<request>\S+) \S+" (?P<status_code>\d+) \S+ "(?P<user_agent>.*?)"')

    # Match the log entry with the regular expression
    match = log_pattern.match(log_line)
    
    if match:
        groups = match.groupdict()
        timestamp_str = log_line.split('[')[1].split(']')[0].strip()  # Extract timestamp separately

        # Modify the timestamp format to match the provided log entries
        timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z').strftime('%Y-%m-%d %H:%M:%S')

        return {
            'ip_address': groups['ip_address'],
            'timestamp': timestamp,
            'request': f"{groups['method']} {groups['request']}",
            'status_code': int(groups['status_code']),
            'user_agent': groups['user_agent']
        }
    else:
        return None
# --------------------------------------------------------------->>>>>>>>>>>

def addData(log_file_path, database_name="database.db"):
    if log_file_path == '':
        print("Enter some Data")
        return "Enter some Data"
    # conn = sqlite3.connect("database.db")
    # cursor = conn.cursor()

    # query = '''
    # INSERT INTO dataset (temp)
    # VALUES (?)
    # '''
    # if all(char.isdigit() for char in temp):
    #     try:
    #         cursor.execute(query,(temp,))
    #         conn.commit()
    #         conn.close()
    #         print("Temperature Recorded")
    #         return "Temperature Recorded"
    #     except KeyError as e:
    #         print(e)
    # else:
    #     conn.commit()
    #     conn.close()
    #     print("Give Numeric Values")
    #     return "Give Numeric Values"

    # Connect to the SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    try:
        with open(log_file_path, 'r') as log_file:
            for log_line in log_file:
                # Parse each log entry
                log_data = parse_apache_log_line(log_line)
                print(log_data)
                # If the log entry is valid, insert it into the database
                if log_data:
                    cursor.execute(
                        'INSERT INTO dataset (ip_address, timestamp, request, status_code, user_agent) VALUES (?, ?, ?, ?, ?)',
                        (log_data['ip_address'], log_data['timestamp'], log_data['request'], log_data['status_code'], log_data['user_agent'])
                    )

        # Commit the changes and close the connection
        conn.commit()
        print("Data added successfully.")
    except Exception as e:
        print(f"Error adding data: {e}")
    finally:
        conn.close()

# --------------------------------------------------------------->>>>>>>>>>>

# def deleteData(day):

#     if(day == ""):
#         return "Enter the Day Number"

#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()

#     query = '''
#     DELETE FROM dataset 
#     WHERE id = (?)
#     '''
#     if all(char.isdigit() for char in day):
#         try:
#             cursor.execute(query,(day,))
#             conn.commit()
#             conn.close()
#         except:
#             print("Error occured")
#         else:
#             return "Temperature Deleted"
#     else:
#         conn.commit()
#         conn.close()
#         print("Enter Numeric Values")
#         return "Enter Numeric Values"

    
# --------------------------------------------------------------->>>>>>>>>>>

# def updateData(day, temp):

#     if(day == "" or temp == ""):
#         return "Enter Data in both fields"

#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()

#     query = '''
#     UPDATE dataset 
#     SET temp = (?)
#     WHERE id = (?)
#     '''
#     if all(char.isdigit() for char in day) and all(char.isdigit() for char in temp):
#         try:
#             cursor.execute(query,(temp, day))
#         except:
#             conn.commit()
#             conn.close()
#             print("Error occured")
#             return "Error Occured"
#         else:
#             return "Temperature Updated"
#     else: 
#         print("Enter Numeric Values")
#         return "Enter Numeric Values"

    
# --------------------------------------------------------------->>>>>>>>>>>

def clearDataset():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM dataset;")
    
    conn.commit()
    conn.close()

print(parse_apache_log_line('127.0.0.1 - - [22/Nov/2023:12:34:56 +0000] "GET /example-page HTTP/1.1" 200 1234 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"'))