# ticker_management_api.py

from openapi_server.apis.ticker_management_api_base import BaseTickerManagementApi
from openapi_server.models.ticker_output import TickerOutput
from openapi_server.models.ticker_input import TickerInput 
from fastapi import HTTPException
from sqlalchemy import Engine, create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from typing import List  # Add this line


Base = declarative_base()
class Ticker(Base):
    __tablename__ = 'tickers'
    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class TickerManagementApi(BaseTickerManagementApi):
    async def tickers_delete(
        self,
        ticker: str
    ) -> TickerOutput:
        """지정된 티커를 삭제합니다."""
        engine: Engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        ticker_to_delete = session.query(Ticker).filter_by(ticker=ticker).first()
        if ticker_to_delete:
            session.delete(ticker_to_delete)
            session.commit()
            session.close()
            return TickerOutput(tickerId=ticker_to_delete.id, ticker=ticker_to_delete.ticker, name=ticker_to_delete.name, description=ticker_to_delete.description)
        else:
            raise HTTPException(status_code=404, detail="Ticker not found")


    async def tickers_get(
        self,
        ticker: str,
    ) -> TickerOutput:
        """지정된 티커 정보를 조회합니다."""
        engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        ticker_to_get = session.query(Ticker).filter_by(ticker=ticker).first()
        if ticker_to_get:
            session.close()
            return TickerOutput(tickerId=ticker_to_get.id, ticker=ticker_to_get.ticker, name=ticker_to_get.name, description=ticker_to_get.description)
        else:
            raise HTTPException(status_code=404, detail="Ticker not found")


    async def tickers_list_get(
        self,
    ) -> List[TickerOutput]:
        """모든 티커 목록을 조회합니다."""
        engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        tickers = session.query(Ticker).all()
        session.close()
        return [TickerOutput(tickerId=ticker.id, ticker=ticker.ticker, name=ticker.name, description=ticker.description) for ticker in tickers]


    async def tickers_post(
        self,
        ticker_input: TickerInput,
    ) -> TickerOutput:
        """새로운 티커를 추가합니다."""
        engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        new_ticker = Ticker(ticker=ticker_input.ticker, name=ticker_input.name, description=ticker_input.description)
        print(new_ticker)
        session.add(new_ticker)
        session.commit()
        session.close()
        return TickerOutput(tickerId=new_ticker.id, ticker=ticker_input.ticker, name=ticker_input.name, description=ticker_input.description)


    async def tickers_put(
        self,
        ticker_input: TickerInput,
    ) -> TickerOutput:
        """기존 티커 정보를 수정합니다."""
        engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        existing_ticker = session.query(Ticker).filter(Ticker.ticker == ticker_input.ticker).first()
        if existing_ticker:
            existing_ticker.name = ticker_input.name
            existing_ticker.description = ticker_input.description
            session.commit()
            session.refresh(existing_ticker)  # 인스턴스를 새로 고침하여 세션에 바인딩
            session.close()
            return TickerOutput(tickerId=existing_ticker.id, ticker=ticker_input.ticker, name=ticker_input.name, description=ticker_input.description)
        else:
            raise HTTPException(status_code=404, detail="티커를 찾을 수 없습니다.")
