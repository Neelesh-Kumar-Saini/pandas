def categorize_performance(rating):
  if rating >= 4.5:
    return "Excellent"
  elif rating >= 4:
    return "Good"
  else:
    return "Average"

df["Performance"] = df["Rating"].apply(categorize_performance)
df
