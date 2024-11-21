#loops
# Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.
even = [1, 2, 3, 4,5,6,7,8,9,10,11,13, 14,15,16, 17,19,20]
for even in range(2,21,2):
   print(even)



# Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
user_input = int(input("Enter a number greater than 10:"))
if user_input <=10:
      print("You entered anumber below 10,please try again")
elif user_input >=10:
     print("Thank you for entering correct amount")
          

# Advanced: Write a program that prints the multiplication table (from 1 to 10) for 
# numbers from 1 to 5 using nested for loops.
for i in range(1,6):
   print(f"multiplication for {i}")
   for j in range(1, 11):
    print(f"{i} x {j} = {i * j}")

# Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to 
# find the sum of all odd numbers and print the result.
numbers =[4, 7, 2, 9, 12, 15]
sum =0
for number in numbers:
    if number % 2 !=0:
     sum += number
     print(sum)




# Lists
# Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.
fruits=["mango","ovacado","berry", "jackfruit","oranges"]
for fruit in fruits:
     print(fruit)

# Intermediate: Write a function that takes a list of numbers and returns a new list
# with each number squared. Example: [1, 2, 3] should become [1, 4, 9].
def list_of_numbers():
     squared_list =[]
     numbers = [1,2,3]
    
     for num in numbers:
        squared_list.append(num**2)
     
     return squared_list
result = list_of_numbers()
print(result)
list_of_numbers()


# Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3]
# and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
first_list = [1 , 2, 3]
second_list =[4, 5, 6]
combined = [x for pair in zip(first_list, second_list) for x in pair]
print(combined)



#given a list of numbers, [3,1,4,5,9,2]
#write a python program to find and print the two largest numbers in the list without using the max() fuction
numbers = [3, 1, 4, 1, 5, 9, 2]

largest = float('-inf') 
second_largest = float('-inf')  


for num in numbers:
    if num > largest:
        second_largest = largest 
        largest = num  
    elif num > second_largest:
        second_largest = num  
print("Largest number:", largest)
print("Second largest number:", second_largest)


# Dictionaries
# Basic: Create a dictionary with three key-value pairs representing a student's 
# information: name, age, and grade. Print each key-value pair on a new line.
student_info = {
    "name": "John Doe",
    "age": 20,
    "grade": "A"}
for key, value in student_info.items():
    print(f"{key}: {value}")


# Intermediate: Write a function that takes a dictionary of people's names and 
# their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def adults(people_dict):
    return [name for name, age in people_dict.items() if age >= 21]
people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
result = adults(people)
print(result) 

# Advanced: Given a dictionary representing items in a store with their prices, 
# {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought,
# ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
fruit =["apple","banana","orange"]
fruit_prices={"apple":0.5, "banana":0.3 , "orange":0.7}
total_cost = (0.5 + 0.3 + 0.7) 
print(f"The total cost of apple, banana and orange is {total_cost}")


# Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the
# sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
sentence = ("hello world hello")
x = sentence.count("hello")
y = sentence.count("world")
print(f"hello :{x}, world:{y}")


# Object-Oriented Programming (OOP)
# Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class 
# and print its attributes.
class Car:
    def __init__(self, brand, color):
        self.brand = brand  
        self.color = color 

my_car = Car(brand="Toyota", color="Red")

print("Car brand:", my_car.brand)
print("Car color:", my_car.color)
          
          
# Intermediate: Add a method called start_engine to the Car class that prints a message saying the engine of
# the car has started. Create an instance of Car and call the method.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} has started.")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)
my_car.start_engine()
        

# Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        "Deposits the specified amount into the account."
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraws the specified amount if sufficient balance exists."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def print_balance(self):
        """Prints the current balance."""
        print(f"Account balance: ${self.balance}")
        
