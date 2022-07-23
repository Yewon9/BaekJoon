N = int(input())
count = 0
M = N

while True:
  ten = N // 10
  one = N % 10
  next = ten + one
  count += 1
  N = int(str(N % 10) + str(next % 10))

  if N == M:
    break

print(count)