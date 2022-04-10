import hashlib
import json
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)

        AMOUNT = int(request.POST.get('amount'))
        #print('AMOUNT')
        print(AMOUNT)

        pay_amount = AMOUNT*100
        pay_value = str(pay_amount)
        print(pay_value)
        print('pay_value')

        CURRENCY_CODE = request.POST.get('currency_code')
        print('CURRENCY_CODE')
        print(CURRENCY_CODE)

        CUST_NAME = request.POST.get('cust_name')
        print('cust_name')
        print(CUST_NAME)

        CUST_EMAIL = request.POST.get('cust_email')
        print('cust_email')
        print(CUST_EMAIL)

        PHONE = request.POST.get('phone')
        print('phone')
        print(PHONE)

        HASH = request.POST.get('hash')
        print('hash')
        print(HASH)

        MOP_TYPE = request.POST.get('mop_type')
        print('mop_type')
        print(MOP_TYPE)

        # ORDER_ID = 'ORD'+get_random_string(length=8)
        # print('order_id')
        # print(ORDER_ID)

        ORDER_ID = request.POST.get('order_id')
        print('order_id')
        print(ORDER_ID)

        PAYMENT_TYPE = request.POST.get('payment_type')
        print('payment_type')
        print(PAYMENT_TYPE)

        UPI = request.POST.get('example@upi')
        print('upi')
        print(UPI)

        PAY_ID = '2104291057251151'
        PRODUCT_DESC = request.POST.get('product_desc')
        print('product_desc')
        print(PRODUCT_DESC)

        RETURN_URL = 'http://127.0.0.1:8000/response'
        print('return_url')
        print(RETURN_URL)

        TXNTYPE = 'SALE'
        print('txn_type')
        print(TXNTYPE)

        CARD_NUMBER = request.POST.get('card_number')
        print('card_number')
        print(CARD_NUMBER)

        CARD_EXP_DT = request.POST.get('card_exp_date')
        print('card_exp_date')
        print(CARD_EXP_DT)

        CVV = request.POST.get('cvv')
        print('cvv')
        print(CVV)

        UPI = request.POST.get('upi')
        print('upi')
        print(UPI)

        has_str = 'AMOUNT='+ pay_value + '~CARD_EXP_DT=' +CARD_EXP_DT + '~CARD_NUMBER='+CARD_NUMBER + '~CURRENCY_CODE='+CURRENCY_CODE + '~CUST_EMAIL='+CUST_EMAIL + '~CUST_NAME='+CUST_NAME + '~CUST_PHONE='+PHONE + '~CVV='+CVV + '~MOP_TYPE=' + MOP_TYPE + '~ORDER_ID='+ORDER_ID + '~PAYMENT_TYPE='+PAYMENT_TYPE + '~PAY_ID='+PAY_ID + '~PRODUCT_DESC='+str(PRODUCT_DESC) + '~RETURN_URL='+RETURN_URL + '~TXNTYPE='+TXNTYPE+'~UPI='+ UPI +'ae8539c97f1a4b7d'
        print(has_str)

        sha256_hash = hashlib.sha256()
        sha256_hash.update(has_str.encode('utf-8'))
        has_val = sha256_hash.hexdigest().upper()
        print(has_val)

        return render(request, 'postForm.html', {'AMOUNT': pay_value, 'CURRENCY_CODE': CURRENCY_CODE, 'CUST_NAME': CUST_NAME, 'CUST_EMAIL': CUST_EMAIL, 'CUST_PHONE': PHONE, 'HASH': HASH, 'MOP_TYPE': MOP_TYPE, 'ORDER_ID': ORDER_ID, 'PAYMENT_TYPE': PAYMENT_TYPE, 'PAY_ID': PAY_ID, 'PRODUCT_DESC': PRODUCT_DESC, 'RETURN_URL': RETURN_URL, 'TXNTYPE': TXNTYPE, 'CARD_NUMBER':CARD_NUMBER, 'CARD_EXP_DT':CARD_EXP_DT, 'CVV':CVV, 'UPI':UPI, 'HASH':has_val})
    else:
        fm = ContactForm(initial={'currency_code': 356, 'txn_type': 'SALE'})
    return render(request, 'pay.html', {'form': fm})

def create_has(request, string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(b''+string)
    print(sha256_hash)
    return sha256_hash.hexdigest().upper()

def signature(request):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(b"AMOUNT=100~CURRENCY_CODE=356~CUST_CITY=Noida~CUST_COUNTRY=India~CUST_EMAIL=ashok@cagtech.in~CUST_NAME=Asho Sharma~CUST_PHONE=9911480245~CUST_SHIP_CITY=Aligarh~CUST_SHIP_COUNTRY=India~CUST_SHIP_EMAIL=ashok@cagtech.in~CUST_SHIP_NAME=Ashok Sharma~CUST_SHIP_PHONE=9911480245~CUST_SHIP_STATE=Uttar Pradesh~CUST_SHIP_STREET_ADDRESS1=Address 1~CUST_SHIP_STREET_ADDRESS2=Address 2~CUST_SHIP_ZIP=201301~CUST_STATE=Uttar Pradesh~CUST_STREET_ADDRESS1=Address1~CUST_STREET_ADDRESS2=Address2~CUST_ZIP=201301~MERCHANTNAME=Demo Merchant~ORDER_ID=ORD0000001~PAY_ID=2104291057251151~PRODUCT_DESC=Test Product~RETURN_URL=https://www.csgtech.in/~TXNTYPE=SALE~submit=Click to Payae8539c97f1a4b7d")
    print(sha256_hash)
    return HttpResponse(sha256_hash.hexdigest().upper())

@csrf_exempt
def response(request):
    if request.method == "POST":
        print('response Start')
        print(dict(request.POST.items()))
    return HttpResponse('response')

def has_eith_file(request):
    filename = 'pay_app/ashok.txt'
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            print(sha256_hash)
        print(sha256_hash.hexdigest().upper())
    return HttpResponse(sha256_hash.hexdigest().upper())
