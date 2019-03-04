import tushare as ts
import pandas as pd

# script to test the basic function of tushare
def test_script():
    # try to get history data of a stock
    df = ts.get_hist_data(code='885738',start="20170501",stop="20170630",ktype="60")
    print(df.head())

