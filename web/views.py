
import json

from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q

from web.models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def del_book(request):
    response = {}
    try:
        book = Book.objects.get(id=request.GET.get('id'))
        book.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def check_user(request):
    response = {}
    try:
        email = request.GET.get('user_email')
        pwd = request.GET.get('user_pwd')
        user = User.objects.filter(Q(user_email=email))
        list_user = list(user)
        if list_user[0].password == pwd:
            response['msg'] = '欢迎你 - ' + list_user[0].user_name
            response['list'] = json.loads(serializers.serialize("json", user))
            response['error_num'] = 0
        else:
            response['msg'] = 'password is worry'
            response['error_num'] = 2
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)