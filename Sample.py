import csv

class DB:
    def __init__(self,filename):                #constructor which is used to load csv file in python class object. It will be called as soon as the object is created.
        with open(filename,newline='') as f:
          reader = csv.reader(f)
          data = list(reader)
          for row in data[1:]:
              print(row)
        print("-------------------------------------------")
        print("Do you want to search a record or exit:[Y/N]?")
        ans = str(input()).lower()
        if ans == 'y':
            self.find(data)               #calling the find function and passing the data i.e. nested list to it for searching records
        else:
            exit()

    def find(self,data):
        self.data = data
        print("Enter the keyword by which you want to search record/ First_name/Last_name/Age/Home_city")
        prompt = input()
        if prompt == "First_name":     #branch of if which is used to sarch first name.
            print("Enter First Name:")
            x = str(input()).lower()   #lower to convert all the uppercase to lowercase to avoid runtime errors.
            count = 0
            for row in  self.data[1:]:
                if x in row:
                    print(row)
                    count +=1          #count variable to keep track wether the search was successful or not>
                else:
                    continue
            if count ==0:              #nested branch for unsuccessful search.
                print("You Have entered wrong first name")   
                print("Do you want to search again??[y/n]")
                yn = str(input()).lower()
                if yn=='y':
                    self.find(data)
                else:
                    exit()
            else:
                print("Do you want to search again??[y/n]") 
                yn = str(input()).lower()
                if yn=='y':
                    self.find(data)
                else:
                    exit()        #to exit the program directly.
        elif prompt == "Last_name": #primary branch to search according to the Last name.
            print("Enter Last Name:")
            x = str(input()).lower()
            count = 0
            for row in  self.data[1:]:
                if x in row:
                    print(row)
                    count +=1
                else:
                    continue
            if count ==0:          #branch if the search is unsuccessful
                print("You Have entered wrong Last name")
                print("Do you want to search again??[y/n]")
                yn = str(input()).lower()
                if yn=='y':
                    self.find(data)
                else:
                    exit()
            else:
                print("Do you want to search again??[y/n]") #prompt to search again if the search was unsuccesful.
                yn = str(input()).lower()
                if yn=='y':
                    self.find(data)
                else:
                    exit()
            
        else:
            prompt == "Age":     #primary branch that will find record according to the Age.
            print("Enter Age:")
            x = str(input()).lower()
            count = 0
            for row in  self.data[1:]:
                if x in row:
                    print(row)
                    count +=1
                else:
                    continue
            if count ==0:       #secondary nested condition if the search is unsuccessful
                print("You Have entered wrong Age")
                print("Do you want to search again??[y/n]")
                yn = str(input()).lower()
                if yn=='y':
                    self.find(data)
                else:
                    exit()
            else:
                print("Do you want to search again??[y/n]") #prompt to search again.
                yn = str(input()).lower()
                if yn=='y':
                    self.find(data)
                else:
                    exit()

            
            
                    
        

DB1 = DB("Sample.csv")
        


