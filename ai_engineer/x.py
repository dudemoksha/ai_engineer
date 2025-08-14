def count(n):
    coun=0
    with open("C:\\Users\\nmoks\\Downloads\\ai engineer\\y.txt","r") as f:
        for i in f:
            j= i.strip().split(',')
            j= [int(x) for x in j]
            coun+=j.count(n)
    return coun
print(count(9))
      
            


      
        


