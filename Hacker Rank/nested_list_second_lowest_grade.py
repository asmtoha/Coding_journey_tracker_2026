n = int(input().strip())
students_list = []

for i in range(n):
  name = input()
  score = float(input())
  students_list.append([name,score])

scores_list = []
for i in students_list:
  scores_list.append(i[1])
# i[i] for i in students_list

unique_list = sorted(list(set(scores_list)))

second_low_scores_students = []
for i in students_list:
  if unique_list[1] == i[1]:
    second_low_scores_students.append(i[0])
# i[0] for i in students_list if unique_list[1] == i[1]    
for i in sorted(second_low_scores_students):
  print(i)