import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]

# Bar Graph plot karein
plt.bar(categories, values, color='orange')
plt.title("Bar Graph Example")
plt.xlabel("Categories")
plt.ylabel("Values")

# Image save karein
plt.savefig("graph.png")
print("✅ Bar graph successfully 'graph.png' file mein save ho gaya hai!")
