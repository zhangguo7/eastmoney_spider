# -*- coding:utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import datetime
emDB_engine = create_engine("sqlite:///eastmoney.db", echo=True)

# 生成一个基类
Base = declarative_base()
Session = sessionmaker(bind=emDB_engine)


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


# stk1 = StkGubaUrl(
#     stk_cd='600000',
#     stk_name='浦发银行',
#     stk_gb_url='http://guba.eastmoney.com/list,600000.html',
#     stk_update_time=datetime.datetime.now()
# )

# Base.metadata.create_all(emDB_engine)
# session = Session()
# session.add(stk1)
# session.commit()
