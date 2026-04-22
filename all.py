import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/rittw/Downloads/company_dataset/updated_20_rows_dataset.csv")

# -------------------------------
# 1. Print first 10 Headquarters
# -------------------------------
hq_names = df['hq'].head(10)

print("Top 10 Headquarters:")
for hq in hq_names:
    print(hq)

# -------------------------------
# 2. Funnel Chart (Review-wise)
# -------------------------------
review_counts = df['review_count'].value_counts().sort_values(ascending=True)

plt.figure()
plt.barh(review_counts.index.astype(str), review_counts.values)

plt.title("Company Review-wise Funnel Chart")
plt.xlabel("Number of Companies")
plt.ylabel("Review Count")

plt.show()

# -------------------------------
# 3. Bar Chart (Year-wise)
# -------------------------------
years = df['years'].value_counts().sort_index()  # sorted for better readability

plt.figure()
plt.bar(years.index.astype(str), years.values)

plt.title("Company Year Distribution")
plt.xlabel("Years")
plt.ylabel("Number of Companies")

plt.show()

# -------------------------------
# 4. Line Chart (Rating-wise)
# -------------------------------
rating_counts = df['ratings'].value_counts().sort_index()

plt.figure()
plt.plot(rating_counts.index, rating_counts.values, marker='o')

plt.title("Company Rating-wise Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Companies")

plt.grid()

plt.show()

# -------------------------------
# 5. Pie Chart (Employee-wise)
# -------------------------------

employee_counts = df['employees'].value_counts()

plt.figure()
plt.pie(employee_counts.values, labels=employee_counts.index, autopct='%1.1f%%')

plt.title("Company-wise Employee Category Distribution")

plt.show()