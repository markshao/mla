from typing import Optional

from sqlmodel import Field, SQLModel


class StockDayTrade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ts_code: str
    trade_date: str
    open: float
    high: float
    low: float
    close: float
    pre_close: float
    change: float  # 涨跌额
    pct_chg: (
        float  # 涨跌幅 【基于除权后的昨收计算的涨跌幅：（今收-除权昨收）/除权昨收 】
    )
    vol: float  # 成交量 （手）
    amount: float  # 成交额 （千元）


class StockInfo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ts_code: str
    trade_count: int
