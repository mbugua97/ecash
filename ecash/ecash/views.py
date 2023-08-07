from django.shortcuts import render,HttpResponse
from django.http import HttpResponse, JsonResponse
import requests


mdb_endpoint='https://0a48-105-161-158-238.ngrok-free.app/getdata'


def callback(request):
    try:
     data=request.body.decode('\n','')
     dbdata={"data":data}
    except:
     dbdata={"data":'message failed data from vers'}
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
