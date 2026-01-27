import psycopg2
connection = psycopg2.connect(database="postgres",user="postgres",password="......",host="localhost",port="5432")
cursor = connection.cursor()
print("DB opened successfully")

insert_query="""insert into emp1 (name, dep,salary) values(%s,%s,%s)"""

cursor.execute(insert_query,("Pruthvi","Engg",75000))
connection.commit()
print("innsert successfully")