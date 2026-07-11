print("=== STUDENT ADMISSION & MARK ENTRY SYSTEM ===")

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\n--- Enter details for Student {i+1} ---")

    adm_no = int(input("Admission Number: "))
    name = input("Student Name: ")
    dept = input("Department: ")

    # Tuple - permanent student data
    student = (adm_no, name, dept)

    subjects = set()
    marks = {}

    print("\nEnter subjects & marks (type 'done' to finish)")

    while True:
        sub = input("Subject name: ")

        if sub.lower() == "done":
            break

        if sub in subjects:
            print("⚠ Subject already entered")
            continue

        mark = int(input(f"Mark for {sub}: "))

        subjects.add(sub)
        marks[sub] = mark

    # -------- Output --------
    print("\n===== STUDENT REPORT =====")
    print("Admission No:", student[0])
    print("Name:", student[1])
    print("Department:", student[2])

    total = 0
    print("\nMarks:")
    for s in subjects:
        print(s, ":", marks[s])
        total += marks[s]

    print("Total Marks:", total)
    print("Subjects Count:", len(subjects))

print("\n✅ All student data entered successfully")