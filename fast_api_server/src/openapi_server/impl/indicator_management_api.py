# indicator_management_api.py

from openapi_server.apis.indicator_management_api import BaseIndicatorManagementApi
from openapi_server.models.indicator_input import IndicatorInput
from openapi_server.models.indicator_output import IndicatorOutput 
from fastapi import HTTPException
from sqlalchemy import Engine, create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session   
from datetime import datetime
from typing import List  # Add this line


Base = declarative_base()
class Indicator(Base):
    __tablename__ = 'indicators'
    id = Column(Integer, primary_key=True)
    indicator_name = Column(String(255), nullable=False)
    indicator_code = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class IndicatorCalculationApi(BaseIndicatorManagementApi):

    async def indicators_delete(
        self,
        indicator_code: str
    ) -> IndicatorOutput:
        """지정된 인디케이터를 삭제합니다."""
        engine: Engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session: Session = Session()
        indicator_to_delete: Indicator = session.query(Indicator).filter_by(indicator_code=indicator_code).first()
        if indicator_to_delete:
            session.delete(indicator_to_delete)
            session.commit()
            session.close()
            return IndicatorOutput(indicatorId=indicator_to_delete.id, indicatorName=indicator_to_delete.indicator_name, indicatorCode=indicator_to_delete.indicator_code, description=indicator_to_delete.description)
        else:
            raise HTTPException(status_code=404, detail="Indicator not found")

    async def indicators_get(
        self,
        indicator_code: str
    ) -> IndicatorOutput:
        """지정된 인디케이터 정보를 조회합니다."""
        engine: Engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session: Session = Session()
        indicator_to_get: Indicator = session.query(Indicator).filter_by(indicator_code=indicator_code).first()
        if indicator_to_get:
            session.close()
            return IndicatorOutput(indicatorId=indicator_to_get.id, indicatorName=indicator_to_get.indicator_name, indicatorCode=indicator_to_get.indicator_code, description=indicator_to_get.description)
        else:
            raise HTTPException(status_code=404, detail="Indicator not found")


    async def indicators_list_get(
        self,
    ) -> List[IndicatorOutput]:
        """모든 인디케이터 목록을 조회합니다."""
        engine: Engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session: Session = Session()
        indicators: List[Indicator] = session.query(Indicator).all()
        session.close()
        return [IndicatorOutput(indicatorId=indicator.id, indicatorName=indicator.indicator_name, indicatorCode=indicator.indicator_code, description=indicator.description) for indicator in indicators]   



    async def indicators_post(
        self,
        indicator_input: IndicatorInput,
    ) -> IndicatorOutput:
        """새로운 인디케이터를 추가합니다."""
        engine: Engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session: Session = Session()
        new_indicator = Indicator(indicator_name=indicator_input.indicator_name, indicator_code=indicator_input.indicator_code, description=indicator_input.description)
        session.add(new_indicator)
        session.commit()
        session.close()
        return IndicatorOutput(indicatorId=new_indicator.id, indicatorName=new_indicator.indicator_name, indicatorCode=new_indicator.indicator_code, description=new_indicator.description)

    async def indicators_put(
        self,
        indicator_input: IndicatorInput,
    ) -> IndicatorOutput:
        """기존 인디케이터 정보를 수정합니다."""
        engine: Engine = create_engine('mysql+pymysql://stock_user:stock1234@localhost/stock_indicator_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session: Session = Session()
        existing_indicator: Indicator = session.query(Indicator).filter(Indicator.indicator_code == indicator_input.indicator_code).first()

        print(existing_indicator)
        print(indicator_input)
        if existing_indicator:
            existing_indicator.indicator_name = indicator_input.indicator_name  
            existing_indicator.description = indicator_input.description
            session.commit()
            session.refresh(existing_indicator)  # 인스턴스를 새로 고침하여 세션에 바인딩
            session.close()
            return IndicatorOutput(
                indicatorId=existing_indicator.id,
                indicatorName=existing_indicator.indicator_name,
                indicatorCode=indicator_input.indicator_code,
                description=indicator_input.description
            )
        else:
            raise HTTPException(status_code=404, detail="Indicator not found")
 