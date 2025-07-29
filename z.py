with open("C:\\Users\\nmoks\\Downloads\\ai engineer\\y.txt","r") as f:
    for i in f:
        j= i.strip().split(',')
        j=[int(x) for x in j]
        k=sum(j)
        print(k,j)
               
      



      
        


