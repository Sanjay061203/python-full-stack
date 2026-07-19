details_={"name":"rocky",
          "ATM PIN":"3530",
          "balance":500000,
          "Transaction":[]}
remaining_atmp=3
print("welcome to the ATM")
#pin=input("enter your pin:")
while remaining_atmp>0:
    pin=input("enter your pin:")
    if len(pin)==4:
        if pin==details_["ATM PIN"]:
            user_inp=int(input("enter \n1.withdraw \n2.deposit \n3.balance \n4.pin change \n5.Transaction History \nEnter your option:"))
            if user_inp==1:
                withdraw_amt=int(input("enter withdraw amount:"))
                if withdraw_amt<=details_["balance"]:
                    if withdraw_amt%100==0:
                        details_['balance']-=withdraw_amt
                        print(f"you drawed {withdraw_amt} and your balance was {details_['balance']}")
                        details_["Transaction"].append(f"withdead amount:{withdraw_amt}")
                        user_inp=int(input("\n1.home \n2.exit \nEnter your option:"))
                        if user_inp==1:
                            print("return to home")
                        if user_inp==2:
                            print("thanks for using our atm")
                            break
                    else:
                        print("atm can not dispatch change so please enter valid withdraw amount")
                        break
                else:
                    print(f"your balance was {details_['balance']}, enter less amount ")
            if user_inp==2:
                deposit_amt=int(input("enter deposit amount:"))
                if deposit_amt%100==0:
                    details_['balance']+=deposit_amt
                    print(f"your have deposited {deposit_amt} your current balace was {details_['balance']}")
                    details_["Transaction"].append(f"Deposit amount:{deposit_amt}")
                    user_inp=int(input("\n1.home \n2.exit \nEnter your option:"))
                    if user_inp==1:
                        print("entered to home page")
                    if user_inp==2:
                        ptint("thanks for using our atm")
                        break
                else:
                    print("atm can not accept change please deposit amount in 100`s")
                    break
            if user_inp==3:
                print(f"your current balance was {details_['balance']}")
                user_inp=int(input("\n1.home \n2.exit \nEnter your option:"))
                if user_inp==1:
                    print("entered to home screen")
                if user_inp==2:
                    print("thanks for using our atm")
                    break
            if user_inp==4:
                old_pin=input("enter your old pin:")
                if old_pin==details_["ATM PIN"]:
                    new_pin=input("enter new pin:")
                    if len(new_pin)==4:
                        print(f"your old pin:{details_['ATM PIN']} was changed to new pin:{new_pin}")
                        details_["ATM PIN"]=new_pin
                        user_inp=int(input("\n1.home \n2.exit \nEnter your option:"))
                        if user_inp==1:
                            print("entered to home screen")
                        if user_inp==2:
                            print("thanks for using our atm")
                            break
                    else:
                        print("invalid input,new pin should be a 4digit pin")
                        break
                else:
                    print("your old pin wont match to the existing pin")
                    break
            if user_inp==5:
                if len(details_["Transaction"])==0:
                    print("No transaction are found")
                else:
                    for i in details_["Transaction"]:
                        print(i)
        else:
            remaining_atmp-=1
            if remaining_atmp>0:
                print(f"you entered invalid pin remaining attempts are {remaining_atmp}")
            else:
                print("your card was temporarly blocked")
                break
    else:
        print("pin length is invalid")
        break
