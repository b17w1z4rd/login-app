import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_db.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL
)
""")

# Insert data into the users table
cursor.execute("""
INSERT INTO users (username, password, name, age, email) VALUES
('user1', 'pass123', 'Mike Smith', 30, 'mike@example.com'),
('user2', 'pass456', 'Jane Doe', 25, 'jane@example.com'),
('user3', 'pass789', 'John Brown', 40, 'john@example.com')
""")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
