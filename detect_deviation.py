import tushare as ts
import pandas as pd

# script to test the basic function of tushare
def test_script():
    # try to get history data of a stock
    #df = ts.get_h_data(code='000725',start="20170501",end="20170630",ktype="D")
    df = ts.get_hist_data(code="000725",ktype="60")
    print(df.head())
    print("content of df:")
    print(df)
test_script()
