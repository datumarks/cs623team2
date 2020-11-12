import psycopg2
from tabulate import tabulate




#cursor`
#For isolation: SERIALIZABLE
con.set_isolation_level(3)
#For atomicity
con.autocommit = False

try:
    cur = con.cursor()
    depot_headers = ["dep", "addr", "volume"]
    product_headers = ["prod", "pname", "price"]
    stock_headers=["dep","prod","qunatity"]

    query1=("select * from product")
    query2=("select * from depot")
    query3 = ("select * from stock")

    #query 4 failed transaction
    query4 = ("delete from DEPO where dep='d1'")

    query5=("delete from depot where dep='d1'")


  #  cur.execute(query4)
    cur.execute(query5)

    cur.execute(query1)
    product = cur.fetchall()
    print("Product")
    print(tabulate(product, product_headers, "psql"))

    cur.execute(query2)
    depot = cur.fetchall()
    print("Depot")
    print(tabulate(depot, depot_headers, "psql"))

    cur.execute(query3)
    stock = cur.fetchall()
    print("Stock")
    print(tabulate(stock, stock_headers, "psql"))



    print("Transaction successful")

except (Exception, psycopg2.DatabaseError) as err:
    con.rollback()
    print("Transaction failed! Column does not exist")
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")
