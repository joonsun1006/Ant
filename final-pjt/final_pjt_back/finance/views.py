from django.conf import settings
from rest_framework.decorators import api_view, authentication_classes
from django.shortcuts import  get_object_or_404
from rest_framework.response import Response
from .serializer import DepositAndSavingsSerializer
from .models import DepositAndSavings
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from accounts.models import User
import requests
import pandas as pd
import joblib
import pickle

# Create your views here.

FINLIFE_API_KEY = settings.FINLIFE_API_KEY
EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY

model_path = 'finance/mymodel.pkl'

model = joblib.load(model_path)



@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def dbupdate(request):
    #은행 예금 업데이트
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={FINLIFE_API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    result = response.get('result')
    for li in result.get('baseList'):
        save_data = {
            'dcls_month': li.get('dcls_month'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'join_member': li.get('join_member'),
            'join_way': li.get('join_way'),
            'spcl_cnd': li.get('spcl_cnd'),
            'etc_note' : li.get('etc_note'),
            'type' : 1
        }
        serializer = DepositAndSavingsSerializer(data=save_data)
        if DepositAndSavings.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
            continue
        else:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    for li in result.get('optionList'):
        save_trm = li.get('save_trm')
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            f'intr_rate_{save_trm}': li.get('intr_rate'),
            f'intr_rate2_{save_trm}': li.get('intr_rate2'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
        }
        product = DepositAndSavings.objects.get(fin_prdt_cd=save_data['fin_prdt_cd'])
        if save_trm == '6':
            product.intr_rate_6 = save_data['intr_rate_6']
            product.intr_rate2_6 = save_data['intr_rate2_6']
        elif save_trm == '12':
            product.intr_rate_12 = save_data['intr_rate_12']
            product.intr_rate2_12 = save_data['intr_rate2_12']
        elif save_trm == '24':
            product.intr_rate_24 = save_data['intr_rate_24']
            product.intr_rate2_24 = save_data['intr_rate2_24']
        elif save_trm == '36':
            product.intr_rate_36 = save_data['intr_rate_36']
            product.intr_rate2_36 = save_data['intr_rate2_36']
        product.intr_rate_type_nm = save_data['intr_rate_type_nm']
        product.save()
    # 저축은행 예금 업데이트
    for i in range(1,5):
        url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={FINLIFE_API_KEY}&topFinGrpNo=030300&pageNo={i}'
        response = requests.get(url).json()
        result = response.get('result')
        for li in result.get('baseList'):
            save_data = {
                'dcls_month': li.get('dcls_month'),
                'kor_co_nm': li.get('kor_co_nm'),
                'fin_prdt_nm': li.get('fin_prdt_nm'),
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'join_member': li.get('join_member'),
                'join_way': li.get('join_way'),
                'spcl_cnd': li.get('spcl_cnd'),
                'etc_note' : li.get('etc_note'),
                'type' : 1
            }
            serializer = DepositAndSavingsSerializer(data=save_data)
            if DepositAndSavings.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
                continue
            else:
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

        for li in result.get('optionList'):
            save_trm = li.get('save_trm')
            save_data = {
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                f'intr_rate_{save_trm}': li.get('intr_rate'),
                f'intr_rate2_{save_trm}': li.get('intr_rate2'),
                'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            }
            product = DepositAndSavings.objects.get(fin_prdt_cd=save_data['fin_prdt_cd'])
            if save_trm == '6':
                product.intr_rate_6 = save_data['intr_rate_6']
                product.intr_rate2_6 = save_data['intr_rate2_6']
            elif save_trm == '12':
                product.intr_rate_12 = save_data['intr_rate_12']
                product.intr_rate2_12 = save_data['intr_rate2_12']
            elif save_trm == '24':
                product.intr_rate_24 = save_data['intr_rate_24']
                product.intr_rate2_24 = save_data['intr_rate2_24']
            elif save_trm == '36':
                product.intr_rate_36 = save_data['intr_rate_36']
                product.intr_rate2_36 = save_data['intr_rate2_36']
            product.intr_rate_type_nm = save_data['intr_rate_type_nm']
            product.save()
    # 은행 적금 업데이트
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={FINLIFE_API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    result = response.get('result')
    for li in result.get('baseList'):
        save_data = {
            'dcls_month': li.get('dcls_month'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'join_member': li.get('join_member'),
            'join_way': li.get('join_way'),
            'spcl_cnd': li.get('spcl_cnd'),
            'etc_note' : li.get('etc_note'),
            'max_limit' : li.get('max_limit'),
            'type' : 2
        }
        serializer = DepositAndSavingsSerializer(data=save_data)
        if DepositAndSavings.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
            continue
        else:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    for li in result.get('optionList'):
        save_trm = li.get('save_trm')
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            f'intr_rate_{save_trm}': li.get('intr_rate'),
            f'intr_rate2_{save_trm}': li.get('intr_rate2'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
        }
        product = DepositAndSavings.objects.get(fin_prdt_cd=save_data['fin_prdt_cd'])
        if save_trm == '6':
            product.intr_rate_6 = save_data['intr_rate_6']
            product.intr_rate2_6 = save_data['intr_rate2_6']
        elif save_trm == '12':
            product.intr_rate_12 = save_data['intr_rate_12']
            product.intr_rate2_12 = save_data['intr_rate2_12']
        elif save_trm == '24':
            product.intr_rate_24 = save_data['intr_rate_24']
            product.intr_rate2_24 = save_data['intr_rate2_24']
        elif save_trm == '36':
            product.intr_rate_36 = save_data['intr_rate_36']
            product.intr_rate2_36 = save_data['intr_rate2_36']
        product.intr_rate_type_nm = save_data['intr_rate_type_nm']
        product.save()
    # 저축은행 적금 업데이트
    for i in range(1,4):
        url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={FINLIFE_API_KEY}&topFinGrpNo=030300&pageNo={i}'
        response = requests.get(url).json()
        result = response.get('result')
        for li in result.get('baseList'):
            save_data = {
                'dcls_month': li.get('dcls_month'),
                'kor_co_nm': li.get('kor_co_nm'),
                'fin_prdt_nm': li.get('fin_prdt_nm'),
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'join_member': li.get('join_member'),
                'join_way': li.get('join_way'),
                'spcl_cnd': li.get('spcl_cnd'),
                'etc_note' : li.get('etc_note'),
                'max_limit' : li.get('max_limit'),
                'type' : 2
            }
            serializer = DepositAndSavingsSerializer(data=save_data)
            if DepositAndSavings.objects.filter(fin_prdt_cd=save_data['fin_prdt_cd']).exists():
                continue
            else:
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

        for li in result.get('optionList'):
            save_trm = li.get('save_trm')
            save_data = {
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                f'intr_rate_{save_trm}': li.get('intr_rate'),
                f'intr_rate2_{save_trm}': li.get('intr_rate2'),
                'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            }
            product = DepositAndSavings.objects.get(fin_prdt_cd=save_data['fin_prdt_cd'])
            if save_trm == '6':
                product.intr_rate_6 = save_data['intr_rate_6']
                product.intr_rate2_6 = save_data['intr_rate2_6']
            elif save_trm == '12':
                product.intr_rate_12 = save_data['intr_rate_12']
                product.intr_rate2_12 = save_data['intr_rate2_12']
            elif save_trm == '24':
                product.intr_rate_24 = save_data['intr_rate_24']
                product.intr_rate2_24 = save_data['intr_rate2_24']
            elif save_trm == '36':
                product.intr_rate_36 = save_data['intr_rate_36']
                product.intr_rate2_36 = save_data['intr_rate2_36']
            product.intr_rate_type_nm = save_data['intr_rate_type_nm']
            product.save()
    return Response({'message':'OK'})


@api_view(['GET'])
def deposit(request):
    products = DepositAndSavings.objects.filter(type=1)
    serializer = DepositAndSavingsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def savings(request):
    products = DepositAndSavings.objects.filter(type=2)
    serializer = DepositAndSavingsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request, detail_pk):
    products = DepositAndSavings.objects.get(pk=detail_pk)
    serializer = DepositAndSavingsSerializer(products)
    return Response(serializer.data)


@api_view(['GET'])
def exchange(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={EXCHANGE_API_KEY}&searchdate=20231124&data=AP01'
    response = requests.get(url).json()
    result = {}
    for li in response:
        result[li['cur_nm']] = li['deal_bas_r']
    return Response(result)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def recommend(request):
    user = pd.DataFrame({'age': [request.user.age], 'money': [request.user.money], 'salary': [request.user.salary]})
    financial_recommend_pk =  model.predict(user)
    products = DepositAndSavings.objects.get(pk=financial_recommend_pk)
    serializer = DepositAndSavingsSerializer(products)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def addOrDeleteProducts(request, user_pk, dns_pk):
    user = get_object_or_404(User, pk=user_pk)
    financial_products = user.financial_products
    product = get_object_or_404(DepositAndSavings, pk=dns_pk)

    if financial_products:
        products = financial_products.split(',')
        if str(product.pk) in products:
            products.remove(str(product.pk))
        else:
            products.append(str(product.pk))
    else:
        products = [str(product.pk)]

    if len(products) > 1:
        financial_products = ','.join(products)
    elif len(products) == 1:
        financial_products = str(products[0])
    else:
        financial_products = ''
    # User 객체를 수정하고 저장
    user.financial_products = financial_products
    user.save()

    return Response({'message': 'ok'})


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def registered_products(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    financial_products = user.financial_products
    products = financial_products.split(',')
    my_products = DepositAndSavings.objects.filter(pk__in = products)
    serializer = DepositAndSavingsSerializer(my_products, many=True)
    return Response(serializer.data)