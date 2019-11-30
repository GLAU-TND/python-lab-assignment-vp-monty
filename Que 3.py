while(1):
    try:
        n=0
        n = int(input("Enter a number"))
        print(n)
        break
    except Exception as e  :
        print("unchecked exception : ",e)
