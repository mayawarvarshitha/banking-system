#installed the library mysql-connector-python
import mysql.connector
class delete:
    def __init__(self):
     self.connect=mysql.connector.connect(
            host = "localhost",
            user = "mayawar",
            password = "Varu",
            database = "bank1"
            )
    def specific_del(self,table_name,cusid):
        cur = self.connect.cursor()
        cur.execute(f"delete from {table_name} where customerid={cusid}")
        self.connect.commit()
        print("Data has been deleted sucessfully")
    
        
