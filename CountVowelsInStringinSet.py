s=input("Enter string")

q=list(s)
sum=0

for i in s:
    x=q.count('a')
    y=q.count('e')
    z=q.count('i')
    a=q.count('o')
    b=q.count('u')
sum=x+y+z+a+b
print(sum)

# s=raw_input("Enter string:")
# count = 0
# vowels = set("aeiou")
# for letter in s:
#     if letter in vowels:
#         count += 1
# print("Count of the vowels is:")
# print(count)

