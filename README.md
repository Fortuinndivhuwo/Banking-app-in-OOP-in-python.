Create a class

#Then we create instance variables for the name and balance of different users(objects)
#Then we create method for getting balance which is easy, just print(f"string with {balance}") 
#Then we create another method for depositing, which adds current balance + amount you are depositing.
#last method which withdraw money by subtracting it from balance.

#Next step we create a while loop.
#Ask user for inputs to create objects.
and an if statement to tell them enter their names with no numbers.
#Then print the operators(1.check 2.balance,3.deposit an withdraw) with number for reference 
#Tell ask user to choose which operator they want to do, by choosing the number corresponding to the printed ones.
#in another while loop check user input by using the try-except, try to change the input to int() or except an error of they enter "abc.." or 1.543.
This loop will break if the try works.
#We use if statements to know which method form the class we should use.
#If the user chooses deposit.
#We make them enter the amount they want to deposit.Then we will pass amount to the deposit method, only if its not negative,"abc..." and we will check this in a another while loop which will break if the use does what's required.
#If the user chooses withdraw.
#We make them enter an the amount the want to withdraw.Then pass it to the withdraw method, only if the amount is not negative,"abc.." and is not greater than the balance and we check this in a while loop which will break if the use does the what's required


