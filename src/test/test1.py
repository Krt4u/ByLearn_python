from sqlalchemy import create_engine, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.ext.automap import automap_base
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

engine = create_engine("mysql+pymysql://pythondb:pythondb@192.168.1.18/testdb")

metadata = MetaData()
metadata.reflect(bind=engine) # 映射所有表
tables = metadata.tables # 获取映射的表
test = 

