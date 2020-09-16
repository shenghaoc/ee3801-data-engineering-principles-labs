import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.use('TkAgg')

fao = pd.read_csv('FAO.csv', encoding='unicode_escape')

# 1(a)
# Convert numbers parsed as float back to int
annual_food_production = fao.groupby('Area').sum().astype(int)
annual_food_production.to_csv('annual_food_production.csv')

# 1(b)
overall_food_production = annual_food_production.sum(axis=1).rename('OPC')

# 1(c)
average_food_production = annual_food_production.mean(axis=1).astype(int).rename('APPYPC')

# 1(d)
overall_food_production_sum = overall_food_production.sum()
# Percentage stored as decimal
percentage_food_production = overall_food_production.rename('GAPPC') / overall_food_production_sum

# 1
overall_and_average_and_percentage_food_production = pd.concat([overall_food_production,
                                                                average_food_production,
                                                                percentage_food_production],
                                                               axis=1)
print('Question 1')
print('First and last three examples of\noverall production by a country (OPC), \nAverage Production per year by each '
      'country (APPYPC) and\nGlobal Average Production by each country (GAPPC)\n')
# Use formatter to output GAPPC as percentage
print(overall_and_average_and_percentage_food_production.head(3).append(
    overall_and_average_and_percentage_food_production.tail(3)).rename_axis('Country')
      .to_string(formatters={'GAPPC': '{:,.2%}'.format}))
print()

# 2
plt.figure()

overall_and_average_and_percentage_food_production['APPYPC'].plot(kind='bar', figsize=(14, 5),
                                                                  title='Average Production per year by each country'
                                                                  ' (APPYPC)', fontsize=6)
plt.xlabel('Country')
plt.ylabel('Average Production per year')
average_food_production_max = overall_and_average_and_percentage_food_production['APPYPC'].max()
average_food_production_min = overall_and_average_and_percentage_food_production['APPYPC'].min()
print('Question 2')
print(overall_and_average_and_percentage_food_production['APPYPC'][
          overall_and_average_and_percentage_food_production['APPYPC'] == average_food_production_min].rename_axis(
    'Lowest average productions').to_string())
print(overall_and_average_and_percentage_food_production['APPYPC'][
          overall_and_average_and_percentage_food_production['APPYPC'] == average_food_production_max].rename_axis(
    'Highest average productions').to_string())

print()

# 3
plt.figure(figsize=(14, 14))
patches, text = plt.pie(overall_and_average_and_percentage_food_production['GAPPC'], pctdistance=None)
plt.legend(patches,
           overall_and_average_and_percentage_food_production.index + ': ' + (
                   overall_and_average_and_percentage_food_production['GAPPC'] * 100).round(3).astype(str) + '%',
           loc='upper center', ncol=10, fontsize=5, bbox_to_anchor=(0.5, 0.1))
plt.title('Global Average Production by each country (GAPPC), Full')
# 4
plt.figure()
percentage_food_production_simplified = overall_and_average_and_percentage_food_production['GAPPC'].copy()

sum_less_than_five_percent = percentage_food_production_simplified[percentage_food_production_simplified <= 0.05].sum()
percentage_food_production_simplified = percentage_food_production_simplified[
    percentage_food_production_simplified > 0.05].append(pd.Series([sum_less_than_five_percent], index=['Others']))

percentage_food_production_simplified.plot(kind='pie', title='Global Average Production by each country (GAPPC)',
                                           autopct='%.2f%%', fontsize=6)

# 5(a)
annual_honey_production_2010_to_2013 = fao[fao['Item'] == 'Honey'].set_index('Area').loc[:, 'Y2010':'Y2013']
annual_honey_production_2010_to_2013 = annual_honey_production_2010_to_2013[
    (annual_honey_production_2010_to_2013 != 0).all(1)]
print('Question 5(a)')
print('First and last three examples of annual honey production (2010 to 2013)')
print(annual_honey_production_2010_to_2013.head(3).append(
    annual_honey_production_2010_to_2013.tail(3)).to_string())
print()

# 5(b)
overall_honey_production_2010_to_2013 = annual_honey_production_2010_to_2013.sum(1).rename('Sum Total')
annual_honey_production_2010_to_2013 = pd.concat(
    [annual_honey_production_2010_to_2013, overall_honey_production_2010_to_2013], axis=1)
annual_honey_production_2010_to_2013.to_csv('annual_honey_production_2010_to_2013.csv')
print('Question 5(b)')
print('First and last three examples of annual honey production and sum total (2010 to 2013)')
print(annual_honey_production_2010_to_2013.head(3).append(
    annual_honey_production_2010_to_2013.tail(3)).to_string())
print()

# 5(c)
plt.figure(figsize=(7, 7))
overall_honey_production_sum_2010_to_2013 = overall_honey_production_2010_to_2013.sum()
percentage_honey_production_2010_to_2013 = overall_honey_production_2010_to_2013 \
                                           / overall_honey_production_sum_2010_to_2013

sum_less_than_five_percent_2010_to_2013 = percentage_honey_production_2010_to_2013[
    percentage_honey_production_2010_to_2013 <= 0.05].sum()
percentage_honey_production_2010_to_2013 = percentage_honey_production_2010_to_2013[
    percentage_honey_production_2010_to_2013 > 0.05].append(
    pd.Series([sum_less_than_five_percent_2010_to_2013], index=['Others']))

patches, text = plt.pie(percentage_honey_production_2010_to_2013, pctdistance=None)
plt.legend(patches,
           percentage_honey_production_2010_to_2013.index + ': ' + (
                   percentage_honey_production_2010_to_2013 * 100).round(3).astype(str) + '%',
           loc='upper center', bbox_to_anchor=(0.5, 0.1))
plt.title('Countries with average honey > 5% global production (2010 to 2013)')

# 6(a)
annual_sugar_related_production_2010_to_2013 = fao.loc[:, ['Area', 'Item', 'Element', 'Y2010', 'Y2011', 'Y2012',
                                                                   'Y2013']][fao.Item.str.contains('sugar', case=False,
                                                                                                   regex=False)]

annual_sugar_related_production_2010_to_2013_malaysia = annual_sugar_related_production_2010_to_2013[
    annual_sugar_related_production_2010_to_2013['Area'] == 'Malaysia'] \
    .groupby(['Area', 'Element'], as_index=False).sum().rename(
    columns={'Area': 'Country', 'Element': 'Food Type'})
annual_sugar_related_production_2010_to_2013_france = annual_sugar_related_production_2010_to_2013[
    annual_sugar_related_production_2010_to_2013['Area'] == 'France'] \
    .groupby(['Area', 'Element'], as_index=False).sum().rename(
    columns={'Area': 'Country', 'Element': 'Food Type'})

# 6(b)
annual_sugar_related_production_2010_to_2013_fr_my = \
    annual_sugar_related_production_2010_to_2013_malaysia \
    .append(annual_sugar_related_production_2010_to_2013_france).set_index('Country')
print('Question 6(b)')
print('Annual sugar and allied sugar products production (2010 to 2013) for Malaysia and France')
print(annual_sugar_related_production_2010_to_2013_fr_my)

# 6(c)
annual_sugar_related_production_2010_to_2013_fr_my_condensed = \
    annual_sugar_related_production_2010_to_2013_fr_my.groupby('Country').sum().transpose()
annual_sugar_related_production_2010_to_2013_fr_my_condensed.plot(legend=True, sharex=False,
                                                                          figsize=(8, 8))
plt.xlabel('Year')
plt.ylabel('Production')

# 6(d)
graph = annual_sugar_related_production_2010_to_2013_fr_my.set_index('Food Type', append=True).transpose() \
    .plot(kind='bar', subplots=True, legend=True, layout=(2, 2), sharex=False, figsize=(10, 14), fontsize=5)
graph[0][0].set_xlabel('Year')
graph[0][0].set_ylabel('Production')
graph[0][1].set_xlabel('Year')
graph[0][1].set_ylabel('Production')
graph[1][0].set_xlabel('Year')
graph[1][0].set_ylabel('Production')
graph[1][1].set_xlabel('Year')
graph[1][1].set_ylabel('Production')

# 6(e)
print('Question 6(e)')
print('The general trends of falling feed production and rising food production are the same.\n'
      'However, feed production appears to be recovering, with France being ahead of Malaysia in '
      'this aspect. Feed production for France flatlined from Y2011 to Y2012, and rose from '
      'Y2012 to Y2013. On the other hand, feed production for Malaysia remained on the '
      'decline and only from Y2012 to Y2013 did the decline begin to slow noticeably.\n'
      'For France, year-on-year growth rose consistently from Y2010 to Y2013. Malaysia\'s '
      'trend was similar except for Y2012 to Y2013, when its year-on-year growth fell instead.\n'
      'Both feed production and food production are significantly higher in France than in Malaysia.'
      )
print()

# 6(f)
# Sort to separate food and feed, then use pct_change() to calculate percentage difference
annual_sugar_related_production_2012_fr_my_pct_change = \
    annual_sugar_related_production_2010_to_2013_fr_my.sort_values(by=['Food Type'])['Y2012'].pct_change()
annual_sugar_related_production_2012_fr_my_pct_change \
    = annual_sugar_related_production_2012_fr_my_pct_change.drop(index='Malaysia')
annual_sugar_related_production_2012_fr_my_pct_change.index = ['Feed', 'Food']
print('Question 6(f)')
print('In 2012, France produced 140.625% more feed and 83.707% more food than Malaysia.')
print((annual_sugar_related_production_2012_fr_my_pct_change * 100).round(3).astype(str) + '%')

plt.show()
