a = [5, 1, 4, 3]
print(sorted(a))     ##sorted
print(a)

str1 = ['aa', 'BB', 'zz', 'CC']
print(sorted(str1))             ##sorting in string
print(sorted(str1, reverse=True))

strs = ['ccc', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))   ##sorting using key

print(sorted(str1, key=str.lower))   