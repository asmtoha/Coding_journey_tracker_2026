n = int(input())
student_marks = {}

for i in range(n):
    name = input("Enter student name:")
    marks_input = input("Enter marks separated by space")
    marks = list(map(int,marks_input.split()))
    student_marks [name] = marks
query_name = input()
avg = sum(student_marks[query_name])/len(student_marks[query_name])
print(f"{avg:.2f}")