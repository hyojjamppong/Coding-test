def solution(stones, k):
answer = 0 
start, end = min(stones), max(stones)

# 이진탐색
while start <= end:
