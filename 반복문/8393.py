n = int(input())
sum = 0

if 1 <= n <= 10000:
  for i in range(1, n+1):
    sum = sum + i
  print(sum)