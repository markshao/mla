import click
from terminal_util import progress_task
from tsclient import get_client
from utils import today,yest_n_year_day
from sqlmodel import Session
from database import get_engine
from models import StockDayTrade

@click.command()
@click.option("--tscode", default=None, help="stock code")
def load_price(tscode=None):
    ts_client = get_client()
    df = ts_client.daily(ts_code = tscode,start_date=yest_n_year_day(3),end_date=today())
    with Session(get_engine()) as session:
        def action(t):
            s = StockDayTrade(**df.loc[t].to_dict())
            session.add(s)
        progress_task("load price", df.index,action=action)
        session.commit()