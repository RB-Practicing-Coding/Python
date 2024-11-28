# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------
N, M = map(int, input().split())
for i in range(N//2):
    print(('.|.'*(2*i + 1)).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N//2-1, -1, -1):
    print(('.|.'*(2*i + 1)).center(M, '-'))