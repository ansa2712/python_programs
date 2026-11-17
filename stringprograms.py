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

str=input("Enter the string :")
a=str.rfind("Emma")
print("Last Occurence of Emma is : ",a)