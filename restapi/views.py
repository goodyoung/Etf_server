from django.shortcuts import render
# from .serializer import EtfDetailsSerializer
from .models import EtfDetails, EtfProfitPayout
import os,json

import sqlalchemy as sqla
import pandas as pd
from django.http import JsonResponse
from .load_to_data import JsonData

def Main(request):
    query = "select d.종목코드, d.종목명,  e.지급기준일, e.`분배금(원)`, e.DC_R `분배율(%)` \
     from etf_details d, etf_profit_payout e \
     where e.종목코드=d.종목코드 \
     and d.PAY_CLASS='MONTLY' \
     order by e.DC_R desc"
     
    a = JsonData().getData()
    s = a.getData(query = query)

    return JsonResponse({'data':s}, safe = False, json_dumps_params={'ensure_ascii': False})





## rest-api

# class EtfDetailViewSet(viewsets.ModelViewSet):
#     print(Main())
#     # data = Main()#serializers.serialize('json', Order.objects.raw(total_sales_query))
#     # q1 = EtfDetails.objects.raw('')
#     # q2 = EtfProfitPayout
#     # EtfDetails.objects.filter(pay_class = 'MONTLY').annotate(
#     raw_query = "select month from etf_profit_payout"

#     with connection.cursor() as cursor:
#         cursor.execute(raw_query)
#         row = cursor.fetchone()
#     print('asdasdasda')
#     print(row)
#     queryset = row

#     # )
#     # queryset = EtfProfitPayout.objects.raw(
#     # """
#     # select d.종목코드,d.종목명,e.지급기준일,e.'분배금(원)',e.DC_R '분배'\
#     # from etf_details d, etf_profit_payout e \
#     # where e.종목코드=d.종목코드 \
#     # and d.PAY_CLASS='MONTLY'\
#     # order by e.DC_R desc
#     # """
#     # """select 종목코드 from etf_profit_payout
#     # """
#     # )
#     # queryset = serializers.serialize('json',Main())#EtfProfitPayout.objects.all()
#     # queryset = Main()[0]
#     # serializer_class = EtfDetailsSerializer(queryset)