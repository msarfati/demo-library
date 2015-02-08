# -*- coding: utf-8 -*-
# Demo-Library
# By Michael Sarfati (michael.sarfati@utoronto.ca), Feb 2015

from sqlalchemy.ext.declarative import declarative_base
from flask.ext.sqlalchemy import SQLAlchemy as sa

Base = declarative_base()

class Author(Base):

    __tablename__ = "author"

    id = sa.Column(sa.BigInteger, primary_key=True)
    last_name = sa.Column(sa.String)
    first_name = sa.Column(sa.String)
    birth = sa.Column(sa.Date)
    death = sa.Column(sa.Date)

    # def __repr__(self):
    #     string = ""
    #     return string.format()
