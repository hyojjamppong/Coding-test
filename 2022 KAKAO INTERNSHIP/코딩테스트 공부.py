# dp[i][j] : (알고력 i, 코딩력 j) 상태에 도달하는 데 필요한 최단 시간
# (초기 알고력, 초기 코딩력) 상태에서 시작해 (목표 알고력, 목표 코딩력) 상태에 도달하는 최단 시간을 구하는 문제


def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0]
    
    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
    
    dp = [[float('inf')] * (max_alp_req + 1) for _ in range(max_cop_req + 1)]
    
    alp = min(alp, max_alp_req) # alp, cop 모두 목표값을 넘기면 안됨
    cop = min(cop, max_cop_req)
    
    dp[alp][cop] = 0 # dp[i][j]는 알고력i, 코딩력j에 도달하는데 걸리는 최소시간
    
    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            if i < max_alp_req:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < max_cop_req:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
                
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp_req)
                    new_cop = min(j + cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
     return dp[max_alp_req][max_cop_req]
                    
