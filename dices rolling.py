#POWERED BY||SALEH AMOO||Piπ||⚂⚃⚄⚅
print("Welcome to rolling dices app.")
import random 
a = 1 
b = 6
rolling_again = "yes"
while rolling_again == 'yes' or rolling_again == "yes":
    print('Dices rolling...')
    print(f"The value are:{random. randint(a , b)}")
    rolling_again = str(input("rolling the dices again?(yes/no):"))
while rolling_again != str and rolling_again != 'yes':
    if rolling_again == "no":
        print("Please click again.")
    #if rolling_again != str or rolling_again != 'yes':
    print("The word is out of range.")
    rolling_again = str(input("rolling the dices again?:"))
    
    if rolling_again == 'yes' :
            print('Dices rolling...')
            print(f"The value are:{random. randint(a , b)}")
            rolling_again = str(input("rolling the dices again?:"))
    if rolling_again == 'no':
        break 
        #print("The end") 
        #break