import pandas as pd
import numpy as np
import os

# 1. 创建输出目录
os.makedirs("outputs", exist_ok=True)

# 2. 读取数据
data = pd.read_csv("data/raw/prices.csv", index_col="Date", parse_dates=True)
data = data.ffill().dropna()

# 3. 计算日收益率
returns = data.pct_change().dropna()

# 4. 计算年化收益 (假设一年 252 个交易日)
annual_return = returns.mean() * 252

# 5. 计算年化波动率
annual_vol = returns.std() * np.sqrt(252)

# 6. 计算夏普比率 (无风险利率假设为 0)
sharpe = annual_return / annual_vol

# 7. 计算累计收益和最大回撤
cumulative = (1 + returns).cumprod()
peak = cumulative.cummax()
drawdown = (cumulative - peak) / peak
max_drawdown = drawdown.min()

# 8. 汇总指标
metrics = pd.DataFrame({
    "Annual Return": annual_return,
    "Annual Volatility": annual_vol,
    "Sharpe Ratio": sharpe,
    "Max Drawdown": max_drawdown
})

# 9. 输出结果
metrics.to_csv("outputs/metrics.csv")
returns.to_csv("outputs/returns.csv")
cumulative.to_csv("outputs/cumulative.csv")
drawdown.to_csv("outputs/drawdown.csv")

print("=== 核心指标 ===")
print(metrics.round(4))
print("\n=== 指标已保存至 outputs/ 文件夹 ===")