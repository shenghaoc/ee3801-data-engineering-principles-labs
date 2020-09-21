import sys
import pandas as pd

original_df = pd.read_csv(sys.argv[1], encoding='unicode_escape', index_col=0)

filtered_df = original_df[(original_df['Item']==sys.argv[2]) &  (original_df['Element']==sys.argv[3])]

filtered_df.to_csv(sys.argv[2] + '_' + sys.argv[3] + '.csv')
