import pandas as pd
bonus_df = pd.DataFrame({
    'Name': ['Bob', 'Eve', 'Charlie', 'Alice', 'David'],
    'Bonus': [1000, 2000, 3000, 4000, 5000]
})

df = df.merge(bonus_df, on='Name', how='left')
df
