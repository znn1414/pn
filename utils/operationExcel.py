#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:zhaonina


import xlrd
from xlutils.copy import copy
from utils.public import *


class OperationExcel:
	def getExcel(self):
		excel = xlrd.open_workbook()


