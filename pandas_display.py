"""
Expand pandas output

Last update - 03.09.2022
"""


# for old pandas
import pandas as pd
# pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)




# for new pandas
pd.options.display.max_rows = None
pd.options.display.max_columns = None
pd.options.display.width = None
