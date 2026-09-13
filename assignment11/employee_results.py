import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Task 1

conn = None
df = None

try:
    conn = sqlite3.connect('../db/lesson.db')
    
    df = pd.read_sql_query("SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;", conn)
    df.plot(kind = 'bar', x = 'last_name', y = 'revenue', legend = False, color = 'skyblue', rot = 45 )

    plt.xlabel('Employee Name')
    plt.ylabel('Revenue')
    plt.title('Employee Revenue')
    plt.tight_layout()
    plt.show()

except sqlite3.Error as e:
    print(f"Error connecting to database: {e}") 

finally:
    if conn:
        conn.close()
