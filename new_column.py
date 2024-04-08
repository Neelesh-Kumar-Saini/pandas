def categorize_age(age):
    if age < 30:
        return "Young"
    elif age < 40:
        return "Middle-aged"
    else:
        return "Senior"

df["Age_Group"] = df["Age"].apply(categorize_age)
df
