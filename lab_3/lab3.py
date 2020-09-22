import sys
import pandas as pd

source, item, element = sys.argv[1:]

original_df = pd.read_csv(source, encoding='unicode_escape', index_col=0)

filtered_df = original_df.query('Item==@item & Element==@element').drop(columns=['Item', 'Element'])

filtered_df.to_csv(item + '_' + element + '.csv')
