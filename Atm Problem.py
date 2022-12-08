#Project by:- A.T.M. Interface code
# Contributers to this code: 
# 68: Ajay Kadawla(12201788)
# 69: Abhay Pratap Singh(1221878)
# 70: Anuskha Singh Raghuvanshi(12201687)


import time as t

user_pin = 6969
user_balance = 9743.50
user_name = "Mr. John"
print("Welcome to your bank account", user_name, end = "\n\n")

choice = 9

while (True):
    print("\t\t0. Logout and Exit")
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Cash")
    print("\t\t3. Deposit Cash")
    print("\t\t4. Change PIN")
    print("\t\t5. Return Card")
    choice = int(input("Enter number to proceed > "))
    print("\n\n")

    if choice == 0:
        print("Exiting...")
        t.sleep(2)
        print("You have been logged out. Thank you!\n\n")
        break

    elif choice in (1,2,3,4,5):
        num_of_tries = 3
        while (num_of_tries!=0):
            input_pin = int(input("Please enter your 4-digit PIN > "))

            if input_pin == user_pin:
                print("Account auhtorized!\n\n")

                if choice == 1:
                    print("Loading Account Balance...")
                    t.sleep(5)
                    print("Your current balance is Rs.", user_balance, end = "\n\n\n")
                    if user_balance<5000:
                        print("Your account balance is lower than Minimum Balance required!!")
                    break
                elif choice == 2:
                    print("Opening Cash Withdrawal...")
                    t.sleep(5)

                    while(True):
                        withdraw_amt = float(input("Enter the withdrawal amount > "))
                        if user_balance<5000:
                            print("Your account balance is lower than Minimum Balance required!!")
                            break
                        if withdraw_amt>user_balance:
                            print("Can't withdraw Rs.", withdraw_amt)
                            print("Please enter a lower amount!")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            confirm = input("Confirm? Y/N > ")
                            if confirm in ('Y', 'y'):
                                user_balance-=withdraw_amt
                                print("Amount withdrawn - Rs.", withdraw_amt)
                                print("Remaining balance - Rs.", user_balance, end = "\n\n\n")
                                if user_balance<5000:
                                    print("Your account balance is less than minimum ")
                                break

                            else:
                                print("Cancelling transaction...")
                                t.sleep(1)
                                print("Transaction Cancelled!\n\n")
                                break

                    break

                elif choice == 3:
                    print("Loading Cash Deposit...")
                    t.sleep(1.5)

                    deposit_amt = float(input("Enter the amount you wish to deposit > "))
                    print("Depositing Rs.", deposit_amt)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_balance+=deposit_amt
                        print("Amount deposited - Rs.", deposit_amt)
                        print("Updated balance - Rs.", user_balance, end = "\n\n\n")
                    else:
                        print("Cancelling transaction...")
                        t.sleep(4)
                        print("Transaction Cancelled!\n\n")

                    break


                elif choice == 4:
                    print("Loading PIN Change...")
                    t.sleep(5)

                    pin_new = int(input("Enter your new PIN > "))

                    print("Changing PIN to", pin_new)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_pin = pin_new
                        t.sleep(4)
                        print("PIN changed successfully! \n\n")
                    else:
                        print("Cancelling PIN change...")
                        t.sleep(4)
                        print("Process Cancelled!\n\n")

                    break

                else:
                    print("Loading Card Return...")
                    t.sleep(5)

                    print("Returning your ATM Card")
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        print("Card returned successfully! \n\n")
                    else:
                        print("Cancelling process...")
                        t.sleep(4)
                        print("Process Cancelled!\n\n")

                    break

            else:
                num_of_tries-=1
                print("PIN incorrect! Number of tries left -", num_of_tries, end = "\n\n")

        else:
            print("Exiting...")
            t.sleep(4)
            print("You have been logged out. Thank you!\n\n")
            break


    else:
        print("Invalid input!")
        print("\t\t0. Enter 0 to Logout and Exit!")
        continue