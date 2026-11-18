# str=input("Enter the String: ")
# first=str[0]
# mid_len=len(str)//2
# mid=str[mid_len]
# last=str[-1]
# new_str=first+mid+last
# print("Original String: ",str)
# print("New String: ",new_str)

# mid_len=len(str)//2
# new_str=str[mid_len-1]+str[mid_len]+str[mid_len+1]
# print("Original String : ",str)
# print("New String : ",new_str)

# s1=input("Enter the 1st string : ")
# s2=input("Enter the 2nd string : ")
# mid_len=len(s1)//2
# new_str=s1[0:mid_len]+s2+s1[mid_len:]
# print("New String : ",new_str)

# mid_len1=len(s1)//2
# mid_len2=len(s2)//2
# new_str=s1[0]+s2[0]+s1[mid_len1]+s2[mid_len2]+s1[-1]+s2[-1]
# print("New String : ",new_str)

# str=input("Enter the String: ")
# rev=str[::-1]
# print("Original String : ",str)
# print("Reversed String : ",rev)

# str=input("Enter the string :")
# a=str.rfind("Emma")
# print("Last Occurence of Emma is : ",a)

# str=input("Enter the string : ")
# words=str.split("-")
# for i in words:
#     print(i)

# str=(input("Enter the string : ")).lower()
# count=str.count("usa")
# print("The count of USA : ",count)

# s1=input("Enter the first string: ")
# s2=input("Enter the second string: ")
# balanced=True
# for i in s1:
#     if i not in s2:
#         balanced=False
# print("Two Strings are Balanced? ",balanced)

# str=input("Enter the string: ").lower()
# count=0
# for i in str:
#     if i in "aeiou":
#         count+=1
# print("Count of vowels : ",count)

# str=input("Enter the URL: ")
# valid=False
# if str.startswith("https") and str.endswith(".com"):
#     valid=True
# print("Is a valid URL : ",valid)

# str=input("Enter a string: ")
# print("Original String: ",str)
# new=str.swapcase()
# print("Toggled string : ",new)

# str=input("Enter the string: ")
# new=""
# for i in str:
#     if i==" ":
#         continue
#     else:
#         new+=i
# print("Space removed : ",new)

# str=input("Enter the string : ")
# i=int(input("Enter the index number: "))
# new=str[:i]+str[i+1:]
# print("new string :",new)

# str=input("Enter the sring: ")
# new=str.partition("@")
# print(new)

# str=input("Enter the File Name: ")
# extension=str[str.rfind(".")+1:]
# print("The extension is : ",extension)

# str=input("Enter the string: ")
# lower=""
# upper=""
# for i in str:
#     if i.islower():
#         lower+=i
#     else:
#         upper+=i
# print("New string : ",lower+upper)

# str=input("Enter the string : ")
# count_char=0
# count_digit=0
# count_symbol=0
# for i in str:
#     if i.isalpha():
#         count_char+=1
#     elif i.isdigit():
#         count_digit+=1
#     else:
#         count_symbol+=1
# print("Count of Charcters: ",count_char)
# print("Count of Digits: ",count_digit)
# print("Count of SSymbols: ",count_symbol)

# s1=input("Enter the 1st string: ")
# s2=input("Enter the 2nd string: ")
# str=""
# i=0
# j=len(s2)-1
# while i>len(s1) and j<0:
#     str=str+s1[i]+s2[j]
#     i+=1
#     j-=1
# str=str+s1[i:]
# str=str+s2[:j+1]
# print("New String : ",str)

# str=input("Enter the string : ")
# total=0
# count=0
# for i in str:
#     if i.isdigit():
#         total+=int(i)
#         count+=1
# if count>0:
#     avg=total/count
#     print("Sum is : ",total)
#     print("Average is : ",avg)
# else:
#     print("No digits found")
    
# str=input("Enter the string: ")
# result={}
# for i in str:
#     if i in result:
#         result[i]+=1
#     else:
#         result[i]=1
# print(result)

# str=input("Enter the string: ")
# new=""
# for i in str:
#     if i.isalpha() or i==" ":
#         new+=i
#     else:
#         continue
# print(new)

# str_list=["Emma","Jon","","Kelly","",None,"Eric"]
# new=[]
# for i in str_list:
#     if i=="" or i is None:
#         continue
#     else:
#         new.append(i)
# print(new)

# str=input("Enter the string: ")
# new=""
# for i in str:
#     if i.isdigit():
#         new+=i
# print("new string: ",new)

# str=input("Enter the string: ")
# words=str.split()
# for i in words:
#     if i.isalpha():
#         continue
#     else:
#         print(i)

# s1=input("Enter the first string: ")
# s2=input("Enter the second string: ")
# anagram=False
# if sorted(s1)==sorted(s2):
#     anagram=True
# print("Is Anagram? ",anagram)

# s1=input("Enter the string: ")
# unique=False
# for i in s1:
#     if s1.count(i)<1:
#         unique=True
# print("Is unique: ",unique)

s1=input("Enter the string: ")
words=s1.split()
new=""
for i in words:
    new+=i.capitalize()+" "
print(new)
    