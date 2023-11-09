from create import insert
from read import read
obj = insert()

print("------ break management system--------")
print("for Inserting the data press 1 : ")
print("for Reading the data press 2 : ")
print("for Updating the data press 3 : ")
print("for deleting the data press 4 : ")

opr=int(input("please enter your operation: "))
def myopr():
    print("---- For Personal information press 1 ----")
    print("---- For Bank details press 2 ------------")
    print("---- For transaction details press 3 -------")
    print("---- For Account details press 4 ---------")
    vr = int(input("Please Select your table : "))

    if vr == 1:
        return 'personal_details'
    elif vr ==2:
        return 'bank_details'
    elif vr ==3:
        return 'transaction_details'
    elif vr ==4:
        return 'account_details'
    

if opr ==1:
    h = myopr() 
    if h=='personal_details':
        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addr = input("please eneter customer address:")
        pn = int(input("please enter customer phone number:"))
        an = input("please enter customer aadhar number:")
        pan = input("please enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)

    elif h=='bank_details':
            acn = int(input("please enter account number:"))
            cid = int(input("please enter customerid:"))
            ifsc = input("please enter ifsc code:")
            actype = input("please enter account type:")
            obj.bank_details(acn,cid,ifsc,actype)

    elif h=='transaction_details':
            transid = int(input("please enter transaction_id:"))
            sendacc = int(input("please enter sender acc num :"))
            recacc = int(input("please enter receiver account number:"))
            amount = int(input("pleases enter amount:"))
            mtd = (input("please select the method:"))
            obj.transaction_details(transid,sendacc,recacc,amount,mtd)

    elif h=='account_details':
            accn = int(input("please enter accountnum"))
            transid = int(input("please enter transaction_id :"))
            amount = int(input("pleases enter amount:"))
            cbal = int(input("please enter closing balance:"))
            tp = input("please enter the transactiontype:")
            obj.account_details(accn,transid,amount,cbal,tp)


objread = read()
if opr==2: # user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)

from update import update
objupdate = update()
if opr ==3:
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    colname = input("please enter column name:")
    newval = input("please enter new values:") # 500 str # 'jhon'
    objupdate.myupdate(j,colname,newval,cusid)

from delete import delete
objdelete = delete()

if opr ==4:
    k = myopr()
    cusid = int(input("please enter customer id to delete the data: "))
    objdelete.specific_del(k,cusid)

