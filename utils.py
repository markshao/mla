from datetime import datetime
from dateutil.relativedelta import relativedelta


def today():
    return datetime.now().strftime("%Y%m%d")


def yest_n_year_day(n: int = 1):
    # 获取当前日期
    current_date = datetime.now()
    # 获取前两年的日期
    two_years_ago = current_date - relativedelta(years=n)
    # 格式化为 YYYYMMDD
    formatted_date = two_years_ago.strftime("%Y%m%d")
    return formatted_date
