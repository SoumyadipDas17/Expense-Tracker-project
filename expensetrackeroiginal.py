import pickle
def addrecord(): ####1
    ans="Y"
    while ans=="Y":
            tpe=input("enter type(income/expense):")
            if tpe.upper()!="INCOME" and tpe.upper()!="EXPENSE":
                print("types other than 'INCOME' or 'EXPENSE' can not be added")
                break
            amount=float(input("enter amount:"))
            category=input("category:")
            date=input("date(DD/MM/YYYY):")
            if len(date)!=10 or date[2]!="/" or date[5]!="/" or not(date[0:2].isdigit()) or not(date[3:5].isdigit()) or not(date[6:10].isdigit())  :
                print("Can't add this date becuse it is not in DD/MM/YYYY format!")
                break
            record["type"]=tpe.upper()
            record["amount"]=amount
            record["category"]=category.upper()
            record["date"]=date
        
            ans=input("want to enter more reords(y//n):").upper()
            
            pickle.dump(record,f)
         
def edit(): ####2
    f.seek(0)
    entry=1
    newdiction=[]
    l=[]
    try:
        while True :
            newdiction=pickle.load(f)
            l.append(newdiction)
    except EOFError :
        
        ans="y"
        while ans=="y":
            serial=int(input(" enter transaction number whose record u want to edit:"))
            l[serial-1]["type"]=input("enter type(income/expense):").upper()
            if l[serial-1]["type"]!="INCOME" or l[serial-1]["type"]!="EXPENSE" :
                print("types other than 'INCOME' or 'EXPENSE' can not be added")
                entry=0
                break
                            
            l[serial-1]["amount"]=float(input("enter amount:"))
            l[serial-1]["category"]=input("category:").upper()
            l[serial-1]["date"]=input("date:")
            
            if len(l[serial-1]["date"])!=10 or l[serial-1]["date"][2]!="/" or l[serial-1]["date"][5]!="/" or not(l[serial-1]["date"][0:2].isdigit()) or not(l[serial-1]["date"][3:5].isdigit()) or not(l[serial-1]["date"][6:10].isdigit()) :
                print("Can't add this date becuse it is not in DD/MM/YYYY format!")
                entry=0
                break
            ans=input("want to edit more reords(y//n):")
        if entry==0 :
            return
        fh=open("expensetracker.dat","wb")
        fh.seek(0)
        for i in l :
            pickle.dump(i,fh)
        fh.close()    

def remove(): ####3
    ans=input("Do u want to delete record(y//n)").upper()
    serial=[]
    l=[]
    while ans=="Y" :
        i=int(input("enter the serial number of the record u want to delete:"))
        serial.append(i)
        ans=input("do u want to delete record(y//n)").upper()
    newdiction={}
    f.seek(0)
    try:
        while True :
            newdiction=pickle.load(f)
            l.append(newdiction)
    except :
        pass
    for j in sorted(serial,reverse=True) :
        del l[j-1]
    fh=open("expensetracker.dat","wb")
    fh.seek(0)
    for i in l :
        pickle.dump(i,fh)
    fh.close()
    print("records has been removed from your transaction history/nyour current transaction history is :-")
    history ()
                            
    
def balance():  ####5
    f.seek(0)
    income=0
    expense=0
    a={}
    try:
        while True :
            a=pickle.load(f)
            if a["type"]=="INCOME":
                income+=a["amount"]
            if a["type"]=="EXPENSE":
                expense+=a["amount"]
    except:
         print("The total income is",income,"\nThe total expense is",expense,"\nBalance=" ,income-expense)
                
    
     
   
        
def filter():       ####6
    f.seek(0)
    
    print("\t1.type\t2.amount\t3.category\t4.date:")
    x=int(input("enter filter: "))
    fd={}
    if x==1:
           fil="type"
    elif x==2:
           fil="amount"
    elif x==3:
           fil="category"
    elif x==4:
           fil="date"
    if x==2 :       
        val=float(input("enter value:"))
    else :
        val=input("enter value:").upper()
    
    try :
        while True :
            fd=pickle.load(f)
        
            
            if (fil in fd) and (fd[fil]==val):
                print(fd)
    except :
        print("")
        

def history():      ####7
           
    print("tranaction number","\t transaction record")
    f.seek(0) 
    d={}
    i=1
    try:
        while True :
            d=pickle.load(f)           
            print(i,"\t\t\t",d)
            i+=1
    except:
        print("")

def monthlysummary():       ####8
    m=input("enter month")
    y=input("enter year")
    a={}
    record={}
    f.seek(0)
    
    try:
        while True:
            a=pickle.load(f)
            

            if (a["date"][3:5] == m) and ( a["date"][6:10]==y) :
                if a["type"] not in record:
                    record[a["type"]]=a["amount"]
                else:
                    record[a["type"]]+=a["amount"]
                if a["category"] not in record:
                    
                    record[a["category"]]=a["amount"]
                else :
                    record[a["category"]]+=a["amount"]
    except EOFError :
        if "INCOME" in record:
            print("income is :",record["INCOME"])
            del record["INCOME"]
        if "EXPENSE" in record:
            print("expense is :",record["EXPENSE"])
            del record["EXPENSE"]
        print ("\n\t\t\t\t\t\t*************categorywise totals*************\n")
        
        for i in record :
            print(i,":",record[i])
def categorywisetotals():       ####9
    c=input("enter the category:").upper()
    a={}
    record={}
    f.seek(0)
    total=0
    try:
        while True:
            a=pickle.load(f)
            if a["category"]==c:
                total+=a["amount"]
    except EOFError :
        print("TOTAL=",total)
                                
                                 
#####################################################           MAIN            ##################################################################
          
l=[]
record={}
ans="y"
f=open("expensetracker.dat","ab+")
while True :
    print("\n*********************************************************************MAIN MENU*********************************************************************\n")
    print("1.ADD\t\t2.EDIT\t\t3.REMOVE\t\t4.EXIT\t\t5.BALANCE\t\t6.FILTER\t\t7.HISTORY\t\t8.MONTHLY SUMMARY\t\t9.CATEGORYWISE TOTALS\t\t10.DELETE HISTORY")
    
    menu=int(input("\nENTER THE NUMBER PRESENT BEFORE THE OPTIONS IN ORDER TO USE IT:"))
    if menu==1 :
        addrecord()
    elif menu==2:
        edit()
        
    elif menu==3 :
        remove()
      
    elif menu==4 :
        f.close()
        break
        
    elif menu==5 :
        balance()
    elif menu==6:
        filter()
    elif menu==7 :
        history()
    elif menu==8:
        monthlysummary()
    elif menu==9 :
        categorywisetotals()
    elif menu==10 :
        choice=input("WARNING!!!\n your entire transaction history will be deleted. Do you want to delete your entire transaction history(y/n):")
        if choice=="y" :
            fh=open("expensetracker.dat","wb")
            fh.close()
    else :
        print("INVALID CHOICE!!")
            
        
               
        
        
