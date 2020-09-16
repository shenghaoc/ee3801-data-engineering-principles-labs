import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

fao = pd.read_csv('FAO.csv', encoding='unicode_escape')

# 1(a)
overall_annual_food_production = fao.groupby("Area").sum().astype(int)
overall_annual_food_production.to_csv('overall_annual_food_production.csv')
print()

# 1(b)
overall_food_production = overall_annual_food_production.sum(axis=1).rename('OPC')
print()

# 1(c)
average_food_production = overall_annual_food_production.mean(axis=1).astype(int).rename('APPYPC')
print()

# 1(d)
overall_food_production_sum = overall_food_production.sum()
percentage_food_production = overall_food_production.rename('GAPPC') / overall_food_production_sum
print()

# 1
overall_and_average_and_percentage_food_production = pd.concat([overall_food_production,
                                                                average_food_production,
                                                                percentage_food_production],
                                                               axis=1)
print(overall_and_average_and_percentage_food_production.head(3).append(
    overall_and_average_and_percentage_food_production.tail(3)).to_string(formatters={'GAPPC': '{:,.2%}'.format}))
print()

# 2
plt.figure()
overall_and_average_and_percentage_food_production['APPYPC'].plot(kind='bar', figsize=(30, 5),
                                                                  title='Overall production by country', legend=True)
plt.xlabel('Countries')
plt.ylabel('Food Production')
# max_val = overall_and_average_and_percentage_food_production['APPYPC'].idxmax()
# min_val = overall_and_average_and_percentage_food_production['APPYPC'].idxmin()
print()

# 3
plt.figure()
overall_and_average_and_percentage_food_production['GAPPC'].plot(kind='pie', figsize=(30, 30),
                                                                 title='Overall production by country', legend=True,
                                                                 labeldistance=None)
plt.legend(ncol=2, bbox_to_anchor=(1.05, 1))
print()

# 4
plt.figure()
percentage_food_production_simplified = overall_and_average_and_percentage_food_production['GAPPC'].copy()

sum_less_than_five_percent = percentage_food_production_simplified[percentage_food_production_simplified <= 0.05].sum()
percentage_food_production_simplified = percentage_food_production_simplified[
    percentage_food_production_simplified > 0.05].append(pd.Series([sum_less_than_five_percent], index=['Others']))

percentage_food_production_simplified.plot(kind='pie', title='Overall production by country', autopct="%.2f%%")
print()

# 5(a)
overall_annual_honey_production_2010_to_2013 = fao[fao['Item'] == 'Honey'].set_index('Area').loc[:, 'Y2010':'Y2013']
overall_annual_honey_production_2010_to_2013 = overall_annual_honey_production_2010_to_2013[
    (overall_annual_honey_production_2010_to_2013 != 0).all(1)]
print(overall_annual_honey_production_2010_to_2013.head(3).append(
    overall_annual_honey_production_2010_to_2013.tail(3)).to_string())
print()

# 5(b)
overall_honey_production_2010_to_2013 = overall_annual_honey_production_2010_to_2013.sum(1).rename('Sum Total')
overall_annual_honey_production_2010_to_2013 = pd.concat(
    [overall_annual_honey_production_2010_to_2013, overall_honey_production_2010_to_2013], axis=1)
overall_annual_honey_production_2010_to_2013.to_csv('overall_annual_honey_production_2010_to_2013.csv')
print(overall_annual_honey_production_2010_to_2013.head(3).append(
    overall_annual_honey_production_2010_to_2013.tail(3)).to_string())
print()

# 5(c)
overall_honey_production_sum_2010_to_2013 = overall_honey_production_2010_to_2013.sum()
percentage_honey_production_2010_to_2013 = overall_honey_production_2010_to_2013 \
                                           / overall_honey_production_sum_2010_to_2013

sum_less_than_five_percent_2010_to_2013 = percentage_honey_production_2010_to_2013[
    percentage_honey_production_2010_to_2013 <= 0.05].sum()
percentage_honey_production_2010_to_2013 = percentage_honey_production_2010_to_2013[
    percentage_honey_production_2010_to_2013 > 0.05].append(
    pd.Series([sum_less_than_five_percent_2010_to_2013], index=['Others']))

percentage_honey_production_2010_to_2013.plot(kind='pie', title='Overall production by country', autopct="%.2f%%",
                                              figsize=(10, 10), legend=True)
print()

# 6(a)
overall_annual_sugar_related_production_2010_to_2013 = fao.loc[:, ['Area', 'Item', 'Element', 'Y2010', 'Y2011', 'Y2012',
                                                                   'Y2013']][fao.Item.str.contains('sugar', case=False,
                                                                                                   regex=False)]

overall_annual_sugar_related_production_2010_to_2013_malaysia = overall_annual_sugar_related_production_2010_to_2013[
    overall_annual_sugar_related_production_2010_to_2013['Area'] == 'Malaysia'] \
    .groupby(['Area', 'Element'], as_index=False).sum().rename(
    columns={"Area": "Country", "Element": "Food Type"})
overall_annual_sugar_related_production_2010_to_2013_france = overall_annual_sugar_related_production_2010_to_2013[
    overall_annual_sugar_related_production_2010_to_2013['Area'] == 'France'] \
    .groupby(['Area', 'Element'], as_index=False).sum().rename(
    columns={"Area": "Country", "Element": "Food Type"})

print()

# 6(b)
overall_annual_sugar_related_production_2010_to_2013_fr_my = \
    overall_annual_sugar_related_production_2010_to_2013_malaysia \
    .append(overall_annual_sugar_related_production_2010_to_2013_france).set_index('Country')
print(overall_annual_sugar_related_production_2010_to_2013_fr_my)

# 6(c)
overall_annual_sugar_related_production_2010_to_2013_fr_my_condensed = \
    overall_annual_sugar_related_production_2010_to_2013_fr_my.groupby('Country').sum().transpose()
overall_annual_sugar_related_production_2010_to_2013_fr_my_condensed.plot(subplots=True, legend=True)

print()

# 6(d)
overall_annual_sugar_related_production_2010_to_2013_fr_my.set_index('Food Type', append=True).transpose().plot(subplots=True, legend=True)
plt.show()
print()
