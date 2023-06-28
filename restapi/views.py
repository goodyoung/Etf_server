from django.shortcuts import render
# from .serializer import EtfDetailsSerializer
from .models import EtfDetails, EtfProfitPayout
import os,json

import sqlalchemy as sqla
import pandas as pd
from django.http import JsonResponse


def Main(request):
    os.chdir("/Users/goodyoung/Desktop/대학교/Dash")
    
    with open(f'./.api_keys/secret_homedb.json') as f:
        secrets = json.loads(f.read())
        
    DB_USER, DB_PW = secrets['stockmart']['userid'], secrets['stockmart']['password']
    
    engine = sqla.create_engine(f'mysql+pymysql://{DB_USER}:{DB_PW}@220.121.140.51:3030/financedb')  

    query =  sqla.text("select d.종목코드, d.종목명,  e.지급기준일, e.`분배금(원)`, e.DC_R `분배율(%)` "\
    " from etf_details d, etf_profit_payout e "\
    " where e.종목코드=d.종목코드 "\
    " and d.PAY_CLASS='MONTLY' " \
    # " and e.지급기준일 like '2023-02%' "\
    " order by e.DC_R desc")
    result = pd.read_sql(query, con=engine).to_json(orient="records",force_ascii = False)
    parsed = json.loads(result)
    s = json.dumps(parsed,ensure_ascii=False, separators=(',', ':')) 

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