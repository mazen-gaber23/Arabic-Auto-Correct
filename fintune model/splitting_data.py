# Important File
import pandas as pd
from sklearn.model_selection import train_test_split

INPUT_CSV = 'formatted_dataset.csv'
TRAIN_CSV = 'train_spelling_data.csv'
VALIDATION_CSV = 'validation_spelling_data.csv'
df = pd.read_csv(INPUT_CSV)
train_df, validation_df = train_test_split(df, test_size=0.1, random_state=42)
train_df.to_csv(TRAIN_CSV, index=False, encoding='utf-8')
validation_df.to_csv(VALIDATION_CSV, index=False, encoding='utf-8')
print("Done!")
