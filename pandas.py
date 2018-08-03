#coding:utf-8
"""
Working with Pandas Dataframes
https://openpyxl.readthedocs.io/en/stable/pandas.html
"""

from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
wb = Workbook()
ws = wb.active

for r in dataframe_to_rows(df, index=True, header=True):
    ws.append(r)