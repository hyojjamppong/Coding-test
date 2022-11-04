# My solution
from collections import deque

def solution(queue1, queue2):
  lqueue = deque(queue1)
  rqueue = deque(queue2)
  lsum = sum(lqueue)
  rsum = sum(rqueue)
  
  num = 0
  
  limit = 2 * (len(queue1)+len(queue2))
  
  if (lsum + rsum) % 2 == 1:
    return -1
  
  while num < limit:
    if lsum == rsum:
      return num
    elif lsum > rsum:
      rqueue.append(lqueue.popleft())
      lsum -= lqueue.popleft()
      rsum += lqueue.popleft()
    else:
      lqueue.append(rqueue.popleft())
      rsum -= rqueue.popleft()
      lsum += rqueue.popleft()
    num += 1
 return -1 # [1, 1]	[1, 5] 이런 경우 고려


# Other Solution

from collections import deque

def solution(queue1, queue2):
    answer = 0
    target = (sum(queue1) + sum(queue2)) // 2
  
    q1 = deque(queue1)
    q2 = deque(queue2)
  
    sum_Val = sum(q1)
  
    while sum_Val != target:
    
        if sum_Val < target:
            item = q2.popleft()
            q1.append(item)
            sum_Val += item
        else:
            item = q1.popleft()
            q2.append(item)
            sum_Val -= item
        if not q2:
            return -1
        answer += 1
        
  return answer
   
        
