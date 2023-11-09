#installed the library mysql-connector-python
import mysql.connector
class insert:
    def __init__(self):
     self.connect=mysql.connector.connect(
            host = "localhost",
            user = "mayawar",
            password = "Varu",
            database = "bank1"
            )

    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.connect.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.connect.commit()
        print("-------------------Personal information has been saved sucessfully-------------")

    def bank_details(self,acn,cid,ifsc,actype):
        cur = self.connect.cursor()
        cur.execute(f"INSERT INTO BANK_DETAILS VALUES({acn},{cid},'{ifsc}','{actype}')")
        self.connect.commit()
        print("------------------Bank details has been sucessfully saved-----------------------")

    def transaction_details(self,transid,sendacc,reciveracc,amount,method):
       cur=self.connect.cursor()
       cur.execute(f"INSERT INTO TRANSACTION_DETAILS VALUES({transid},{sendacc},{reciveracc},{amount},'{method}')")
       self.connect.commit()
       print('-----transaction_details has been saved successfully--------')

    def account_details(self,accno,transid,amount,cbal,tp):
       cur=self.connect.cursor()
       cur.execute(f"INSERT INTO ACCOUNT_DETAILS VALUES({accno},{transid},{amount},{cbal},'{tp}')")
       self.connect.commit()
       print('-----account_details has been saved successfully--------')

            
