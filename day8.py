# # Pizza Bill Generator

# print("Pizza Categories")
# print("1.Normal")
# print("2.Delux")
# category = int(input("Enter your Choice [1 or 2]: "))

# # Base price
# if category == 1:
#     base_price = 400.0
# else:
#     base_price = 600.0

# print("\nPizza Types")
# print("1.Veg")
# print("2.Non Veg")
# ptype = int(input("Enter your Choice [1 or 2]: "))

# cheese_price = 0
# cheese = int(input("\nEnter Cheese? [1.Yes or 2.NO]: "))
# if cheese == 1:
#     cheese_price = 100.0

# topping_price = 0
# topping = int(input("Enter Topping? [1.Yes or 2.NO]: "))
# if topping == 1:
#     topping_price = 100.0

# water_price = 0
# water = int(input("\nDo you want Water Bottles? [1.Yes or 2.NO]: "))
# if water == 1:
#     bottles = int(input("How many bottles?: "))
#     water_price = bottles * 20.0   


# ketchup_price = 0
# ketchup = int(input("\nDo you want Ketchup? [1.Yes or 2.NO]: "))
# if ketchup == 1:
#     packets = int(input("How many Packets?: "))
#     ketchup_price = packets * 5.0   

# soft_drink_price = 0
# soft = int(input("\nDo you want Soft Drinks? [1.Yes or 2.NO]: "))
# if soft == 1:
#     cans = int(input("How many Cans?: "))
#     soft_drink_price = cans * 75.0   


# takeaway_charge = 0
# takeaway = int(input("\nIs it a Take Away? [1.Yes or 2.NO]: "))
# if takeaway == 1:
#     takeaway_charge = 20.0

# total_cost = (base_price + cheese_price + topping_price +
#               water_price + ketchup_price + soft_drink_price +
#               takeaway_charge)

# gst = total_cost * 0.18   
# net_amount = total_cost + gst


# print("\n------------------------------")
# print("** Pizza Bill Generator **")
# print("------------------------------")
# print(f"Base Price         = {base_price}")
# print(f"Extra Cheese       = {cheese_price}")
# print(f"Extra Toppings     = {topping_price}")
# print(f"Water Bottle       = {water_price}")
# print(f"Ketchup Packets    = {ketchup_price}")
# print(f"Soft Drinks        = {soft_drink_price}")
# print(f"Take Away Charges  = {takeaway_charge}")
# print("------------------------------")
# print(f"Total Cost         = {total_cost}")
# print(f"GST Charges (18%)  = {gst}")
# print("------------------------------")
# print(f"Net Amount Payable = {net_amount}")

#Stack -->LIFO or FILO
#operation
#PUSH-->insert
#POP-->delete
#peek-->view top item

#isEmpty-check stack empty
#size-number of item

#PUSH-add an item from top
#create empty stack
#input value
#add value to the stack
#print the stack

#pseudocode
# push(data)
# if (stack is full)
#     print stack overflow
# else    
#     top++
#     stack[top or index]=data

#pop()
#if (stack is empty)
#    print stack underflow
# else    
#     top--
#     stack[top or index]=data


#peek()
#if (stack is empty)
#     print the stack underflow
# else
#     print [top of index]=data

# #code
# stack=[]
# while True:
#     print("\n 1.Push 2.Pop 3.Peek 4.display 5.exit")
#     choice=int(input("Enter the choice:"))
#     if choice==1:
#         val=int(input("Enter the value:"))
#         stack.append(val)
#         print("Pushed",val)
#     elif choice==2:
#         if not stack:
#             print("The stack is empty")
#         else:
#             print("Poped stack",stack.pop())
#     elif choice==3:
#         if not stack:
#             print("The stack is empty")
#         else:
#             print("top",stack[-1])
#     elif choice==4:
#         print("The stack is ",stack)
#     elif choice==5:
#         break
#     else:
#         print("Invalid choice")


#Queue
#1)Enqueue-add an item at rear
#2)Deqeue-remove an item at front
#front/peek


# #code
# queue=[23,34,56,78,89,90]
# while True:
#     print("\n 1.Enqueue 2.Dequeue 3.Peek 4.display 5.exit")
#     choice=int(input("Enter the choice:"))
#     if choice==1:
#         val=int(input("Enter the value:"))
#         queue.append(val)
#         print("Pushed",val)
#     elif choice==2:
#         if not queue:
#             print("The stack is empty")
#         else:
#             print("Poped stack",queue.pop())
#     elif choice==3:
#         if not queue:
#             print("The stack is empty")
#         else:
#             print("top",queue[-1])
#     elif choice==4:
#         print("The stack is ",queue)
#     elif choice==5:
#         break
#     else:
#         print("Invalid choice")

#Circular
#1)reuse,empty,space
#save memory

#if fron is free,rear can reuse it
# n=3
# queue=[None]*3
# front=0
# rear=0

# #insert
# queue[rear]=10
# rear=(rear+1)%size

# [10---------]
# [10,20------]
# [10,20,30,--]
# delete->10
# [-20,30,---]

# #Important condition
# Queue is full when(rear+1)%size==front

# queue is empty when front ==-1

# circular movements
# rear=(rear+1)%size
# front=(front+1)%size


# Psedocode
# ENQUEUE

# 1)if queue full --> print"Queue full"
# 2)if first element -> set front = 0
# 3)move rear circularly
# 4)Insert element

# DEQUEUE

# 1)if queue empty --> print"Queue empty"
# 2)remove first element 
# 3)if last element removed --> reset fron and Rear
# 4)else move front circulary


#display

#if empty--> print message
#start from the front
#prinrt until rear

#step by step logic
#Enqueue steps

#Check full condition
#set front if first insert
#move rear using modulo
#insert value

# | Type           | Insert      | Delete      | Special Feature       |
# | -------------- | ----------- | ----------- | --------------------- |
# | Simple Queue   | Rear        | Front       | FIFO                  |
# | Circular Queue | Rear        | Front       | Reuses space          |
# | Priority Queue | By priority | By priority | Important items first |
# | Deque          | Both ends   | Both ends   | Flexible              |
        


# size = int(input("Enter the size of the Queue"))
# queue = [None] * size
# front = -1
# rear = -1

# def enqueue(value):
#     global front, rear
    
#     if (rear + 1) % size == front:
#         print("Queue Full")
#         return
    
#     if front == -1:
#         front = 0
    
#     rear = (rear + 1) % size
#     queue[rear] = value
#     print(value, "inserted")

# def dequeue():
#     global front, rear
    
#     if front == -1:
#         print("Queue Empty")
#         return
    
#     removed = queue[front]
    
#     if front == rear:
#         front = rear = -1
#     else:
#         front = (front + 1) % size
    
#     print(removed, "removed")

# def display():
#     if front == -1:
#         print("Queue Empty")
#         return
    
#     i = front
#     print("Queue elements:")
    
#     while True:
#         print(queue[i], end=" ")
#         if i == rear:
#             break
#         i = (i + 1) % size
#     print()

# while True:
#     print("\n1.Enqueue 2.Dequeue 3.Display 4.Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         enqueue(value)

#     elif choice == 2:
#         dequeue()

#     elif choice == 3:
#         display()

#     elif choice == 4:
#         break

#     else:
#         print("Invalid choice")