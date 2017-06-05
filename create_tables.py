# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

emDB_engine = create_engine("sqlite:///eastmoney.db", echo=True)

Base = declarative_base()

class StkGubaUrl(Base):
    """定义股吧表"""
    __tablename__= 'stk_guba_url'

    stk_cd = Column(String(6), primary_key=True)
    stk_name = Column(String(10))
    stk_gb_url = Column(String(100))
    stk_update_time = Column(DateTime)

    def __repr__(self):
        """规定打印对象的格式"""
        return "<stk_guba_url(code='%s',name='%s',url='%s')>"\
               % (self.stk_cd, self.stk_name, self.stk_gb_url)

Base.metadata.create_all(emDB_engine)
