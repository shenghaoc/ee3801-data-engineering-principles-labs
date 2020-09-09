import pandas as pd

bodyfat2 = pd.read_csv('bodyfat2.csv')
bodyfat3 = pd.read_csv('bodyfat3.csv')

# 1(a)
print('1(a)')

# Select columns from neck onwards till wrist
bodyfat2_neck_to_wrist = bodyfat2.iloc[:, 5:15]

# Compute the mean, median, and sum, for each individual
bodyfat2_neck_to_wrist_means = bodyfat2_neck_to_wrist.mean(1)
bodyfat2_neck_to_wrist_medians = bodyfat2_neck_to_wrist.median(1)
bodyfat2_neck_to_wrist_sums = bodyfat2_neck_to_wrist.sum(1)

print('Mean body measurements for first 3 individuals')
print(bodyfat2_neck_to_wrist_means.head(3).to_string(), '\n')
print('Mean body measurements for last 3 individuals')
print(bodyfat2_neck_to_wrist_means.tail(3).to_string(), '\n')

print('Median body measurements for first 3 individuals')
print(bodyfat2_neck_to_wrist_medians.head(3).to_string(), '\n')
print('Median body measurements for last 3 individuals')
print(bodyfat2_neck_to_wrist_medians.tail(3).to_string(), '\n')

print('Sum of all measurements for first 3 individuals')
print(bodyfat2_neck_to_wrist_sums.head(3).to_string(), '\n')
print('Sum of all body measurements for last 3 individuals')
print(bodyfat2_neck_to_wrist_sums.tail(3).to_string(), '\n')

# Combine the means of the first 3 and last 3 individuals into a data frame
# and remove their individual IDs.
bodyfat2_top_bottom_3_means = bodyfat2_neck_to_wrist_means.head(3) \
    .append(bodyfat2_neck_to_wrist_means.tail(3), ignore_index=True)

# Combine the medians of the first 3 and last 3 individuals into a data frame
# and remove their individual IDs.
bodyfat2_top_bottom_3_medians = bodyfat2_neck_to_wrist_medians.head(3) \
    .append(bodyfat2_neck_to_wrist_medians.tail(3), ignore_index=True)

# Combine the sums of the first 3 and last 3 individuals into a data frame
# and remove their individual IDs.
bodyfat2_top_bottom_3_sums = bodyfat2_neck_to_wrist_sums.head(3) \
    .append(bodyfat2_neck_to_wrist_sums.tail(3), ignore_index=True)

# Combine all the 2 * 3 data frames to form the required 6 * 3 data frame
bodyfat2_top_bottom_3 = pd.concat([bodyfat2_top_bottom_3_means,
                                   bodyfat2_top_bottom_3_medians,
                                   bodyfat2_top_bottom_3_sums], axis=1)

print()

# 1(b)
print('1(b)')
# Compute and store means, medians and sums of features in bodyfat2
# and store them as Series
bodyfat2_means = bodyfat2.mean()
bodyfat2_medians = bodyfat2.median()
bodyfat2_sums = bodyfat2.sum()

# YOU DID NOT STATE ANYTHING ABOUT DATAFRAME CREATION IN THE QUESTION
print('The means of the values of each feature')
print(bodyfat2_means.to_string())
print()
print('The medians of the values of each feature')
print(bodyfat2_medians.to_string())
print()
print('The sums of the values of each feature')
print(bodyfat2_sums.to_string())

print()

# 2
print('2')
# Remove age, weight and height
bodyfat2_without_age_weight_height = bodyfat2.drop(columns=['age', 'weight', 'height'])

# Using inbuilt methods, extract max values, min values and their associated individual IDs
# for each feature, and combine them into a single 12 * 4 data frame.
print("Extreme values for all features and associated IDs for identification")
bodyfat2_features_max_and_min_values = pd.concat([bodyfat2_without_age_weight_height.max(),
                                                  bodyfat2_without_age_weight_height.idxmax(),
                                                  bodyfat2_without_age_weight_height.min(),
                                                  bodyfat2_without_age_weight_height.idxmin()], axis=1)\
    .set_axis(['Max value', 'Individual ID', 'Min value', 'Individual ID'], axis='columns').rename_axis('Feature')

print(bodyfat2_features_max_and_min_values)

print()

# 3
print('3')
bodyfat2_stds = bodyfat2.std()
print("For each feature, the more values lie within 10% of standard deviation from the centre, the closer and less "
      "spread out they are")
bodyfat2_num_within_10_percent_std_of_means = bodyfat2[(bodyfat2 >= bodyfat2_means - 0.1 * bodyfat2_stds)
                                                       & (bodyfat2 <= bodyfat2_means + 0.1 * bodyfat2_stds)] \
    .count()
print('Using mean as measure of centre')
print(bodyfat2_num_within_10_percent_std_of_means.to_string())

print()

bodyfat2_num_within_10_percent_std_of_medians = bodyfat2[(bodyfat2 >= bodyfat2_medians - 0.1 * bodyfat2_stds)
                                                         & (bodyfat2 <= bodyfat2_medians + 0.1 * bodyfat2_stds)] \
    .count()
print('Using median as measure of centre')
print(bodyfat2_num_within_10_percent_std_of_medians.to_string())

print()

# 4
print('4')
print('Number of missing values for each feature, the higher the number, the more incomplete the data for the'
      ' feature is')
print('Features with too many missing values should dropped')
print(pd.isna(bodyfat3).sum().to_string())

print()

# 5(a)
print('5(a)')
# Find means of available values
bodyfat3_means = bodyfat3.mean()
# Impute with means
bodyfat3b = bodyfat3.fillna(value=bodyfat3_means)
# Recalculate even though should be same as bodyfat3_means
bodyfat3b_means = bodyfat3b.mean()

print('Means from complete data - Means from incomplete data (imputation)')
print((bodyfat2_means - bodyfat3b_means).to_string())

print()

# 5(b)
print('5(b)')
# Find medians of available values
bodyfat3_medians = bodyfat3.median()
# Impute with medians
bodyfat3c = bodyfat3.fillna(value=bodyfat3_medians)
# Recalculate even though should be same as bodyfat3_medians
bodyfat3c_medians = bodyfat3c.median()

print('Medians from complete data - Medians from incomplete data (imputation)')
print((bodyfat2_medians - bodyfat3c_medians).to_string())

print()

# 5(c)
print('5(c)')
print('Imputation using means appears to be more accurate, closer to original results.\n'
      'Using means, only for weight was the difference greater than 1, and it was only by 0.001302.\n'
      'On the other hand, using medians, for both hip and thigh the difference exceeded 1.\n'
      'For hip and thigh, values are generally lower than weight, meaning the inaccuracy is more significant.')

print()

# 6(i)
print('6(i)')
# Apply normalisation formula
bodyfat2_normalized = (bodyfat2 - bodyfat2_means) / bodyfat2_stds
print('Normalised features for first 3 individuals')
print(bodyfat2_normalized.head(3).to_string())
print('Normalised features for last 3 individuals')
print(bodyfat2_normalized.tail(3).to_string())

print()

# 6(ii)
print('6(ii)')
bodyfat2_normalized_means = bodyfat2_normalized.mean()
bodyfat2_normalized_greater_than_means = bodyfat2_normalized.gt(bodyfat2_normalized_means).sum()
print('Number of people who are above average for the feature')
print(bodyfat2_normalized_greater_than_means.to_string())
