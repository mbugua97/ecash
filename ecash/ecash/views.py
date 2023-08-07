from django.shortcuts import render,HttpResponse
from django.http import HttpResponse, JsonResponse
import requests


mdb_endpoint='https://0a48-105-161-158-238.ngrok-free.app/getdata'


def callback(request):
     data=request.body.decode('\n','')
     dbdata={"data":data}
      
     re=requests.post(mdb_endpoint,data=dbdata)    
     response = {
		'ResultCode': 0,
		'ResultDesc': 'Accepted'
	}
     return JsonResponse(response)
