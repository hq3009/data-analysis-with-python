# %%
import pandas as pd

# %%
yinzhou_fund = pd.read_excel('../data/yinzhou/fund.xlsx')

# %%
yinzhou_fund_equity = yinzhou_fund[~yinzhou_fund.business.str.contains("私募证券投资基金")]
yinzhou_fund_equity = yinzhou_fund_equity[yinzhou_fund_equity.full_name.str.contains("（有限合伙）")]

# %%
name_list = yinzhou_fund_equity.full_name
name_list = name_list.drop_duplicates(keep='first')