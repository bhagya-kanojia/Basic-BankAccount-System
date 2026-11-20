import random
import json
import linecache


detail = {}
pointer = []

def get_index(inp):
    k = inp
    with open("Pointer.txt", "r") as poin:
        pointer = [line.strip() for line in poin]
        a = pointer.index(k)
    poin.close()
    return a


    

class BankAccount:

    def new_acc(self):
        def new_acc_no():
            with open("Pointer.txt", "r") as poin:
                    pointer = [line.strip() for line in poin]
            poin.close()
            t = True
            while t == True:
                ran_no = random.randint(1000,9999)
                chk = str(ran_no)
                if chk not in pointer:
                    break
            # Acc_No.append(ran_no)
            pointer.clear
            return ran_no
    

        self.name = str(input("Enter your name : "))
        self.dob = str(input("Enter your age : "))
        self.ph_no = int(input("Enter your phone number : "))
        self.acc_no = str(new_acc_no())
        self.balance = input("Enter the amount you want to save : ")
        bal = str(self.balance)
        print("Your account number is :", self.acc_no)
        
        detail[self.acc_no] = [self.name, self.dob, self.ph_no, self.balance]
        hold = json.dumps(detail)
        file = open("Details.txt", 'a')
        file.write(f"{hold}\n")
        file.close()
        detail.clear()
        poin = open("Pointer.txt",'a')
        poin.write(f"{self.acc_no}\n")
        poin.close
 

    def deposit(self):
        a_n = str(input("Enter your account number : "))
        indx = get_index(a_n)
        with open("Details.txt", "r") as file:
                    lines = file.readlines()
                    detail = json.loads(lines[indx])
        file.close()
        self.balance = float(detail[a_n][3])
        amt = float(input("enter the amount :- "))
        # print(self.balance,amt)
        if amt >0:
            self.balance = amt + self.balance
            print(f"Amount deposited.")
            # print(self.balance)

        detail[a_n][3] = self.balance
        lines[indx] = json.dumps(detail)
        with open("Details.txt", "w") as file:
             file.writelines(lines)
        file.close()

    def withdraw(self):
        a_n = str(input("Enter your account number : "))
        indx = int(get_index(a_n))
        with open("Details.txt", "r") as file:
                    lines = file.readlines()
                    detail = json.loads(lines[indx])
        file.close()
        self.balance = float(detail[a_n][3])

        amt = float(input("enter the amount :- "))
        if amt >0 and amt<=self.balance:
            self.balance = self.balance - amt
            print(f"Amount withdrawed.")

            detail[a_n][3] = self.balance
            lines[indx] = json.dumps(detail)
            with open("Details.txt", "w") as file:
                 file.writelines(lines)
            file.close()


    def show_balance(self):
        a_n = str(input("Enter your account number : "))
        indx = get_index(a_n)
        with open("Details.txt", "r") as file:
                    lines = file.readlines()
                    detail = json.loads(lines[indx])
        file.close()
        self.balance = detail[a_n][3]
        print(f"Your current balance is ",self.balance)

    def display(self):
        a_n = str(input("Enter your account number : "))
        with open("Details.txt", "r") as file:
            detail = json.load(file)
        file.close()
        print("----Account Details----")
        print("Name = ",detail[a_n][0])
        print("Account number = ",a_n)
        print("Date of Birth = ",detail[a_n][1])
        print("Phone Number = ",detail[a_n][2])
        print("Balance = ",detail[a_n][3])
        detail.clear()
        # print(detail)
    


# print("new account creation ")
# acc = BankAccount()
# # acc.new_acc()
# # acc.display()
# acc.deposit()
# acc.show_balance()