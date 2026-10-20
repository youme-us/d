import matplotlib.pyplot as plt

subjects = ['Python', 'DBMS', 'Java', 'Maths', 'Statistics']
marks = [85, 75, 90, 80, 70]

plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Subject Marks Pie Chart")
plt.show()

plt.bar(subjects, marks, color='skyblue')
plt.title("Subject Marks Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()