from FinMind.data import DataLoader
from config import FINMIND_TOKEN

dl = DataLoader()
dl.login_by_token(api_token=FINMIND_TOKEN)

df = dl.taiwan_stock_daily(
    stock_id="2330",
    start_date="2025-01-01",
    end_date="2025-12-31"
)

print("\n========== 台積電最新資料 ==========\n")

last = df.iloc[-1]

print(f"日期：{last['date']}")
print(f"股票：{last['stock_id']}")
print(f"開盤：{last['open']} 元")
print(f"最高：{last['max']} 元")
print(f"最低：{last['min']} 元")
print(f"收盤：{last['close']} 元")
print(f"成交量：{last['Trading_Volume']:,} 股")