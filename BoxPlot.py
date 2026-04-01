import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\rittw\Downloads\python file\ddos_dataset_updated_traffic.csv")

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

numeric_df = df.select_dtypes(include=['number'])
numeric_df = numeric_df.fillna(0)

plt.figure()
numeric_df.boxplot()

plt.title("Box Plot of Dataset")
plt.xlabel("Features")
plt.ylabel("Values")

plt.show()