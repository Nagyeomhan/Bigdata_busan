## 1. 필요한 패키지 import
# 기본적인 패키지
import pandas as pd
import numpy as np
import pyarrow
import time
import datetime
from time import strftime
from datetime import datetime

# MySQL 관련 패키지
import MySQLdb
import mysql.connector

# SQL Alchemy 관련 패키지 1
import sqlalchemy
from sqlalchemy import create_engine

# SQL Alchemy 관련 패키지 2
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, MetaData
from sqlalchemy import insert, update



## 2. SQLAlchemy로 DB에 접속
url = 'mysql+mysqldb://sixdogma:Poiu0987*@13.113.12.130:3306/Test'
engine = sqlalchemy.create_engine(url, encoding='utf-8', echo=True)

## 3. SQLAlchemy로 DB에서 GET
var_df = pd.read_sql('SELECT DateTime, Date, Time, Lot, pH, Temp, Voltage FROM VARIABLE', con=engine, index_col=None)
err_df = pd.read_sql('SELECT Date, FailureLot1, FailureLot2 FROM ERROR', con=engine, index_col=None)

## 4. 라벨링 과정
# 날짜 부분에서 문제가 없도록 전처리
var_df['Date'] = var_df['Date'].replace(' 0 days', '')
err_df['Date'] = err_df['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
print(var_df)
# 조건에 해당하는 행에 라벨링하는 작업(정상 로트: 0 / 불량 로트: 1)
sep = list()

for i in range(len(err_df)):
    for j in range(len(var_df)):
        if err_df['Date'][i] == var_df['Date'][j]:
            if err_df['FailureLot1'][i] == var_df['Lot'][j]:
                sep.append(1)
            elif err_df['FailureLot2'][i] == var_df['Lot'][j]:
                sep.append(1)
            else:
                sep.append(0)

var_df['sep'] = sep
print(sep)


## 5. SQLAlchemy로 DB에 PUT
# labelwork_type = {'DateTime':sqlalchemy.types.DATETIME(),
#                     'Date':sqlalchemy.types.DATE(),
#                     'Time':sqlalchemy.types.TIME(),
#                     'Lot':sqlalchemy.types.INT(),
#                     'pH':sqlalchemy.types.FLOAT(),
#                     'Temp':sqlalchemy.types.FLOAT(),
#                     'Voltage':sqlalchemy.types.FLOAT(),
#                     'sep':sqlalchemy.types.INT()
#                     }

# var_df.to_sql(name='MODEL', con=engine, if_exists='append', index=False, dtype=labelwork_type)