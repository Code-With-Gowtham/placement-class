#encapsulation

#1)wrap code and data
#2)Data hiding

#ATM MACHINE
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#         print("Deposit:",amount)
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             print("Withdrawal successful")
#         else:
#             print("Insufficent Balance")
#     def show_balance(self):
#         print("The bank balance:",self.__balance)
# pin=1712
# name=input("Enter your name:")
# balance=int(input("Enter your opening Balance:"))
# PIN=int(input("Enter the PIN number:"))
# s=BankAccount(name,balance)
# while True:
#     if pin==PIN:
#         print("\n 1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
#         choice=int(input("Enter your choice:"))
#         if choice==1:
#             amt=int(input("Enter the amount:"))
#             s.deposit(amt)
#         elif choice==2:
#             withdraw=int(input("Enter your withdraw amount:"))
#             s.withdraw(withdraw)
#         elif choice==3:
#             s.show_balance()
#         elif choice==4:
#             break
#     else:
#         print("Enter the valid PIN number ")
#         break

#Polymorphsim

#build in function
#len()
# print(len("HELLo"))
# print(len([1,2,3,4,5,6,7]))

# #operator polymorphism
# print(5+3)
# print("5"+"3")

# #function poiymorphism
# def add(a,b):
#     return a+b
# print(add(5,3))
# print(add('hello','world'))

# class Animal:
#     def sound(self):
#         print("The animals makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# d=Dog()
# c=Cat()
# a=Animal()

# a.sound()
# d.sound()
# c.sound()

#ATM MACHINE usin polymorphism

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#         print("Deposit:",amount)
#     def withdraw(self,amount):
#        pass
#     def show_balance(self):
#         print("The bank balance:",self.__balance)
#         return self.__balance

# class SavingsAccount(BankAccount):
#      def withdraw(self,amount):
#         if amount<=self.show_balance():
#             newbal=self.show_balance()-amount
#             print("Withdrawal (od)successful",newbal)
#         else:
#             print(" OD Insufficent Balance")
    


# class currentAccount(BankAccount):
#     def withdraw(self,amount):
#         if amount<=self.show_balance():
#             newbal=self.show_balance()-amount
#             print("Withdrawal successful",newbal)
#         else:
#             print("Insufficent Balance")
    
    
# pin=1712
# name=input("Enter your name:")
# balance=int(input("Enter your opening Balance:"))
# PIN=int(input("Enter the PIN number:"))
# print("1.savingsAccount")
# print("2.CurrentAccount")
# ch=int(input("Enter your choice:"))
# if ch==1:
#     obj=SavingsAccount(name,balance)
# elif ch==2:
#     obj=currentAccount(name,balance)
# else:
#     print("Invalid choice")

# while True:
#     if pin==PIN:
#         print("\n 1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
#         choice=int(input("Enter your choice:"))
#         if choice==1:
#             amt=int(input("Enter the amount:"))
#             obj.deposit(amt)
#         elif choice==2:
#             withdraw=int(input("Enter your withdraw amount:"))
#             obj.withdraw(withdraw)
#         elif choice==3:
#             obj.show_balance()
#         elif choice==4:
#             break
#     else:
#         print("Enter the valid PIN number ")
#         break

#Abstraction
#Hide detail
#absraction class
#absraction class -->cant'n create the object
#abraction method


# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Square(Shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side*self.side
# class Circle(Shape):
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return 3.14*self.radius*self.radius

# Square=Square(2)
# Circle=Circle(4)
# print(Square.area())
# print(Circle.area())


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposit:", amount)

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Withdrawal successful")
#         else:
#             print("Insufficient Balance")

#     def show_balance(self):
#         print("The bank balance:", self.__balance)
#         return self.__balance


# class SavingsAccount(BankAccount):
#     def withdraw(self, amount):
#         print("Savings Account Withdrawal:")
#         super().withdraw(amount)


# class CurrentAccount(BankAccount):
#     def withdraw(self, amount):
#         print("Current Account Withdrawal:")
#         super().withdraw(amount)


# pin = 1712
# name = input("Enter your name: ")
# balance = int(input("Enter your opening Balance: "))
# PIN = int(input("Enter the PIN number: "))

# print("1. SavingsAccount")
# print("2. CurrentAccount")
# ch = int(input("Enter your choice: "))

# if ch == 1:
#     obj = SavingsAccount(name, balance)
# elif ch == 2:
#     obj = CurrentAccount(name, balance)
# else:
#     print("Invalid choice")
#     exit()

# while True:
#     if pin == PIN:
#         print("\n1.Deposit  2.Withdraw  3.Check Balance  4.Exit")
#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             amt = int(input("Enter the amount: "))
#             obj.deposit(amt)

#         elif choice == 2:
#             amt = int(input("Enter your withdraw amount: "))
#             obj.withdraw(amt)

#         elif choice == 3:
#             obj.show_balance()

#         elif choice == 4:
#             print("Thank you!")
#             break
#     else:
#         print("Enter the valid PIN number")
#         break

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, number, total_seats):
        self.number = number
        self.total_seats = total_seats

    @abstractmethod
    def calculate_fare(self):
        pass

    def show_details(self):
        print("Bus Number:", self.number)
        print("Total Seats:", self.total_seats)



class LuxuryBus(Vehicle):
    def calculate_fare(self):
        return 500



class OrdinaryBus(Vehicle):
    def calculate_fare(self):
        return 200



class SeatManager:
    def __init__(self, total_seats):
        self.__total_seats = total_seats
        self.__booked = []

    def book_seat(self):
        if len(self.__booked) < self.__total_seats:
            seat_no = len(self.__booked) + 1
            self.__booked.append(seat_no)
            return seat_no
        else:
            return None

    def cancel_seat(self, seat_no):
        if seat_no in self.__booked:
            self.__booked.remove(seat_no)
            print("Seat", seat_no, "cancelled successfully.")
        else:
            print("Invalid seat number.")

    def available_seats(self):
        return self.__total_seats - len(self.__booked)



class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Passenger Name:", self.name)
        print("Passenger Age:", self.age)



class Ticket:
    def __init__(self, passenger, bus, seat, fare):
        self.passenger = passenger
        self.bus = bus
        self.seat = seat
        self.fare = fare

    def show_ticket(self):
        print("\n----- TICKET DETAILS -----")
        self.passenger.show()
        print("Bus Number:", self.bus.number)
        print("Seat Number:", self.seat)
        print("Fare:", self.fare)
        print("---------------------------")


print("1. Luxury Bus")
print("2. Ordinary Bus")

choice = int(input("Choose Bus Type: "))

if choice == 1: 
    bus = LuxuryBus("LUX123", 5)
else:
    bus = OrdinaryBus("ORD456", 5)

seat_manager = SeatManager(bus.total_seats)
tickets = []

while True:
    print("\n1. Available Seats")
    print("2. Book Seat")
    print("3. Cancel Seat")
    print("4. Show Tickets")
    print("5. Exit")

    option = int(input("Enter choice: "))

    if option == 1:
        print("Available Seats:", seat_manager.available_seats())

    elif option == 2:
        name = input("Enter Passenger Name: ")
        age = int(input("Enter Passenger Age: "))

        seat = seat_manager.book_seat()

        if seat is None:
            print("Bus is Full!")
        else:
            passenger = Passenger(name, age)
            fare = bus.calculate_fare()   # Polymorphism
            ticket = Ticket(passenger, bus, seat, fare)
            tickets.append(ticket)
            ticket.show_ticket()

    elif option == 3:
        seat_no = int(input("Enter seat number to cancel: "))
        seat_manager.cancel_seat(seat_no)

    elif option == 4:
        if not tickets:
            print("No tickets booked yet.")
        else:
            for t in tickets:
                t.show_ticket()

    elif option == 5:
        print("Thank you for using Bus Booking System!")
        break

    else:
        print("Invalid choice!")