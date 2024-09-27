import json
from jinja2 import Template
from psycopg.conninfo import make_conninfo
from psycopg2_pool import *

# Establish a connection to the PostgreSQL database
conn_info = make_conninfo(host='localhost', port=5432, dbname='wixitasks', user='postgres', password='admin1234')

# Create a cursor object
cur = conn_info.cursor()

try:
    # Execute a SELECT statement
    cur.execute("SELECT * FROM wixitasks")

    # Fetch all the rows from the cursor
    rows = cur.fetchall()

    # Convert rows to a list of dictionaries
    records = []
    for row in rows:
        record = {}
        for i, column in enumerate(cur.description):
            record[column.name] = row[i]
        records.append(record)

    # Write records to a JSON file
    with open('output.json', 'w') as f:
        json.dump(records, f, indent=4)

    # Render the JSON data into HTML using Jinja2 template
    with open('template.html', 'r') as template_file:
        template = Template(template_file.read())
        html_content = template.render(data=records)

    # Print to screen

    # Write the HTML content to a file
    with open('output.html', 'w') as html_file:
        html_file.write(html_content)

except psycopg2.Error as e:
    print("Error executing SELECT statement:", e)

finally:
    # Close the cursor and the connection
    cur.close()
    conn.close()
