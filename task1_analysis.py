import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student_data.csv")

print("✅ File loaded successfully!\n")

# Display basic info
print("First 5 rows:\n", df.head())
print("\nDataset Info:\n")
df.info()

# Calculate average
print("\nAverage Math Score:", df["math_score"].mean())

# ================= VISUALIZATION =================

# Bar Chart
plt.figure()
df["math_score"].value_counts().plot(kind="bar")
plt.title("Top Math Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(df["math_score"], df["reading_score"])
plt.title("Math vs Reading Score")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.show()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()