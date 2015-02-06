# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

Base = declarative_base()

class Authors(Base):

    id = sa.Column(sa.Integer)
    last_name = sa.Column(sa.String)
    first_name = sa.Column(sa.String)
    birth = sa.Column(sa.Date)
    death = sa.Column(sa.Date)
    nationality = sa.Column(sa.String)

    # def __repr__(self):
    #     string = ""
    #     return string.format()
