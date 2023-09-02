class task:
    def __init__(self):
        self.l1=[]
        self.l2=[]
        
    def addtask(self,a):
        
        self.l2.append(0)
        self.l1.append(a)
       

    def complte(self,i):
        if i>=0 and i <=len(self.l1):
            self.l2[i]=1
        else:
            print("invalid index")
    def show(self):
        print()
        print("TO-DO LIST")
        print(20*"*")
        for k in range(len(self.l1)):
            if self.l2[k]==0:
                print(self.l1[k],"-NOT DONE")  
            else:
                print(self.l1[k],"-COMPLETED")
        print(20*"*")        




def todolist(): 
        t1=task()
        while True:
            print("MENU\n1.Add task\n2.complete task\n3.show task\n4.exit")
            a=input("enter your option:")
            match(a):
                    case "1":
                        a=input("enter your task:")
                        t1.addtask(a)
                    
                    case "2":
                        i=int(input("enter task index value to complete:"))
                        t1.complte(i-1)
                    
                    case "3":
                        t1.show()
                        
                    case "4":
                        print(10*"*")
                        print("THANK YOU")
                        print(10*"*")
                        break
                    case _:
                        print("Invalid option")

            print()
todolist()                