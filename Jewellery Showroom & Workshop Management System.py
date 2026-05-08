import datetime
import time

import mysql.connector

print("SQL Connection Details:")
HOST = input("Enter Host: ")
USER = input("Enter User: ")
PASSWORD = input("Enter Password: ")

myconn = mysql.connector.connect(host="localhost",user="root",passwd="Password")

mycursor = myconn.cursor()

#--------------------------------------------------------------------------------------------------

# Creating Database

mycursor.execute("CREATE DATABASE showroom_workshop_mgmt;")
mycursor.execute("USE showroom_workshop_mgmt;")

#--------------------------------------------------------------------------------------------------

# Creating Table of Employee Details

mycursor.execute("CREATE TABLE employee_details (\
    name VARCHAR(19),\
    gender VARCHAR(8),\
    phn_no BIGINT,\
    address VARCHAR(60),\
    task VARCHAR(40),\
    emp_id VARCHAR(24) NOT NULL,\
    PRIMARY KEY (emp_id)\
);")

# Inserting Values into Table Employee Details

mycursor.execute("INSERT INTO employee_details \
VALUES ('Rahul Prajapati','Male',9897398971,'RP Road Mumbai','Workshop Stock','Ra1Pra2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Binod Tharu','Male',9892348971,'BT Road Mumbai','Sales Management','Bi1Tha2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Ujjwal Chaurasia','Male',9892348971,'UC Road Mumbai','Workshop Management','Uj1Cha2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Anshu Bisht','Male',9892343471,'AB Road Mumbai','Showroom Stock','An1Bis2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Hitesh Khangta','Male',3492343471,'HK Road Mumbai','Billing','Hi1Kha2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Rakhi Sawant','Female',1022343471,'RS Road Mumbai','Receptionist','Ra1Saw2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Ajay Nagar','Male',9112343471,'AN Road Mumbai','Guard','Aj1Nag2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Payal Dhare','Female',9112693471,'PD Road Mumbai','Customer Care','Pa1Dha2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Samay Raina','Male',9112611171,'SR Road Mumbai','Sales','Sa1Rai2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Kaashvi Hiranandani','Female',9112691171,'KH Road Mumbai','Sales','Ka1Hir2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Saurav Joshi','Male',3452691171,'SJ Road Mumbai','Sweeping','Sa1Jos2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Avantika Bhatt','Female',7862691171,'AB Road Mumbai','Sweeping','Av1Bha2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Bhupendra Jogi','Male',7862567171,'BJ Road Mumbai','Smithing','Bh1Jog2');")
mycursor.execute("INSERT INTO employee_details \
VALUES ('Mithilesh Patankar','Male',7889567171,'MP Road Mumbai','Merchandiser','Mi1Pat2');")

#--------------------------------------------------------------------------------------------------

# Creating Table of Customer Details

mycursor.execute("CREATE TABLE customer_details (\
    name VARCHAR(25),\
    gender VARCHAR(20),\
    phn_no BIGINT,\
    address VARCHAR(150),\
    customer_id VARCHAR(20) NOT NULL,\
    PRIMARY KEY (customer_id)\
);")

# Inserting Values into Table Customer Details

mycursor.execute("INSERT INTO customer_details \
VALUES ('Ankit Bajpai','Male',0112553253,'AB Colony Pune','An1Baj2')")
mycursor.execute("INSERT INTO customer_details \
VALUES ('Suraj Singhania','Male',0144353253,'SS Colony Pune','Su1Sin2')")
mycursor.execute("INSERT INTO customer_details \
VALUES ('Rahul Srivastava','Male',0122353253,'RS Colony Pune','Ra1Sri2')")
mycursor.execute("INSERT INTO customer_details \
VALUES ('Adarsh Thakur','Male',0112553155,'At Colony Pune','Ad1Tha2')")

#--------------------------------------------------------------------------------------------------

# Creating Table of Products

mycursor.execute("CREATE TABLE products (\
    p_id VARCHAR(25),\
    p_type VARCHAR(100),\
    stock_quantity INT\
);")

# Inserting Values into Products Table

mycursor.execute("INSERT INTO products VALUES ('Ka_18','Kada',100)")
mycursor.execute("INSERT INTO products VALUES ('Ka_22','Kada',100)")
mycursor.execute("INSERT INTO products VALUES ('Cha_18','Chain',50)")
mycursor.execute("INSERT INTO products VALUES ('Cha_22','Chain',50)")
mycursor.execute("INSERT INTO products VALUES ('Rin_18','Ring',200)")
mycursor.execute("INSERT INTO products VALUES ('Rin_22','Ring',200)")
mycursor.execute("INSERT INTO products VALUES ('Nec_18','Necklace',60)")
mycursor.execute("INSERT INTO products VALUES ('Nec_22','Necklace',60)")
mycursor.execute("INSERT INTO products VALUES ('Pen_18','Pendant',80)")
mycursor.execute("INSERT INTO products VALUES ('Pen_22','Pendant',80)")
mycursor.execute("INSERT INTO products VALUES ('Ear_18','Earring',160)")
mycursor.execute("INSERT INTO products VALUES ('Ear_22','Earring',160)")
mycursor.execute("INSERT INTO products VALUES ('Aus_18','Auspicious Thread',40)")
mycursor.execute("INSERT INTO products VALUES ('Aus_22','Auspicious Thread',40)")
mycursor.execute("INSERT INTO products VALUES ('Nos_18','Nose Pin',140)")
mycursor.execute("INSERT INTO products VALUES ('Nos_22','Nose Pin',140)")
mycursor.execute("INSERT INTO products VALUES ('Br_18','Bracelet',55)")
mycursor.execute("INSERT INTO products VALUES ('Br_22','Bracelet',55)")
mycursor.execute("INSERT INTO products VALUES ('Bis_24','Biscuit',50)")
mycursor.execute("INSERT INTO products VALUES ('Coin_24','Coin',120)")

#--------------------------------------------------------------------------------------------------

# Creating Workshop Table

mycursor.execute("CREATE TABLE workshop (\
    order_id INT NOT NULL PRIMARY KEY,\
    customer_id VARCHAR(50),\
    product_type VARCHAR(50),\
    description VARCHAR(255),\
    due_date DATE\
);")


#--------------------------------------------------------------------------------------------------

# Creating Tables for Bill

mycursor.execute("CREATE TABLE bill_master (\
    bill_id INT AUTO_INCREMENT PRIMARY KEY,\
    grand_total DECIMAL(12,2)\
);")

mycursor.execute("CREATE TABLE bill_items (\
    bill_id INT,\
    description VARCHAR(60),\
    net_wt DECIMAL(6,3),\
    metal_rate DECIMAL(7,2),\
    making_charge DECIMAL(9,2),\
    total_amount DECIMAL(12,2)\
);")

#--------------------------------------------------------------------------------------------------

# Creating Sales Table

mycursor.execute("CREATE TABLE sales (\
    sale_id INT NOT NULL PRIMARY KEY,\
    customer_id VARCHAR(50) NULL,\
    product_id VARCHAR(50) NULL,\
    quantity INT NULL,\
    date DATE NULL,\
    total_amount DECIMAL(10,2) NULL\
);")

#--------------------------------------------------------------------------------------------------

# Creating Order Status Table

mycursor.execute("Create Table order_status (\
    order_id_ VARCHAR(20),\
    status VARCHAR(20)\
);")

#--------------------------------------------------------------------------------------------------

# Login Module

access = False

def login():
    """For Accessing The system, getting employee ID by the employee name."""
    mycursor.execute("SELECT * FROM employee_details;")
    emp_det = mycursor.fetchall()
    global access
    while not access:
        emp_name = input("Enter Employee name: ")
        emp_id = input("Enter Employee ID: ")
        if any(emp_name == r[0] for r in emp_det):
            for emp in emp_det:
                if emp[0] == emp_name:
                    if emp[-1] == emp_id:
                        time.sleep(1)
                        print("Access Granted!")
                        access = True
                        break
                    else:
                        time.sleep(1)
                        print("Invalid ID!")
                        print("Access Denied!")
                        access = False
        else:
            time.sleep(1)
            print("You are not an Employee!")
            print("Access Denied!")
            access = False

myconn.commit()

#--------------------------------------------------------------------------------------------------

# Employee Management Module

def employee_details():
    """Getting the details of an Employee by Employee Name."""
    mycursor.execute("SELECT * FROM employee_details;")
    emp_det = mycursor.fetchall()
    x = input("Enter Name of the Employee: ")
    if any(j[0].lower() == x.lower() for j in emp_det):
        for i in emp_det:
            if i[0].lower() == x.lower():
                print(i)
                time.sleep(1)
                break
    else:
        time.sleep(1)
        print("Employee not found.")
    myconn.commit()

def modify_employee_task():
    """Assigning and Modifying task of an Employee by Employee Name."""
    mycursor.execute("SELECT * FROM employee_details;")
    emp_det = mycursor.fetchall()
    x = input("Enter Name of the Employee: ")
    if any(i[0] == x for i in emp_det):
        new_task = input(f"What task would you like to assign to {x}?: ")
        task_query = f"UPDATE employee_details SET task = '{new_task}' WHERE name = '{x}';"
        mycursor.execute(task_query)
        print("Employee Task Modified!")
    else:
        print("Employee not found")
    myconn.commit()

#--------------------------------------------------------------------------------------------------

# Customer Management Module

def display_customer_details():
    """Getting the details of a Customer by Customer Name."""
    x = input("Enter Customer Name: ")
    mycursor.execute("SELECT * FROM customer_details;")
    customer_det = mycursor.fetchall()
    if any(j[0] == x for j in customer_det):
        for i in customer_det:
            if i[0] == x:
                print(i)
                time.sleep(1)
                break
    else:
        time.sleep(1)
        print("Customer not found")
    myconn.commit()

def add_customer_details():
    """Adding the details of a New Customer."""
    cus_name = input("Enter Customer Name: ")
    cus_gender = input("Enter Customer Gender: ")
    cus_phone = input("Enter Customer Phone: ")
    cus_address = input("Enter Customer Address: ")
    cus_id = input("Enter Customer ID: ")
    add_query = (f"INSERT INTO customer_details \
                 VALUES ('{cus_name}', '{cus_gender}', '{cus_phone}', '{cus_address}', '{cus_id}');")
    mycursor.execute(add_query)
    print("Customer Details Added!")
    myconn.commit()

def update_customer_details():
    """Updating the details of a Customer by Customer Name."""
    x = input("Enter Customer Name: ")
    mycursor.execute("SELECT * FROM customer_details;")
    customer_det = mycursor.fetchall()
    if any(i[0] == x for i in customer_det):
        new_det_col = input(f"Which detail would you like to update?: ")
        new_det = input(f"Enter new detail for {new_det_col}: ")
        update_query = f"UPDATE customer_details SET {new_det_col.lower()} = '{new_det.lower()}' WHERE name = '{x}';"
        mycursor.execute(update_query)
        print("Customer Details Updated!")
    else:
        print("Customer not found.")
    myconn.commit()

#--------------------------------------------------------------------------------------------------

# Products Management Module

def search_products():
    """Searching Products Details using Product ID."""
    search_id = input("Enter Product ID: ")
    mycursor.execute("SELECT * FROM products;")
    products = mycursor.fetchall()
    if any(i[0]==search_id for i in products):
        for product in products:
            if product[0] == search_id:
                print("(ID, Type, Quantity)")
                print(product)
                time.sleep(1)
                break
    else:
        time.sleep(1)
        print("Product not found.")
    myconn.commit()

def add_products():
    """Adding products to Products Table."""
    p_id = input("Enter Product ID: ")
    p_type = input("Enter Product Type: ")
    quantity = input("Enter Product Quantity: ")
    add_query = f"INSERT INTO products VALUES ('{p_id}', '{p_type}', '{quantity}');"
    mycursor.execute(add_query)
    print("Products Added!")
    myconn.commit()

def update_products():
    """Updating Stock Quantity of Products."""
    n_id = input("Enter Product ID whose Stock Quantity you want to update: ")
    n_quantity = int(input("Enter Product Quantity: "))
    if n_quantity == 0:
        mycursor.execute(f"DELETE FROM products WHERE p_id = '{n_id}';")
    else:
        update_query = f"UPDATE products SET stock_quantity = '{n_quantity}' WHERE p_id = '{n_id}';"
        mycursor.execute(update_query)
        print("Products Details Updated!")
    myconn.commit()

#--------------------------------------------------------------------------------------------------

# Inserting Values into Workshop Table

def order():
    """Recording Order details in Workshop Table"""
    c = "y"
    while c == "y":
        order_id = input("Enter Order ID: ").strip()
        customer_id = input("Enter Customer ID: ").strip()
        product_type = input("Enter Product Type: ").strip()
        description = input("Enter Description: ").strip()
        de_date = input("Enter Due Date(YYYY-MM-DD): ").strip()
        format_string = "%Y-%m-%d"
        due_date = datetime.datetime.strptime(due_date, format_string)
        mycursor.execute(f"INSERT INTO workshop \
        VALUES ({order_id}, '{customer_id}', '{product_type}', '{description}', '{due_date}');")
        c = input("Would you like to continue? (y/n): ").strip().lower()

# Displaying Order Status

def display_order_status():
    """Updating Order Status with respect to Due Date."""
    mycursor.execute("SELECT * FROM workshop;")
    sale_records = mycursor.fetchall()

    for sale_record in sale_records:
        print("Order ID: ", sale_record[0],"; Due Date: ",sale_record[-1])
        status = input("Status?(Pending/Done/Delivered): ").strip()
        if status == "Pending":
            mycursor.execute(f"INSERT INTO order_status VALUES ('{sale_record[0]}','{status}');")
            myconn.commit()
        elif status == "Delivered":
            mycursor.execute(f"INSERT INTO order_status VALUES ('{sale_record[0]}','{status}');")
        elif status == "Done":
            if datetime.date.today() <= sale_record[-1]:
                mycursor.execute(f"INSERT INTO order_status VALUES ('{sale_record[0]}','{status}');")
            else:
                new_date = input("Enter new Due Date: ")
                mycursor.execute(f"INSERT INTO order_status VALUES ('{sale_record[0]}','{new_date}');")
    mycursor.execute("SELECT * FROM order_status;")
    print("\n----- ORDER STATUS -----")
    print(mycursor.fetchall())
    myconn.commit()

#--------------------------------------------------------------------------------------------------

# Creating Billing Module

def bill():
    """Generating Bill of the Products Purchased"""
    # ---------- CREATE NEW BILL ----------
    mycursor.execute("INSERT INTO bill_master (grand_total) VALUES (0)")
    myconn.commit()

    bill_id = mycursor.lastrowid
    grand_total = 0

    print("\nBill No:", bill_id)

    # ---------- ADD PRODUCTS ----------
    while True:
        desc = input("\nEnter product name: ")
        net_wt = float(input("Enter net weight: "))
        rate = float(input("Enter metal rate: "))
        making = float(input("Enter making charge: "))

        total = (net_wt * rate) + making
        grand_total += total

        mycursor.execute(f"INSERT INTO bill_items \
                         VALUES ('{bill_id}','{desc}','{net_wt}','{rate}','{making}','{total}');")
        myconn.commit()

        # Stock Updating

        pr_id = input("Enter Product ID of the product: ")
        q = int(input("Enter Quantity of the product: "))
        update_q = f"UPDATE products SET stock_quantity = stock_quantity-{q} WHERE p_id = '{pr_id}';"
        mycursor.execute(update_q)
        myconn.commit()

        ch = input("Add another product? (y/n): ")
        if ch.lower() != 'y':
            break

    # ---------- UPDATE GRAND TOTAL ----------
    mycursor.execute(f"UPDATE bill_master SET grand_total={grand_total} WHERE bill_id={bill_id};")
    myconn.commit()

    # ---------- DISPLAY BILL ----------
    time.sleep(1)
    print("\n----- BILL -----")
    mycursor.execute(f"SELECT * FROM bill_items WHERE bill_id={bill_id};")
    items = mycursor.fetchall()

    for item in items:
        print(item[1], "₹", item[5])

    print("------------------------")
    print("GRAND TOTAL: ₹", grand_total)

#--------------------------------------------------------------------------------------------------

# Inserting Sales Records

def sales():
    """Updating Records of Sales."""
    sale_id = int(input("Enter Sale ID: "))
    sales_cus_id = input("Enter Customer ID: ")
    sales_pro_id = input("Enter Product ID: ")
    sales_rate = int(input("Enter Product Rate: "))
    sales_quantity = int(input("Enter Sale Quantity: "))
    sales_date = datetime.date.today()
    sales_total = sales_quantity * sales_rate

    sales_query = (f"INSERT INTO sales \
                   VALUES ({sale_id},'{sales_cus_id}','{sales_pro_id}',{sales_quantity},'{sales_date}',{sales_total});")
    mycursor.execute(sales_query)
    print("Sales Record Updated!")
    myconn.commit()

# Displaying Monthly Sales Record

def monthly_record():
    date1 = input("Enter Month First Date (YYYY-MM-DD): ")
    date2 = input("Enter Month Last Date (YYYY-MM-DD): ")

    show_query = f"""
    SELECT sale_id, customer_id, product_id, quantity, date, total_amount
    FROM sales
    WHERE date BETWEEN '{date1}' AND '{date2}';
    """

    mycursor.execute(show_query)
    records = mycursor.fetchall()

    for row in records:
        sale_id = row[0]
        cus_id = row[1]
        pro_id = row[2]
        qty = row[3]
        sale_date = row[4].strftime("%Y-%m-%d")
        total = float(row[5])
        print(f"({sale_id}, {cus_id}, {pro_id}, {qty}, {sale_date}, {total})")
    myconn.commit()
    time.sleep(1)


#--------------------------------------------------------------------------------------------------

# Integrating All Modules and Preparing Final Program for Demonstration


while True:
    print("\n=========================================================")
    print("\t\t\tWELCOME TO ELEGANTE JEWELS!")
    print("=========================================================")
    time.sleep(0.5)
    print("1. Login")
    time.sleep(0.5)
    print("2. Work with Employee Details")
    time.sleep(0.5)
    print("3. Work with Customer Details")
    time.sleep(0.5)
    print("4. Manage Stock Details")
    time.sleep(0.5)
    print("5. Manage Workshop")
    time.sleep(0.5)
    print("6. Create Bill")
    time.sleep(0.5)
    print("7. Work with Sales")
    time.sleep(0.5)
    print("8. Exit")
    time.sleep(0.5)
    choice = int(input("Enter your choice(1-8): "))
    if choice == 1:
        print("\n=========================================================")
        print("\t\t\t\t\t\tLOGIN!")
        print("=========================================================")
        time.sleep(1)
        login()
    elif choice == 2:
        time.sleep(1)
        print("\n=========================================================")
        print("\t\t\tWorking With Employee Details!")
        print("=========================================================")
        time.sleep(1)
        print("1. Get Details of an Employee")
        time.sleep(1)
        print("2. Update or Assign a task to an Employee")
        time.sleep(1)
        choice2 = int(input("Enter your choice(1-2): "))
        if choice2 == 1:
            employee_details()
        elif choice2 == 2:
            modify_employee_task()
    elif choice == 3:
        print("\n=========================================================")
        print("\t\t\tWorking With Customer Details!")
        print("=========================================================")
        time.sleep(1)
        print("1. Display a Customer's Details")
        time.sleep(1)
        print("2. Adding a New Customer")
        time.sleep(1)
        print("3. Updating a Customer's Details")
        time.sleep(1)
        choice3 = int(input("Enter your choice(1-3): "))
        if choice3 == 1:
            display_customer_details()
        elif choice3 == 2:
            add_customer_details()
        elif choice3 == 3:
            update_customer_details()
    elif choice == 4:
        print("\n=========================================================")
        print("\t\t\t\t\tStock Handling!")
        print("=========================================================")
        time.sleep(1)
        print("1. Search Product Details")
        time.sleep(1)
        print("2. Add Product Details")
        time.sleep(1)
        print("3. Update Product Details")
        time.sleep(1)
        choice4 = int(input("Enter your choice(1-3): "))
        if choice4 == 1:
            search_products()
        elif choice4 == 2:
            add_products()
        elif choice4 == 3:
            update_products()
    elif choice == 5:
        print("\n=========================================================")
        print("\t\t\t\tWorkshop Management!")
        print("=========================================================")
        time.sleep(1)
        print("1. Insert Records of Orders")
        time.sleep(1)
        print("2. Update and Display Status of Orders")
        time.sleep(1)
        choice5 = int(input("Enter your choice(1-2): "))
        if choice5 == 1:
            order()
        elif choice5 == 2:
            display_order_status()
    elif choice == 6:
        time.sleep(1)
        bill()
    elif choice == 7:
        print("\n=========================================================")
        print("\t\t\t\tSales Management!")
        print("=========================================================")
        time.sleep(1)
        print("1. Updating Records of Sales")
        time.sleep(1)
        print("2. Displaying Record of Monthly Sales")
        time.sleep(1)
        choice6 = int(input("Enter your choice(1-2): "))
        if choice6 == 1:
            sales()
        elif choice6 == 2:
            monthly_record()
    elif choice == 8:
        time.sleep(1)
        print("\n=========================================================")
        print("\t\t\t\tThank You For Visiting!")
        print("=========================================================")
        break
    else:
        time.sleep(1)
        print("Invalid Choice")
