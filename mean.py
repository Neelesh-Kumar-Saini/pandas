df.groupby('Department').agg(mean_salary=('Salary', 'mean'), mean_experience=('Experience', 'mean'))
