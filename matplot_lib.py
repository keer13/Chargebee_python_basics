---Line Graph------
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


----Bar Graph------
import matplotlib.pyplot as plt
subjects = ["Python", "Java", "C++"]
marks = [90, 75, 85]
plt.bar(subjects, marks)
plt.title("Marks")
plt.show()


----pie chart------

import matplotlib.pyplot as plt
sizes = [40, 35, 25]
labels = ["Python", "Java", "C++"]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

-----Scatter Plot-----

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 7, 8, 7, 9]
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()



---Box plot----
import matplotlib.pyplot as plt
data = [12, 15, 14, 10, 18, 20, 22, 25, 30]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()
