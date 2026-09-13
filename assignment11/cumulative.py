import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Task 2
conn = None
df = None

try:
    conn = sqlite3.connect('../db/lesson.db')
    df = pd.read_sql_query(
    "SELECT o.order_id, SUM(l.quantity * p.price) AS total_price FROM orders o JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY o.order_id ORDER BY o.order_id;", conn)
    df['cumulative'] = df['total_price'].cumsum()

    df.plot(kind = 'line', x = 'order_id', y = 'cumulative', legend = False, color = 'skyblue', rot = 45 )
    plt.xlabel('Order ID')
    plt.ylabel('Cumulative Revenue')
    plt.title('Cumulative Revenue vs Order ID')
    plt.tight_layout()
    plt.show()
    

except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")

finally:
    if conn:
        conn.close()