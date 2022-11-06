def solution(s):
    answer = []
    split = s[2:-2].split('},{')
    split2 = sorted([temp.split(',') for temp in split], key = lambda x : len(x))
    answer.append(int(split2[0][0]))
    for i in range(1, len(split2)):
        for j in split2[i]:
            if j not in split2[i-1]:
                answer.append(int(j))
                break
   return answer
