class Atm:

    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
    
    def balanceinquiry(self):
        new_amount = 100-amount
        print ("You withdrawed : " + str(amount) + "Your remaining balance is : " + str(new_amount))

    def main ():
        name = input("Hello! Enter your namee : ")
        print ("Hello," + name)
        cardnumber = input("Insert you card number : ")
        pin = input("Enter you pin : ")
        new_user = Atm(cardnumber,pin)

        print ("Choose your activity")
        print ("1. Balance Inquiry")
        print ("2.Cash Withdrawl")
        activity = int(input("Enter activity choice in number (1 or 2) : "))

        if (activity == 1):
            new_user.balanceinquiry()
        
        elif (activity == 2):
            new_user.cashwithdrawal(amount)

        else :
            print ("Enter a vaild number (1 or 2) : ")

if __name__ == "__main__":
    main()