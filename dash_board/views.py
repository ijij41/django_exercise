# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.http import HttpResponse
from django.shortcuts import render

from django.http import JsonResponse

# Create your views here.
import gviz_api
# https://developers.google.com/chart/interactive/docs/dev/gviz_api_lib

def getGBarData(request):
    description = {"time": ("timeofday", "Time of Day"),
                   "motivation": ("number", "Motivation Level"),
                   "energy": ("number", "Energy Level")}
    data = [{"time": (datetime.time(8, 0, 0), "8 am"), "motivation": 1, "energy": .25},
            {"time": (datetime.time(9, 0, 0), "9 am"), "motivation": 2, "energy": .5},
            {"time": (datetime.time(10, 0, 0), "10 am"), "motivation": 3, "energy": 1},
            {"time": (datetime.time(11, 0, 0), "11 am"), "motivation": 4, "energy": 2.25},
            {"time": (datetime.time(12, 0, 0), "12 am"), "motivation": 5, "energy": 2.25},
            ]

    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)
    # print "Content-type: text/plain"
    # print data_table.ToJSon(columns_order=("time", "motivation", "energy"))

    return HttpResponse(data_table.ToJSon(columns_order=("time", "motivation", "energy")))




