student_scores = []
for _ in range(int(raw_input())):
    name = (raw_input())
    score = (float(raw_input()))
    
    student_scores.append([name, score])
    
second_lowest=sorted(list(set([x[1] for x in student_scores])))[1]
student_scores.sort(key = lambda x: x[0])
for student in student_scores:
    if student[1] == second_lowest:
        print student[0]