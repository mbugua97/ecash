from django.shortcuts import render,HttpResponse
from django.http import HttpResponse, JsonResponse
import requests


mdb_endpoint='http://18cb-105-48-225-20.ngrok-free.app/getdata'


def callback(request):
    try:
     data=request.body.decode('\n','')
     dbdata={"data":data}
    except:
     dbdata={"data":'message from vers'}
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
