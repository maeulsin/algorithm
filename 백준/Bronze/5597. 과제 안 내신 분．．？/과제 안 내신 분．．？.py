all_students = [number for number in range(1, 31)]

for number in range(28):
    n = int(input())

    all_students.remove(n)

print(all_students[0])
print(all_students[1])