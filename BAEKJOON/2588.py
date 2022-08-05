# 내 풀이
a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b - ((b//100)*100))//10))
print(a*(b//100))
print((a*(b%10)) + (a*((b - ((b//100)*100))//10))*10 + (a*(b//100))*100)

# 나은 풀이
a = int(input())
b = input()
ab2 = a * int(b[2])
ab1 = a * int(b[1])
ab0 = a * int(b[0])
ab = a * int(b)

print(ab2, ab1, ab0, ab, sep='\n')
