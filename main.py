import pandas as pd

bodyfat2 = pd.read_csv('bodyfat2.csv')
bodyfat3 = pd.read_csv('bodyfat3.csv')

# 1(a)
print('1(a)')

# Select columns from neck onwards till wrist
bodyfat2_neck_to_wrist = bodyfat2.iloc[:, 5:15]

# Compute the mean, median, and sum, for each individual
bodyfat2_neck_to_wrist_mean = bodyfat2_neck_to_wrist.mean(1)
bodyfat2_neck_to_wrist_median = bodyfat2_neck_to_wrist.median(1)
bodyfat2_neck_to_wrist_sum = bodyfat2_neck_to_wrist.sum(1)

print('Top 3 mean body fat')
print(bodyfat2_neck_to_wrist_mean.head(3), '\n')
print('Bottom 3 mean body fat')
print(bodyfat2_neck_to_wrist_mean.tail(3), '\n')

print('Top 3 median body fat')
print(bodyfat2_neck_to_wrist_median.head(3), '\n')
print('Bottom 3 median body fat')
print(bodyfat2_neck_to_wrist_median.tail(3), '\n')

print('Top 3 total body fat')
print(bodyfat2_neck_to_wrist_sum.head(3), '\n')
print('Bottom 3 total body fat')
print(bodyfat2_neck_to_wrist_sum.tail(3), '\n')

# Find top 3 and bottom 3 means
bodyfat2_top_bottom_3_mean = bodyfat2_neck_to_wrist_mean.head(3) \
    .append(bodyfat2_neck_to_wrist_mean.tail(3), ignore_index=True)

# Find top 3 and bottom 3 medians
bodyfat2_top_bottom_3_median = bodyfat2_neck_to_wrist_median.head(3) \
    .append(bodyfat2_neck_to_wrist_median.tail(3), ignore_index=True)

# Find top 3 and bottom 3 sums
bodyfat2_top_bottom_3_sum = bodyfat2_neck_to_wrist_sum.head(3) \
    .append(bodyfat2_neck_to_wrist_sum.tail(3), ignore_index=True)

# Store all values obtained in a dataframe [6 rows by 3 columns]
bodyfat2_top_bottom_3 = pd.concat([bodyfat2_top_bottom_3_mean,
                                   bodyfat2_top_bottom_3_median,
                                   bodyfat2_top_bottom_3_sum], axis=1)

print()

# 1(b)
print('1(b)')
bodyfat2_means = bodyfat2.mean()
bodyfat2_medians = bodyfat2.median()
bodyfat2_sums = bodyfat2.sum()

print(bodyfat2_means)
print(bodyfat2_medians)
print(bodyfat2_sums)

print()

# 2
print('2')
bodyfat2_without_age_weight_height = bodyfat2.drop(columns=['age', 'weight', 'height'])

print(pd.concat([bodyfat2_without_age_weight_height.max(), bodyfat2_without_age_weight_height.idxmax(),
                 bodyfat2_without_age_weight_height.min(), bodyfat2_without_age_weight_height.idxmin()], axis=1)
      .set_axis(['Max value', 'Individual ID', 'Min value', 'Individual ID'], axis='columns')
      .rename_axis('Feature'))

print()

# 3
print('3')
bodyfat2_stds = bodyfat2.std()
bodyfat2_num_within_10_percent_std_of_means = bodyfat2[(bodyfat2 >= bodyfat2_means - 0.1 * bodyfat2_stds)
                                                       & (bodyfat2 <= bodyfat2_means + 0.1 * bodyfat2_stds)] \
    .count()
print(bodyfat2_num_within_10_percent_std_of_means)

bodyfat2_num_within_10_percent_std_of_medians = bodyfat2[(bodyfat2 >= bodyfat2_medians - 0.1 * bodyfat2_stds)
                                                         & (bodyfat2 <= bodyfat2_medians + 0.1 * bodyfat2_stds)] \
    .count()
print(bodyfat2_num_within_10_percent_std_of_medians)

print()

# 4
print('4')
print(pd.isna(bodyfat3).sum())

print()

# 5(a)
print('5(a)')
bodyfat3_means = bodyfat3.mean()
bodyfat3b = bodyfat3.fillna(value=bodyfat3_means)
bodyfat3b_means = bodyfat3b.mean()

print(bodyfat2_means - bodyfat3b_means)

print()

# 5(b)
print('5(b)')
bodyfat3_medians = bodyfat3.median()
bodyfat3c = bodyfat3.fillna(value=bodyfat3_medians)
bodyfat3c_medians = bodyfat3c.median()

print(bodyfat2_medians - bodyfat3c_medians)

print()

# 5(c)
print('5(c)')
print('TODO')

print()

# 6(i)
print('6(i)')
bodyfat2_normalized = (bodyfat2 - bodyfat2_means) / bodyfat2_stds
print(bodyfat2_normalized.head(3).to_string())
print(bodyfat2_normalized.tail(3).to_string())

print()

# 6(ii)
print('6(ii)')
bodyfat2_normalized_means = bodyfat2_normalized.mean()
bodyfat2_normalized_greater_than_means = bodyfat2_normalized.gt(bodyfat2_normalized_means).sum()
print(bodyfat2_normalized_greater_than_means)
