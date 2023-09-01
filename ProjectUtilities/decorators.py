import traceback
from django.shortcuts import render, redirect
from MemoyoApp.models import MyUser
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist


### check request is authenticated or not 

def is_authenticated(request):
	try:
		session_id = request.session.get('userid')
		if session_id is not None:
			user = MyUser.objects.filter(id=session_id).exists()
			print('checking user user exist or not..........', user)
			return user
		else:
			return False
	except Exception as e:
		traceback.print_exc()
		return False



def handle_page_exception(func):
	'''Function template to handle POST request and handle exceptions...'''
	def wrapper(request, *args, **kwargs):
		try:
			user = is_authenticated(request)
			if user:
				return func(request, user, *args, **kwargs)
			else:
				return redirect('/')
		except:
			traceback.print_exc()
		return HttpResponse('Something went wrong')
	return wrapper

def handle_ajax_exception(func):
	'''Function template to handle POST request and handle exceptions...'''
	def wrapper(request, *args, **kwargs):
		send_data = {'status': 0, 'msg': 'Something went wrong.'}
		try:
			if request.method == 'POST':
				return func(request, *args, **kwargs)
			else:
				send_data['msg'] = 'POST method required.'
		except ObjectDoesNotExist:
			send_data['msg'] = 'Object not found.'
		except:
			traceback.print_exc()
		return JsonResponse(send_data)
	return wrapper