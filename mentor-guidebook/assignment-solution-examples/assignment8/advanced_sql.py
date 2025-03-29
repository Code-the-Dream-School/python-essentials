import sqlite3
import traceback

try: # SQL operations can raise exceptions!
    
    # The with statement is helpful, because it ensures that the connection
    # is closed at the end, even if an exception occurs
    with sqlite3.connect("../db/lesson.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")  
        cursor = conn.cursor()
        # TASK 1
        # This does a SELECT and a subquery
        stmt = """SELECT o.order_id, l.line_item_id, p.product_name FROM orders  
        o JOIN line_items l on o.order_id = l.order_id JOIN products p on 
        l.product_id = p.product_id WHERE o.order_id IN 
        (SELECT order_id from orders ORDER BY order_id limit 5);"""
        cursor.execute(stmt)
        result = cursor.fetchall()
        for row in result:
            print(row)

        # TASK 2
        # This retrieves the first 5 orders joined with the line_items and products tables, 
        # and aggregates (SUM) the quantity by the price to give the cost of each order
        stmt = """SELECT o.order_id, SUM(l.quantity * p.price) FROM orders o JOIN line_items l ON 
        o.order_id = l.order_id JOIN products p on l.product_id = p.product_id GROUP BY o.order_id 
        ORDER BY o.order_id LIMIT 5;"""
        cursor.execute(stmt)
        result = cursor.fetchall()
        for row in result:
            print(row)

        # TASK 3
        # This creates a new order with corresponding line_items.  First, we get the ids of
        # the customer, the employee, and the products.
        stmt = """SELECT customer_id FROM customers WHERE customer_name = \"Perez and Sons\";"""
        cursor.execute(stmt)
        result = cursor.fetchone()
        print(result)
        customer_id = result[0]
        stmt = """SELECT employee_id FROM employees WHERE first_name = \"Miranda\" AND last_name = \"Harris\";"""
        cursor.execute(stmt)
        result = cursor.fetchone()
        print(result)
        employee_id = result[0]
        stmt = """SELECT product_id FROM products ORDER BY price DESC LIMIT 5"""
        cursor.execute(stmt)
        result=cursor.fetchall()
        print("product list: ", result)
        products = result

        # Now we add the order, saving the returned order_id.  This example uses a parameterized
        # statement, as is best practice when putting variable values into SQL.
        stmt = f"""INSERT INTO orders (employee_id, customer_id) VALUES (?,?) RETURNING order_id"""
        cursor.execute(stmt,(employee_id, customer_id))
        result = cursor.fetchone()
        print(result)
        order_id = result[0]
        values = []
        value_list = []
        for i in range(5):
            values.append("(?,?, 10)")
            value_list.append(order_id)
            value_list.append(products[i][0]) # The product ids we want
        values_string = ",".join(values)      
        stmt = f"""INSERT INTO line_items (order_id, product_id, quantity) VALUES {values_string};"""
        # This looks a little questionable, because we are using a formattted string for SQL.
        # But the contents of the formatted string are created in the code, so it's safe --
        # There is no potential of a security attack.  We do this to add the 5 line_item
        # records with 1 insert statement.  For the actual values we use a parameterized
        # statement.
        print(stmt)
        cursor.execute(stmt, value_list)  
        conn.commit()
        stmt="""SELECT l.line_item_id, l.quantity, p.product_name FROM line_items l JOIN products p ON 
        l.product_id = p.product_id WHERE l.order_id = ?;"""
        cursor.execute(stmt, (order_id,))
        result = cursor.fetchall()
        for row in result:
            print(row)

        # TASK 4
        stmt = """SELECT first_name, last_name, COUNT(order_id) as count FROM employees e JOIN orders o 
        ON e.employee_id = o.employee_id GROUP BY e.employee_id HAVING COUNT(order_id) >5;"""
        cursor.execute(stmt)
        result = cursor.fetchall()
        for row in result:
            print(row)
        
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
else:
    print("All SQL operations completed.")
    