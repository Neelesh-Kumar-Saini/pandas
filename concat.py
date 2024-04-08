# Additional employee information
additional_data = {
    'Name': ['Frank', 'Grace', 'Hannah'],
    'Age': [28, 33, 37],
    'Salary': [75000, 65000, 80000],
    'Department': ['Finance', 'IT', 'HR'],
    'Start_Date': pd.to_datetime(['2017-06-10', '2018-08-25', '2019-01-15']),
    'Experience': [8, 6, 9],
    'Rating': [4.3, 4.1, 4.6]
}
additional_df = pd.DataFrame(additional_data)
combined_df = pd.concat([df, additional_df], ignore_index=True)

print(combined_df)
