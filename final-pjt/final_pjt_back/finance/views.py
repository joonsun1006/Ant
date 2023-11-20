from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializer import DepositAndSavingsSerializer
from .models import DepositAndSavings
import requests
# Create your views here.

FINLIFE_API_KEY = settings.FINLIFE_API_KEY
EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY

@api_view(['GET'])
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
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={EXCHANGE_API_KEY}&searchdate=20231117&data=AP01'
    response = requests.get(url).json()
    result = {}
    for li in response:
        result[li['cur_nm']] = li['deal_bas_r']
    return Response(result)