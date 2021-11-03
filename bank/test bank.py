import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from tkinter import Button, Entry, Frame, Label, Listbox, Message, messagebox
from tkinter.constants import COMMAND, END
import random
import secrets
import datetime

datetime_object = datetime.datetime.now()
class test(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        
        self.geometry("400x300")
        self.wm_title("bank application")
        
        
        container = tk.Frame(self, height=400,width=600)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (SignIn, Register, Bank, DepositAndWithdraw):
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(SignIn)
    
    def show_frame(self, y):
        frame = self.frames[y]
        frame.tkraise()

    def authorizeUser(self):
        username = name_entry.get()
        PINNo = pass_entry.get()
        global retainUsername
        f = open("User.txt","r")
        info = f.read()
        info = info.split()
        if username in info:
            index = info.index(username) + 1
            usr_password = info[index]
            
            if usr_password == PINNo:
                retainUsername = username
                self.show_frame(Bank)
                messagebox.showinfo(title="Welcome",message="Welcome, " + username)
            
                    
            else:
                messagebox.showerror(title="error",message="Enter correct password.")
                pass_entry.focus()
                
        else:
            messagebox.showerror(title="error",message="Enter an existing username.")
            name_entry.focus()

        
    
class SignIn(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg= "#7851a9")
        
        #def submit():
            
            #u_name = name_entry.get()
            #u_pass = pass_entry.get()
            
            #with open("user.txt", "r") as file2:
              #  x = file2.read(
                
               # print(x)

        global name_entry
        global pass_entry
                
    
                

        # sign in label
        label = tk.Label(self, text="Sign In Page",font=('Helvetica', 18, "bold" ))
        label.pack(padx=10, pady=10)
        
        #name label and input
        name_label = tk.Label(self, text = "Username",bg = "#c7d3d4", fg="black")
        name_label.place(x = 40, y = 60)

        name_entry = tk.Entry(self, width = 30)
        name_entry.place(x = 110, y = 60)

        #password label and input
        pass_label = tk.Label(self, text = "Password",bg = "#c7d3d4", fg="black")
        pass_label.place(x = 40, y = 100)

        pass_entry = tk.Entry(self, width = 30)
        pass_entry.place(x = 110, y = 100)

        #submit button
        submit_button = tk.Button(self, text = "Submit", bg = "#c7d3d4", fg="black", command = lambda:controller.authorizeUser())
        submit_button.place(x = 40, y = 150)
        
        
        # register button           
        switch_window_button = tk.Button(self, text="Register instead", command= lambda:controller.show_frame(Register))
        switch_window_button.pack(side="bottom", fill=tk.X)
        


class Register(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg= "#7851a9")
        
        global u_name_entry
        global pin_entry
        global open_bal_entry

        # register label
        label = tk.Label(self, text="Register Page",font=('Helvetica', 18, "bold" ))
        label.pack(padx=10, pady=10)
        
        #u_name label and input
        u_name_label = tk.Label(self, text = "Please create a username: ",bg = "#c7d3d4", fg="black")
        u_name_label.place(x = 40, y = 60)

        u_name_entry = tk.Entry(self, width = 30)
        u_name_entry.place(x = 190, y = 60)

        #pin label and input
        pin_label = tk.Label(self, text = "Please create a pin: ",bg = "#c7d3d4", fg="black")
        pin_label.place(x = 40, y = 100)
        
        pin_entry = tk.Entry(self, width = 30)
        pin_entry.place(x = 190, y = 100)
        
        #open bal label and input
        open_bal_label = tk.Label(self, text = "Deposit amount: ",bg = "#c7d3d4", fg="black")
        open_bal_label.place(x = 40, y = 140)

        

        open_bal_entry = tk.Entry(self, width = 30)
        open_bal_entry.place(x = 190, y = 140)

        #submit button
        submit_button = tk.Button(self, text = "Submit", command = lambda:self.captureData(),bg = "#c7d3d4", fg="black")
        submit_button.place(x = 40, y = 170)
        
        # go back button
        switch_window_button = tk.Button(self, text="Go Back", command= lambda:controller.show_frame(SignIn))
        switch_window_button.pack(side="bottom", fill=tk.X)

    def captureData(self):
        username = str(u_name_entry.get())
        balance = str(open_bal_entry.get())
        PINno = str(pin_entry.get())
        

        #regexuser = re.search("[A-Za-z0-9] {6,18}", username)
        #regexbalance = re.match("[0-9]", balance)
        #regexpassword = re.match("[0-9]{4,8}", PINno)

        fileobject=open("User.txt","r")
        info = fileobject.read()
        info = info.split()
        fileobject.close()
        if username in info:
            messagebox.showerror(title="error",message="Username already exists.")
            u_name_entry.focus()
        elif username.isalnum() == False or username == "" or len(username) < 6 or len(username) > 18:
            messagebox.showerror(title="error",message="Enter an alphanumeric username, between 6-18 characters.")
            u_name_entry.focus()
        elif balance.isnumeric() == False or balance == "":
            messagebox.showerror(title="error",message="Enter a numeric balance.")
            open_bal_entry.focus()
        elif PINno.isnumeric() == False or PINno == "" or len(PINno) > 8 or len(PINno) < 4:
            messagebox.showerror(title="error",message="Enter a numeric PIN Number between 4-8 characters.")
            pin_entry.focus()
        
        else:
            fileobject = open ("User.txt", "a")
            fileobject.write(username)
            fileobject.write("\n")
            fileobject.write(PINno)
            fileobject.write("\n")
            fileobject.write(str("R" + "%.2f" %  float(balance)))
            fileobject.write("\n")
            fileobject.close()
            with open("Transactions/" + username + " Transaction Log.txt", "w") as f2:
                f2.close()
            messagebox.showinfo(title="Success",message="Registration successful!.")
        


class Bank(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg= "#7851a9")
        
        global dep_bal
        global account_bal_label
    
        label = tk.Label(self, text="Welcome to the Bank" ,font=('Helvetica', 18, "bold" ))
        label.pack(padx=10, pady=10)


        view_account_label = tk.Label(self, text="Your current balance is", )
        view_account_label.place(x = 40, y = 60)

        account_bal_label = tk.Button(self,text="VIEW",command=lambda:self.viewBalance())
        account_bal_label.place(x = 190, y = 60)

        deposit_withdraw_label= tk.Label(self,text="Would you like to deposit or withdraw?")
        deposit_withdraw_label.place(x=40, y= 120)

        deposit_withdraw_button=tk.Button(self,text="click here", command=lambda:controller.show_frame(DepositAndWithdraw))
        deposit_withdraw_button.place(x=300, y=120)

       


        
        switch_window_button = tk.Button(self, text="Logout", command= lambda:controller.show_frame(SignIn))
        switch_window_button.pack(side="bottom", fill=tk.X)
        
    def viewBalance(self):
        f = open("User.txt","r")
        info = f.read()
        info = info.split()
        if retainUsername in info:
            index = info.index(retainUsername) + 2
            balanceAmount = info[index]
            account_bal_label.config(text=balanceAmount)


class DepositAndWithdraw(tk.Frame):
    def __init__(self, parent,controller):    
        tk.Frame.__init__(self, parent)
        self.configure(bg= "#7851a9")

        global amount_entry
        
        amount_label=tk.Label(self,text="Enter amount:")
        amount_label.place(x = 20, y = 60)

        amount_entry=tk.Entry(self,borderwidth="1px")
        amount_entry.place(x=200,y=60)

        deposit_button= tk.Button(self,text="deposit",command=lambda: self.depositMoney())
        deposit_button.place(x=200,y=100)

        withdraw_button=tk.Button(self,text="withdraw", command=lambda: self.withdrawMoney())
        withdraw_button.place(x=250,y=100)

        back_button=tk.Button(self,text="back to main page",command=lambda:controller.show_frame(Bank))
        back_button.pack(side="bottom", fill=tk.X)

    def depositMoney(self):
        transactionType = "Deposit"
        depositAmount = str(amount_entry.get())
        if depositAmount.isnumeric() == False:
            messagebox.showerror(title="error",message="Please enter an appropriate numeric amount.")
            amount_entry.focus()
        
        else:
            f = open("User.txt","r")
            info = f.read()
            info = info.split()
            if retainUsername in info:
                index = info.index(retainUsername) + 2
                oldAmount = info[index].replace("R","")
            accountHolder = retainUsername
            transactionNumber = str(random.randint(000000, 999999))
            f.close()
            
            newAmount = float(oldAmount) + float(depositAmount)
            f = open("User.txt", "w")
            info[index] = str("R" + "%.2f" % float(newAmount))
            info = "\n".join(info)
            f.writelines(info)
            f.close()
                
            f2 = open("Transactions/" + accountHolder + " Transaction Log.txt", "r")
            info2 = f2.read()
            f2.seek(0)
            f2.close()              
                      
            f2 = open("Transactions/" + accountHolder + " Transaction Log.txt", "a+")
            if len(info2) > 0 :
                f2.write("\n" + "\n")
            log_string = str("Transaction Type: " + str(transactionType) + "\n" + "Transaction Number: " + str(transactionNumber) + "\n" + "Account Owner: " + str(accountHolder) + "\n" + "Date of Transaction: " + str(datetime_object) + "\n" + "Previous Amount: R" + "%.2f" % float(oldAmount) + "\n" + "Deposited Amount: R" + "%.2f" % float(depositAmount) + "\n" + "New Amount: R" + "%.2f" % float(newAmount))
            f2.write(str(log_string))
            f2.close()
            messagebox.showinfo(title="Welcome",message="Deposit successful, check balance and transactions for updated details.")
        

    def withdrawMoney(self):
        transactionType = "Withdrawal"
        withdrawAmount = str(amount_entry.get())
        if withdrawAmount.isnumeric() == False:
            messagebox.showerror(title="error",message="Please enter an appropriate numeric amount.")
            amount_entry.focus()

        else:

            f = open("User.txt","r")
            info = f.read()
            info = info.split()
            if retainUsername in info:
                index = info.index(retainUsername) + 2
                oldAmount = info[index].replace("R","")
            if float(withdrawAmount) > float(oldAmount):
                messagebox.showerror(title="error",message="Insufficient balance, please enter a sufficient balance.")
                amount_entry.focus()
            else:
                accountHolder = retainUsername
                transactionNumber = str(random.randint(000000, 999999))
                f.close()
                
                newAmount = float(oldAmount) - float(withdrawAmount)
                f = open("User.txt", "w")
                info[index] = str("R" + "%.2f" % float(newAmount))
                info = "\n".join(info)
                f.writelines(info)
                f.close()

                f2 = open("Transactions/" + accountHolder + " Transaction Log.txt", "r")
                                
                info2 = f2.read()
                f2.seek(0)
                f2.close()
                                
                f2 = open("Transactions/" + accountHolder + " Transaction Log.txt", "a+")
                if len(info2) > 0 :
                    f2.write("\n" + "\n")
                log_string = str("Transaction Type: " + str(transactionType) + "\n" + "Transaction Number: " + str(transactionNumber) + "\n" + "Account Owner: " + str(accountHolder) + "\n" + "Date of Transaction: " + str(datetime_object) + "\n" + "Previous Amount: R" + "%.2f" % float(oldAmount) + "\n" + "Withdrawal Amount: R" + "%.2f" % float(withdrawAmount) + "\n" + "New Amount: R" + "%.2f" % float(newAmount))
                f2.write(str(log_string))
                f2.close()
                messagebox.showinfo(title="Welcome",message="Withdrawal successful, check balance and transactions for updated details.")




test().mainloop()
