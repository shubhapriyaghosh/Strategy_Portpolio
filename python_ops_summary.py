import pandas as pd

df = pd.read_csv('sla_backlog_dataset.csv')
df['closure_rate'] = df['cases_closed'] / df['cases_received']
df['exception_rate'] = df['exceptions'] / df['cases_received']
print(df[['week','closure_rate','avg_tat_hours','sla_adherence','backlog','exception_rate']])
print('Average SLA adherence:', round(df['sla_adherence'].mean(), 2))
