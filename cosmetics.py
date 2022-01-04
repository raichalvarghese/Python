class cosmetics:
    def __init__(self,prdt_id,prdt_name,fruitInOrNot):
        self.prdt_id=prdt_id
        self.prdt_name=prdt_name
        self.fruitInOrNot=fruitInOrNot
list=[]
N=int(input("Enter the number of products:"))
for i in range(0,N):
    print("Enter the product id of",i,"th element:")
    p_id=int(input())
    print("Enter the product name of",i,"th element:")
    p_name=input()
    print("Fruit present or not:(0/1)")
    fi_n=int(input())
    list.append(cosmetics(p_id,p_name,fi_n))

print("Details of cosmetics with the fruit:")    
for obj in list:
    if obj.fruitInOrNot==1:
        print(obj.prdt_id,obj.prdt_name,sep=" ")
