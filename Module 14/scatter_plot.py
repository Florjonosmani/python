import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("avgQperCountry.csv")

plt.figure(figsize=(10,6))

plt.scatter(df['Mean years of schooling - 2021'], df['Average IQ'], color='purple', alpha=0.7)

plt.title('scatter Plot of Mean Years of schooling vs Average IQ')

plt.xlabel('Mean years of schooling - 2021')

plt.ylabel('Average IQ')

plt.grid(True,linestyle='--', alpha=0.7)
plt.show()