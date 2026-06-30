import pandas as pd

# Replace with your real funnel data when available.
df = pd.read_csv('funnel_dataset.csv')
df['signup_rate'] = df['signups'] / df['visitors']
df['activation_rate'] = df['activated'] / df['onboarded']
df['paid_conversion_rate'] = df['paid_users'] / df['activated']
df['m1_retention_rate'] = df['retained_m1'] / df['paid_users']
print(df[['month','signup_rate','activation_rate','paid_conversion_rate','m1_retention_rate']])
