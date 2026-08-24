import requests
import os
from pprint import pprint
import pandas as pd

url = "https://api.finmindtrade.com/api/v4/data?dataset=TaiwanStockInfo&data_id=2330&start_date=2026-08-19&end_date=2026-08-21"

url2 = "https://api.finmindtrade.com/api/v4/taiwan_stock_tick_snapshot?data_id=2330"

url3 = "https://api.finmindtrade.com/api/v4/data"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",    
    "Pragma": "no-cache",    
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    ),
}

#改用 json 傳入 params 參數: API條件設定
#撈取每日股價
params = {
    #dataset=TaiwanStockInfo&data_id=2330&start_date=2026-08-19&end_date=2026-08-21
    "dataset": "TaiwanStockPrice",       #資料集 from FinMind API
    "data_id": "2317",
    "start_date": "2026-08-01",        #起始日期
    "end_date": "2026-08-21"           #結束日期
}

response=requests.get(
    url3, 
    headers=headers, 
    params=params
    )

data = response.json()

#JSON → DataFrame：把 data["data"] 裡面的資料轉成 Pandas DataFrame 
df = pd.DataFrame(data["data"])

print(df)               #dataframe 內容

print("\n資料形狀:")
print(df.shape)         #(列,欄) 數量

print("\n欄位:")
print(df.columns)       #所有欄位內容

print("\n日期與收盤價:")
print(df[["date", "close"]])