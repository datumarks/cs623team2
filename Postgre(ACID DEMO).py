import psycopg2

#connect to the db
con = psycopg2.connect(
            host = "localhost",
            database="postgres",
            user = "postgres",
            password = "password")
#cursor`
#For isolation: SERIALIZABLE
con.set_isolation_level(3)
#For atomicity
con.autocommit = False
try:
    cur = con.cursor()
    #Either the next two statements are executed are not at all
    cur.execute("insert into employees (id, name) values (%s, %s)", (4, "Jeff"))
    cur.execute("insert into employees (id, name) values (%s, %s)", (5, "Suzy"))
    #execute query
    cur.execute("select id, name from employees")
    rows = cur.fetchall()
    for r in rows:
        print(f"id {r[0]} name {r[1]}")

except Exception as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()


#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()