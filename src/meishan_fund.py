# %%
import pandas as pd
import tushare as ts

pro = ts.pro_api('a4ac62de4c2d9beccaea931d9323e38637b5fb97e6ff24fbbd77cba6')


# %% [markdown]
# 获取沪深及科创板全部股票基本资料。然后读取梅山基金及所投上市公司excel表。以上市公司全称为基准，合并两个数据框。

# %%
company = pro.stock_basic(
    exchange='',
    list_status='L',
    fields='ts_code,name,fullname,area,industry,list_date, market')
fund = pd.read_excel('../data/meishan/fund.xlsx')
fund_company = pd.merge(company, fund, on='fullname', how='right')

# %% [markdown]
# 从合并的数据框中，提取股票代码
# %%
market_value = pro.daily_basic(
    ts_code=
    '600748.SH,603083.SH,002286.SZ,003010.SZ,003027.SZ,605183.SH,605060.SH,300971.SZ,300129.SZ,003025.SZ,002931.SZ,688550.SH,600777.SH,603855.SH,301087.SZ,600511.SH,601882.SH,688338.SH,688609.SH,300423.SZ,605007.SH,001211.SZ,688550.SH,000925.SZ,688701.SH,688191.SH,688216.SH,300750.SZ,688067.SH,300906.SZ,002962.SZ,688296.SH,301036.SZ,600721.SH,300045.SZ,688520.SH,003040.SZ,300971.SZ,300129.SZ,688388.SH,301085.SZ,301036.SZ,000035.SZ,601718.SH,300796.SZ,300894.SZ,688195.SH,688168.SH,688059.SH,002483.SZ,605001.SH,688118.SH,301051.SZ,003032.SZ,688609.SH,605266.SH,605168.SH,300905.SZ,688191.SH,688269.SH,605183.SH,300980.SZ,301025.SZ,300796.SZ,688003.SH,002464.SZ,002984.SZ,300970.SZ,300592.SZ,000859.SZ,688080.SH,600916.SH,688296.SH,688329.SH,688296.SH,688335.SH,605588.SH,300984.SZ,300796.S',
    trade_date='20211130',
    fields='ts_code,trade_date,total_mv')

market_value2 = pro.daily_basic(
    ts_code=
    '300089.SZ,603565.SH,300933.SZ,605196.SH,605189.SH,000506.SZ,605388.SH,603565.SH,002483.SZ,605177.SH,003006.SZ,601162.SH,000980.SZ,002120.SZ,688106.SH,688509.SH,300953.SZ,000035.SZ,605081.SH,688558.SH,605268.SH,688687.SH,300421.SZ,688529.SH,603633.SH,688468.SH',
    trade_date='20211130',
    fields='ts_code,trade_date,total_mv')

market_value = pd.concat([market_value, market_value2])
# %%
fund_company = pd.concat(market_value, fund_company, on='ts_code', how='right')
