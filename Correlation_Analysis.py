import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Tenants Feedback_1.csv')
all_columns = df.columns
question_columns = [col for col in all_columns if 'Numeric' in col]
df_selected = df[question_columns]
print("\nCorrelation Analysis:")
corr_matrix = df_selected.corr()
print(corr_matrix)
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for Question Columns')
plt.show()
