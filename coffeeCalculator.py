'''
Coffee Calculator
Shashank Narayanan

This python application will calculate the number of coffee's I can purchase in the future, when deciding to skip out on a purchase.

'''
import os



class CoffeeCalculator:
    def __init__(self):
        #This block of code will create a .txt file on the user's device. the program will read from it
        with open ("coffeeBalance.txt", 'a+') as balanceFile:
            if os.stat("coffeeBalance.txt").st_size == 0:
                balanceFile.write("0")
                print("File name 'coffeeBalance.txt' has been created. Initial value: $0")
        
        #value becomes self.__balance
        with open("coffeeBalance.txt", "r") as balanceFile:
            value= balanceFile.read()
        self.__balance = float(value)


    #Interface, shows how much the user is saving in terms of Tim Hortons coffee
    def showcase(self):
        smCoffee= round( (self.__balance / 1.80) , 2)
        mdCoffee= round( (self.__balance / 2.07) , 2)
        lrgCoffee= round( (self.__balance / 2.34) , 2)
        xlCoffee= round( (self.__balance / 2.66) , 2)

        print(f"\nSo far, you've saved: ${self.__balance: .2f}")
        print(f"Thats about:\n{smCoffee} Small coffees\n{mdCoffee} Medium coffees\n{lrgCoffee} Large coffees\n{xlCoffee} Xtra Large coffees")


    #This function will add to the users saving balance
    def addBalance(self):
        print("\nCongrats on deciding to save some money, each bit counts!")
        
        while True:
            try:
                self.__amount= float(  input("How much did you save: $")  )
                if self.__amount <= 0:
                    raise ValueError

                #confirmation
                confirm= input(f"\nYou've saved ${self.__amount}. Your current balance is: ${round(self.__balance, 2)}. \nIs this correct (Y/N): ")
                while confirm not in ["Y", "N", "y", "n", "Yes", "No", "yes", "no"]:
                    confirm= input("Incorrect input, please confirm (Y/N): ")

                #update balanceFile with the new total savings + inform user on their current total. 
                if confirm in ["Y", "y", "yes", "Yes"]:
                    total= self.__balance + self.__amount
                    with open("coffeeBalance.txt", "w+") as balanceFile:
                        balanceFile.write( str(total) )
                    self.__balance= total
                    return print(f"\nYour new balance is: ${total}", end= "")
                
                #No new changes, inform user
                else:
                    return print(f"\nSounds good, no edits have been made.", end= "")

            #User input validation (if user inputs something less than 0 or just spells it out )
            except ValueError:
                print("\nIncorrect input. Please stick to numeric values GREATER than 0.")
                continue



    #Reset user's balance file
    def resetBalance(self):
        choice= input( f"\nYour current balance is: ${self.__balance}. Would you like to reset your balance to zero?\nInput (Y/N): " )
        while choice not in ["Y", "N", "y", "n", "Yes", "No", "yes", "no"]:
                    choice= input("Incorrect input, please confirm (Y/N): ")

        if choice in ["Y", "y", "yes", "Yes"]:
            with open("coffeeBalance.txt", "w+") as balanceFile:
                balanceFile.write('0')
            self.__balance= 0
            return print(f"\nYour new balance is: $0")
        else:
            return print(f"\nSounds good, no edits have been made.", end="")
                
            

    #Handles user's menu input
    def menu(self, menuInput):
        if menuInput.lower() == "1":
            #activate the addBalance program
            self.addBalance()
            self.activate()

        elif menuInput.lower() == "2":
            #activate the removeBalance program
            self.resetBalance()
            self.activate()
        
        else:
            return print("\nThank you for stopping by. See you soon!")
            


    #acts as the operating function --> will act as the main
    def activate(self):
        self.showcase()
        menuInput= input(f"\n{'MENU':>16}\n1. Add to your stored balance\n2. Reset your balance\n3. End Program\n\nInput: ")

        #Input validation
        while menuInput not in ["1", "2", "3"]:
            menuInput= input(f"Incorrect Input. Please try again: ")
        self.menu(menuInput)
        





def main(): 
    c= CoffeeCalculator()
    c.activate()

if __name__ == "__main__":
    main()