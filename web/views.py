
import json

from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
            response['name'] = list_user[0].user_name
            response['email'] = list_user[0].user_email
            response['phone'] = list_user[0].user_phone
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

@require_http_methods(["GET"])
def get_users(request):
    response = {}
    try:
        user = User.objects.values('user_email', 'user_name')
        list_user = list(user)
        response['list_user'] = list_user
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_message(request):
    response = {}
    try:
        email = request.GET.get('user_email')
        allmsg = Message.objects.filter(user_email=email)
        msg = Message.objects.filter(user_email=email, deal_flag='1')
        unmsg = Message.objects.filter(user_email=email, deal_flag='0')
        count = Message.objects.filter(user_email=email, deal_flag='0').count()
        allmsg = list(allmsg)
        msged = list(msg)
        msging = list(unmsg)
        response['msged'] = json.loads(serializers.serialize("json", msged))
        response['msging'] = json.loads(serializers.serialize("json", msging))
        response['allmsg'] = json.loads(serializers.serialize("json", allmsg))
        response['count'] = count
        response['error_num'] = 0
        response['msg'] = 'success'
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def mod_msg(request):
    response = {}
    try:
        id = request.GET.get('loginFrom[id]')
        Message.objects.filter(id=id).update(message=request.GET.get('loginFrom[message]'), msg_date=request.GET.get('loginFrom[msg_date]')
                                             , msg_remark=request.GET.get('loginFrom[msg_remark]'), deal_remark=request.GET.get('loginFrom[deal_remark]')
                                             , deal_flag=request.GET.get('loginFrom[deal_flag]'), deal_date=request.GET.get('loginFrom[deal_date]'))
        response['error_num'] = 0
        response['msg'] = 'success'
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@csrf_exempt
@require_http_methods(["POST"])
def add_msg(request):
    response = {}
    try:
        message = Message(user_email=request.POST.get('user_email'), message=request.POST.get('message'),
                          msg_date=request.POST.get('msg_date'), msg_remark=request.POST.get('msg_remark'),
                          deal_remark=request.POST.get('deal_remark'), deal_flag=request.POST.get('deal_flag'))
        print(message)
        print(message.deal_date)
        print(message.msg_date)
        message.save()
        response['error_num'] = 0
        response['msg'] = 'success'
    except  Exception as e:
        response['msg'] = str(e)
        print(e)
        response['error_num'] = 1
    return JsonResponse(response)



##电子商城

