# %%
import pandas as pd

# %%
yinzhou_fund = pd.read_excel('../data/yinzhou/yinzhou_fund_raw.xlsx')

# %%
yinzhou_fund_equity = yinzhou_fund[~yinzhou_fund.business.str.
                                   contains("私募证券投资基金")]
yinzhou_fund_equity = yinzhou_fund_equity[
    yinzhou_fund_equity.full_name.str.contains("（有限合伙）")]

yinzhou_fund_equity_survival = yinzhou_fund_equity[yinzhou_fund_equity.status
                                                   == "存续"]

# %%
name_list = yinzhou_fund_equity_survival.legal_representive
name_list_clean = name_list.drop_duplicates()
