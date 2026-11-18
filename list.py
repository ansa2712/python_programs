# 1. Write a script to perform the following three operations on given list
# a=[10,20,30,40,50]
# print(a)
# print("Third Element in the list: ",a[2])
# print("Length of the list: ",len(a))
# empty=False
# if a==[]:
#     empty=True
# print("Is the list empty? ",empty)

# 2. Take a given list and modify it through five specific actions:
# initial_list=[100,50,400,500]
# print("Initial List : ",initial_list)
# initial_list[1]=200
# print("Updated Change: ",initial_list)
# initial_list.append(600)
# print("Updated Append: ",initial_list)
# initial_list.insert(2,300)
# print("Updated Insert: ",initial_list)
# initial_list.remove(600)
# print("Removed 600: ",initial_list)
# initial_list.pop(0)
# print("Removed Index 0: ",initial_list)

# 3. Calculate the total sum of all integers in a list and find the arithmetic mean (average).
# number=[10,20,30,40,50]
# print("List is: ",number)
# sum=sum(number)
# print("Sum : ",sum)
# avg=sum/len(number)
# print("Average : ",avg)

# 4. Find Maximum and Minimum from List
# data=[45,12,89,26,35,15,75]
# print("List : ",data)
# maximum=max(data)
# minimum=min(data)
# print("Maximum : ",maximum)
# print("Minimum : ",minimum)

# 5. Multiply every number in a list together to find the total product.
# factors=[2,3,5,7]
# a=1
# for i in factors:
#     i*=a
#     a=i
# print(a)

# 6. Given a list of integers, iterate through the items and count how many are even and how many are odd.
# numbers=[10,21,4,45,66,93,11]
# odd=0
# even=0
# for i in numbers:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("Even Numbers : ",even)
# print("Odd Numbers : ",odd)

# 7.  Take a list and reverse the order of its elements.
# list=[100,200,300,400,500]
# print("Original List: ",list)
# list.reverse()
# print("Revered List: ",list)

# 8. Sort a list of numbers in ascending order (lowest to highest).
# list=[27,36,15,43,34]
# print("Unsorted List: ",list)
# list.sort()
# print("Sorted List: ",list)

# 9. Create a copy of an existing list so that modifying the copy does not change the original.
# a=["Apple","Orange","Banana","Mango","Grapes"]
# b=a.copy()
# print("Original List : ",a)
# print("Copied List : ",b)

# 10. Merge two separate lists into a single, unified list.
# list_a=["Physics","Chemistry","Maths"]
# list_b=["Biology","English","Malayalam"]
# print("First List: ",list_a)
# print("Second List: ",list_b)
# list_a.extend(list_b)
# print("Combined List: ",list_a)

# 11. Given a List,extract a "slice" containing the middle three elements.
# list=[10,20,30,40,50,60,70,80,90,100]
# print("Original List : ",list)
# list1=[]
# mid=len(list)//2
# list1.append(list[mid-1])
# list1.append(list[mid])
# list1.append(list[mid+1])
# print("Sliced List : ",list1)

# 12. Write a script to swap the positions of two elements in a list based on their indices.
# list=[2,4,6,8,10]
# print("Original List : ",list)
# list[0],list[2]=list[2],list[0]
# print("Swapped List : ",list)

# 13. Given a "list of lists" access a specific item hidden inside the inner list
# list=[[1,2],[3,4,5],[6,7]]
# print("List of Lists : ",list)
# value=list[1][-1]
# print("Accessed number : ",value)

# 14. Write to check to see if a certain value exists within a list and print a message based on the result.
# list=["Laptop","Mouse","Monitor","Keyboard",]
# print("The given Inventory : ",list)
# tablet=False
# if "Tablet" in list:
#     tablet=True
# print("Is Tablet in the Invetory : ",tablet)

# 15. In a list of strings,identify which string has the most characters.
# list=["PHP","Exercises","Backend","Frontend","Python"]
# long=list[0]
# for i in list:
#     if len(i)>len(long):
#         long=i
# print("The string with most character is : ",long)

# 16. Given a list of numbers,create a new list where each number is replaced by its square (n2) using a single line of code
# list=[1,2,3,4,5]
# new=[]
# for i in list:
#     i=i**2
#     new.append(i)
# print("Squred List : ",new)

# 17. Find out how many times a specific value appears in a list.
# list=[10,20,30,10,30,40,10,20]
# print("The List is : ",list)
# a=int(input("Enter a number in the list : "))
# count=list.count(a)
# print(f"The count of {a} is {count}")

# 18. Delete every instance of a specific value from a list.
# list=[5,20,15,20,25,20,35]
# print("Original List : ",list)
# a=int(input("Enter an Element from the given list : "))
# for i in list:
#     if i==a:
#         list.remove(a)
# print("Deleted List : ",list)

# 19. Take a list of string that contains empty entries ("") and remove them to keep only the valid text.
# list=["Mike","","Emma","Kelly","","Brad"]
# print("Original List : ",list)
# new=[]
# for i in list:
#     if i=="":
#         continue
#     else:
#         new.append(i)
# print("Cleaned List : ",new)

# 20. Remove all duplicate values from a list while keeping only one instance of each element.
# list=[10,20,30,10,40,30,20,50,40,50]
# print("Original List : ",list)
# new=[]
# for i in list:
#     if i not in new:
#         new.append(i)
#     else:
#         continue
# print("Duplicates removed list: ",new)

# 21. Given a list of integers,use list comprehensions to create a new list thaat contains only the even numbers from the original list.
# list=[1,2,3,4,5,6,7,8,9,10]
# print("Original List : ",list)
# new=[]
# for i in list:
#     if i%2==0:
#         new.append(i)
# print("list of even numbers : ",new) 

# 22. Given two list of strings, combine them index-by-index to form a sing list of concatenated string:
# list1=["Py","is","awes"]
# list2=["thon"," ","ome"]
# new=[]
# for i in range(len(list1)):
#         new.append(list1[i]+list2[i])
# print(new)

# 23. Use the zip() function to loop through two lists at once and print their values as pairs.
# list1=[10,20,30]
# list2=[100,200,300]
# for i,j in zip(list1,list2):
#     print(i,j)

# 24. Find a specific item in a list and insert a new item immediately after it.
# list=[10,20,30,40,50]
# print("Original List : ",list)
# a=int(input("Enter where to insert the number : "))
# b=int(input("Enter the new item you want to insert : "))
# index=list.index(a)
# list.insert(index+1,b)
# print("Updated List : ",list)

# 25. Find the first occurrence of a specific value in a list and replace it with a new value.
# list=[5,10,15,20,25]
# print("Original List : ",list)
# a=int(input("Enter the element you need replace : "))
# b=int(input("Enter the replaced element : "))
# index=list.index(a)
# list[index]=b
# print("Updated list : ",list)

# 26. Write a Python function that takes a list of numbers and returns the second largest value. Ensure the function handles lists with duplicate values correctly (e.g., if the list is [10, 10, 9], the second largest is 9).
# def second_largest(a):
#     a=list(set(a))
#     a.sort()
#     return a[-2]
# num=[12,35,1,10,34,1,35]
# print("The second largest number is : ",second_largest(num))

# 27. Create a script that identifies the “Mode” of a list—the element that appears most frequently. If there is a tie, returning one of the top elements is sufficient for this exercise.

# 28. Write a function that accepts a list and an integer n, returning a new list containing every nth element from the original, starting from the first element (index 0).
# def nth_element(num,n):
#     return num[::n]
# numbers=["a","b","c","d","e","f","g","h"]
# print("list: ",numbers)
# n=int(input("Enter the limit: "))
# print("Result : ",nth_element(numbers,n))

# 29. Determine if a list reads the same forward and backward. The function should return True if it is a palindrome and False otherwise.
# def palindrome(n):
#     rev=n[::-1]
#     if rev==n:
#         return True
#     else:
#         return False
# list=[1,2,3,2,1]
# print("Is list a palindrome ? ",palindrome(list))

# 30. Given three separate lists, write a function that returns a list containing only the elements that appear in all three.
# def common(a,b,c):
#     same=set(a)&set(b)&set(c)
#     return list(same)
# list1=[1,5,10,20]
# list2=[6,7,20,80,100,10]
# list3=[3,4,15,20,30,70,80,10]
# print("Common Elements : ",common(list1,list2,list3))