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

overall_and_average_and_percentage_food_production['APPYPC'].plot(kind='bar', figsize=(14, 5),
                                                                  title='Overall production by country', legend=True, fontsize=6)
plt.xlabel('Countries')
plt.ylabel('Food Production')
average_food_production_max = overall_and_average_and_percentage_food_production['APPYPC'].max()
average_food_production_min = overall_and_average_and_percentage_food_production['APPYPC'].min()
print(overall_and_average_and_percentage_food_production['APPYPC'][overall_and_average_and_percentage_food_production['APPYPC'] == average_food_production_max].rename_axis('max').to_string())
print(overall_and_average_and_percentage_food_production['APPYPC'][overall_and_average_and_percentage_food_production['APPYPC'] == average_food_production_min].rename_axis('min').to_string())

print()

# 3
plt.figure(figsize=(14,14))
patches, text = plt.pie(overall_and_average_and_percentage_food_production['GAPPC'], pctdistance=None)
plt.legend(patches, 
           overall_and_average_and_percentage_food_production.index + ": " + (overall_and_average_and_percentage_food_production['GAPPC'] * 100).round(3).astype(str) + "%",
           loc="upper center", ncol=10, fontsize=5, bbox_to_anchor=(0.5, 0.1))
print()

# 4
plt.figure()
percentage_food_production_simplified = overall_and_average_and_percentage_food_production['GAPPC'].copy()

sum_less_than_five_percent = percentage_food_production_simplified[percentage_food_production_simplified <= 0.05].sum()
percentage_food_production_simplified = percentage_food_production_simplified[
    percentage_food_production_simplified > 0.05].append(pd.Series([sum_less_than_five_percent], index=['Others']))

percentage_food_production_simplified.plot(kind='pie', title='Overall production by country', autopct="%.2f%%", fontsize=6)
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
plt.figure()
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
           percentage_honey_production_2010_to_2013.index + ": " + (percentage_honey_production_2010_to_2013 * 100).round(3).astype(str) + "%",
           loc="upper center", bbox_to_anchor=(0.5, 0.1))

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
overall_annual_sugar_related_production_2010_to_2013_fr_my_condensed.plot(subplots=True, legend=True, sharex=False)

print()

# 6(d)
overall_annual_sugar_related_production_2010_to_2013_fr_my.set_index('Food Type', append=True).transpose()\
    .plot(subplots=True, legend=True, layout=(2,2), sharex=False, figsize=(8,8))
print()

# 6(e)
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
overall_annual_sugar_related_production_2012_fr_my_pct_change = \
    overall_annual_sugar_related_production_2010_to_2013_fr_my.sort_values(by=['Food Type'])['Y2012'].pct_change()
overall_annual_sugar_related_production_2012_fr_my_pct_change \
    = overall_annual_sugar_related_production_2012_fr_my_pct_change.drop(index='Malaysia')
overall_annual_sugar_related_production_2012_fr_my_pct_change.index = ['Feed', 'Food']
print(overall_annual_sugar_related_production_2012_fr_my_pct_change.to_string())

plt.show()
