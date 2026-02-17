# # Fees Details
# student_type=input("Enter the student Type:")
# if (student_type=='MSDS'):
#     tution_fee=float(input("Enter the tution fee:"))
#     bus_fee=float(input("Enter the bus fee:"))
#     total=tution_fee+bus_fee
#     print("The fees to be paid by the student is Rs.",total)
# elif (student_type=='MSH'):
#     tution_fee=float(input("Enter the tution fee:"))
#     hostel_fee=float(input("Enter the hostel fee:"))
#     total=tution_fee+hostel_fee
#     print("The fees to be paid by the student is Rs.",total)
# elif (student_type=='MGSDS'):
#     tution_fee=float(input("Enter the tution fee:"))
#     bus_fee=float(input("Enter the bus fee:"))
#     total=((150/100)*tution_fee)+bus_fee
#     print("The fees to be paid by the student is Rs.",total)
# elif (student_type=='MGSH'):
#     tution_fee=float(input("Enter the tution fee:"))
#     hostel_fee=float(input("Enter the hostel fee:"))
#     total=((150/100)*tution_fee)+bus_fee
#     print("The fees to be paid by the student is Rs.",total)

# #ATM withdraw money
# acc_balance=100000
# withdrawal_amt=int(input("Enter the withdrawal amount :"))
# if(withdrawal_amt>acc_balance):
#     print("Insufficient Balance")
# elif(withdrawal_amt>10000):
#     print("The withdrawal limit is 10000")
# else:
#     print("Transaction Completed")
#     main_balance=acc_balance-withdrawal_amt
#     print("Remaining Balance:",main_balance)

# #ATM withdrawal with PIN number
# acc_balance=100000
# PIN=1717
# Enter_pin=int(input("Enter the PIN number:"))
# def atm():
#     if(Enter_pin==PIN):
#         withdrawal_amt=int(input("Enter the withdrawal Amount:"))
#         if(withdrawal_amt>acc_balance):
#             print("Insufficient Balance")
#             print(atm())
#         elif(withdrawal_amt>10000):
#             print("The withdrawal limit is 10000")
#             print(atm())
#         elif(withdrawal_amt<=0):
#             print("Invalid amount")
#             print(atm())
            
#         else:
#             print("Transaction Completed")
#             main_balance=acc_balance-withdrawal_amt
#             print("Remaining Balance:",main_balance)
#             return 0
#     elif(Enter_pin!=PIN):
#         print("Wrong PIN ")
# atm()


# #show ticket Discount
# age=int(input("Enter the Age:"))
# time=input("Enter show time(Morning/Evening):")
# Morning=50
# Evening=0
# child=150
# adult=250
# senior=200
# if(age<5):
#     print("The ticket is free")
# elif(age>=5 and age<=17):
#     if(time=='Morning'):
#         total=child-Morning
#         print("The ticket price is Rs.",total)
#     elif(time=='Evening'):
#         total=child-Evening
#         print("The ticket price is Rs.",total)
# elif(age>=18 and age<=59):
#     if(time=='Morning'):
#         total=adult-Morning
#         print("The ticket price is Rs.",total)
#     elif(time=='Evening'):
#         total=adult-Evening
#         print("The ticket price is Rs.",total)

# elif(age>60):
#     if(time=='Morning'):
#         total=senior-Morning
#         print("The ticket price is Rs.",total-((30/100)*total))
#     elif(time=='Evening'):
#         total=senior-Evening
        

# #for loop odd numbers
# n=int(input("Enter the Limit:"))
# a=0
# for i in range (1,n):
#     if(i%2==1):
#         print(i)
#         a=a+i
# print("Sum Of odd numbers",a)

# #Even number
# n=int(input("Enter the Limit:"))
# a=0
# for i in range (1,n):
#     if(i%2==0):
#         print(i)
#         a=a+i
# print("Sum Of odd numbers",a)

# #5th table
# n=int(input("Enter the Limit:"))
# for i in range (1,n):
#     a=i*5
#     print(i," x 5 =",a)

# #mark avg
# t=int(input("Enter the MARk socred in Tamil:"))
# e=int(input("Enter the MARk socred in Engilsh:"))
# m=int(input("Enter the MARk socred in Maths:"))
# s=int(input("Enter the MARk socred in Science:"))
# ss=int(input("Enter the MARk socred in Social Science:"))
# total=t+e+m+s+ss
# avg=total/5
# print("Total:",total)
# print("Average:",avg)

# #star pattern
# n=int(input("Enter the limit:"))
# for i in range (1,n+1):
#     print("*"*i)
# 

# #reverse star
# n=int(input("Enter the limit:"))
# for i in range (n,0,-1):
#     print("*"*i)

# #
# n=int(input("enter the limit:"))
# i=1
# a=0
# while(i<=n):
#     if(i%2==0):
#         print(i)
#         a=a+i
#     i=i+1
#     
# print("Sum of even number:",a)

# #while loop
# n=int(input("enter the limit:"))
# i=1
# a=0
# while(i<=n):
#     if(i%2==1):
#         print(i)
#         a=a+i
#     i=i+1
    
# print("Sum of odd number:",a)

# n=int(input("enter the limit:"))
# i=0
# while(i<n):
#         i=i+1
#         a=i*5
#         print(i," x 5 = ",a)

# #bus seat booking
# total_seat=int(input("Enter the total number of seat:"))
# i=1
# while True:
#     if(i<=total_seat):
#         name=input("Enter the name of the passenger:")
#         print("Seat",i, "booked for ",name )
#         i=i+1
#     else:
#         print("All seats are booked")
#         break


