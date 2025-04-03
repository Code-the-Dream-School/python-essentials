import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT o.order_id, SUM(price * quantity) AS total_price 
    FROM orders o JOIN line_items l 
    ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY o.order_id;"""
    df = pd.read_sql_query(sql_statement, conn)

def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

df.plot(x="order_id", y="cumulative", kind="line", title="Cumulative Revenue")
plt.show()