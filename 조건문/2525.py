A, B = map(int, input().split())
C = int(input())
M = B + C

if M >= 60:
  print((A + (M // 60))% 24, M % 60)
else:
  print(A, M)