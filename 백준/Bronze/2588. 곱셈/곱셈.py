# 3에는 1번에서 입력받은 값 * 2번에서 입력받은 세번째 자리수 값
# 4에는 1번에서 입력받은 값 * 2번에서 입력받은 두번째 자리수 값
# 5에는 1번에서 입력받은 값 * 2번에서 입력받은 첫번째 자리수 값
# 6에는 3+ 4*10 + 5*100

a = int(input())
b = int(input())
c = list(map(int, str(b)))

print(a * int(c[2]))
print(a * int(c[1]))
print(a * int(c[0]))
print(a * b)