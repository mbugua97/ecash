from django.shortcuts import render,HttpResponse
from django.http import HttpResponse, JsonResponse
import requests


mdb_endpoint=' https://18cb-105-48-225-20.ngrok-free.app/getdata'


def callback(request):
    data=request.body.decode('\n','')
    dbdata={"data":data}
    if not data is None:
        try:
           re=requests.post(mdb_endpoint,data=dbdata)
        except:
            pass    
    response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}
    return JsonResponse(response)
