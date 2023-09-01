from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from MemoyoApp.models import *
from django.shortcuts import render
import traceback
import json
from django.template.loader import get_template, render_to_string
import random
import string
from datetime import datetime,timedelta
import base64
from django.core.files.base import ContentFile
from django.utils.html import strip_tags
from datetime import date,timedelta
import time
from django.db.models import Sum
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
import hashlib



@csrf_exempt
def Registration_Ajax(request):
    try:
        name = json.loads(request.POST.get('name'))
        email = json.loads(request.POST.get('email'))
        password = json.loads(request.POST.get('password'))
        
        if MyUser.objects.filter(email=email).exists():            
            send_data = {'status': 0,'title': 'Email Already Registered', 'msg': 'The email you entered is already registered. Please use a different email or proceed with password reset.'}
        else:
            
            obj = MyUser.objects.create(email=email, password=password)
            UserDetails.objects.create(fk_myuser=obj, name=name)
            send_data = {'status': 1, 'title': 'Congratulations!','msg': 'Your account has been successfully created. Welcome aboard!'}

    except:
        traceback.print_exc()
        send_data = {'status': 0, 'title': 'Warning!','msg': 'Something Went Wrong'}

    return JsonResponse(send_data)

@csrf_exempt 
def LoginAjax(request):
    try:
        email = json.loads(request.POST.get('email'))
        password = json.loads(request.POST.get('password'))
        user = authenticate(email=email, password=password)
        print(user, 'oooooooooooooooooooooooooo', )
        if MyUser.objects.filter(email=email, password=password).exists():
            obj = MyUser.objects.get(email=email, password=password)
            request.session['userid'] = obj.id
            send_data = {"status": 1,"msg": "User Found successfully."}
        else:
            send_data = {"status": 0, 'title':'User Not Found', "msg":"The user you are looking for does not exist. Please check the entered information."}

    except:
        traceback.print_exc()
        print(traceback.format_exc())
        send_data = {'status': 0, 'title': 'Warning!','msg': 'Something Went Wrong'}

    return JsonResponse(send_data)


@csrf_exempt
def logoutAjax(request):
    try:
        del request.session['userid']
        send_data = {'status': 1, 'msg': 'User Logout Successfully'}
    except:
        print(traceback.format_exc())
        send_data = {'status':0,'msg':'Something Went Wrong'}
    return JsonResponse(send_data)
