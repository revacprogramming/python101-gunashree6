# Databases
# https://www.py4e.com/lessons/database
import sqlite3
con=sqlite3.connect(":memory:")
c=con.cursor()
c.execute("""CREATE TABLE "Ages" (
          "name"	TEXT,
          "age"	INTEGER
        )""")
def add_information(aname,nage):
    with con:
        c.execute("INSERT INTO Ages VALUES(:name,:age)",{'name':aname,"age":nage})
A=[('Livie', 26),('Zayn', 23),('Yassin', 21),('Malik', 39),('Louise', 30),('Kaiwen', 16)]
for item in A:
  aname,nage=item
  add_information(aname,nage)
c.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
print(c.fetchall())

con.commit()
con.close()


