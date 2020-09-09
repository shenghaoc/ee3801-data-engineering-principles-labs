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

bodyfat2_without_age_weight_height_max_min_with_id_list = []
for column in bodyfat2_without_age_weight_height:
    bodyfat2_without_age_weight_height_max_min_with_id_single_row = [bodyfat2_without_age_weight_height[column].max(),
                                                                     bodyfat2_without_age_weight_height[column].idxmax(),
                                                                     bodyfat2_without_age_weight_height[column].min(),
                                                                     bodyfat2_without_age_weight_height[column].idxmin()]

    bodyfat2_without_age_weight_height_max_min_with_id_list\
        .append(bodyfat2_without_age_weight_height_max_min_with_id_single_row)
print(pd.DataFrame(bodyfat2_without_age_weight_height_max_min_with_id_list, index=bodyfat2_without_age_weight_height.columns,
      columns=['Max value', 'Individual ID', 'Min value', 'Individual ID']).rename_axis('Feature',  axis='columns'))

print()

# 3
print('3')
bodyfat2_stds = bodyfat2.std()
bodyfat2_num_within_10_percent_std_of_means = bodyfat2[(bodyfat2 >= bodyfat2_means - 0.1 * bodyfat2_stds)
               & (bodyfat2 <= bodyfat2_means + 0.1 * bodyfat2_stds)].count()
print(bodyfat2_num_within_10_percent_std_of_means)

bodyfat2_num_within_10_percent_std_of_medians = bodyfat2[(bodyfat2 >= bodyfat2_medians - 0.1 * bodyfat2_stds)
               & (bodyfat2 <= bodyfat2_medians + 0.1 * bodyfat2_stds)].count()
print(bodyfat2_num_within_10_percent_std_of_medians)

print()

#4
print('4')
print(bodyfat3.isnull().sum())
