s = input("Enter a string: ").lower()


count_vow = 0
count_cons = 0
count_dig = 0
count_special = 0

for i in s:
    if i in 'aeiou':
        count_vow += 1
    elif i.isalpha():
        count_cons += 1
    elif i.isdigit():
        count_dig += 1
    else:
        count_special += 1


print("total vowel",count_vow)
print("total consonents",count_cons)
print("total digit",count_dig)
print("total special char",count_special)