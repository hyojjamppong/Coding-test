# My solution
def solution(survey, choices):
    points = [0, 0, 0, 0] # RT CF JM AN
    for i in range(len(survey)):
        if survey[i] = 'RT':
            points[0] += int(choices[i]) - 4
        elif survey[i] = 'TR':
            points[0] -= int(choices[i]) - 4
        elif survey[i] = 'CF':
            points[1] += int(choices[i]) - 4
        elif survey[i] = 'FC':
            points[1] -= int(choices[i]) - 4
        elif survey[i] = 'JM':
            points[2] += int(choices[i]) - 4
        elif survey[i] = 'MJ':
            points[2] -= int(choices[i]) - 4
        elif survey[i] = 'AN':
            points[3] += int(choices[i]) - 4
        else:
            points[3] -= int(choices[i]) - 4
    answer = ''
    if points[0] <= 0:
        answer += 'R'
    else:
        answer += 'T'
    if points[1] <= 0:
        answer += 'C'
    else:
        answer += 'F'
    if points[2] <= 0:
        answer += 'J'
    else:
        answer += 'M'
    if points[3] <= 0:
        answer += 'A'
    else:
        answer += 'N'
    return answer


# Other solution from GeonHyeock , jo_sung
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result
    
