import pymysql 


conn=pymysql.connect(
    host='localhost',
    user='root',
    password='ambanadhills',
    database='sept_2026'
)

cur=conn.cursor()

#sql="create table emp_details(id int primary key, name varchar(20),salary int, dept varchar(20))"
#sql="insert into emp_details values(1,'arun',25000,'python')"
#sql="insert into emp_details values(2,'karun',26000,'analytics')"
#sql="insert into emp_details values(3,'manoj',19000,'java')"
#sql="insert into emp_details values(4,'shaan',35000,'django')"
#sql="insert into emp_details values(5,'varun',28000,'operations')"

sql="select * from emp_details"
cur.execute(sql)
rows=cur.fetchmany(3)
print(rows)
#rows=cur.fetchone()
#print(rows)
#rows=cur.fetchall()
#print(rows)
#for i in rows:
#    print(i)
 #   print(i[0],i[1],i[2],i[3])
conn.commit()

cur.close()
conn.close()