import matplotlib.pyplot as plt

names = ['Amit', 'Rahul', 'Priya', 'Sneha']
percentage = [80, 75, 90, 85]


plt.pie(percentage, labels=names, autopct='%1.1f%%')
plt.title("Student Percentages - Pie Chart")
plt.show()


plt.bar(names, percentage, color='green')
plt.xlabel("Student Names")
plt.ylabel("Percentage")
plt.title("Student Percentages - Bar Chart")
plt.show()