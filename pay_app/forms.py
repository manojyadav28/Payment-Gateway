from email.policy import default
from locale import currency
from random import choices
from secrets import choice
from django import forms
from django.core.validators import RegexValidator


CURRENCY_CHOICES = (("356","INR"),("826","GBP"),("840","USD"),("978","EUR"),)

payment_choices =(
    ("", "Select Payment Type"),
    ("CC", "Credit Card"),
    ("DC", "Debit Card"),
    ("NB", "Net Banking"),
    ("WL", "Wallet"),
    ("UP", "UPI"),
)
mop_type_choices =(
    ("", "Select MOP Payment Type"),
)



class ContactForm(forms.Form):
    amount = forms.CharField(max_length=10, min_length=1, required=True,validators=[RegexValidator('[0-9]',message='Username must be Numeric'),], widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Amount'}))

    # currency_code = forms.CharField(max_length=3, min_length=3, required=True,validators=[RegexValidator('[0-9]',message='Username must be Numeric'),],widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Currency Code'}))

    currency_code = forms.ChoiceField(choices=CURRENCY_CHOICES)

    cust_email = forms.CharField(max_length=120, min_length=6, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    cust_name = forms.CharField(max_length=150, min_length=1)
    phone = forms.CharField(max_length=10, required=True, validators=[RegexValidator('^[6-9][0-9]{9}$', message="Enter a Valid Mobile Number")], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile'}))

    #hash = forms.CharField(max_length=64, min_length=64, required=True,validators=[RegexValidator('^[\s\w-]+$'),])
    payment_type = forms.ChoiceField(choices=payment_choices)

    mop_type = forms.CharField(widget=forms.Select)
    
    card_number = forms.CharField(max_length=16, min_length=14,validators=[RegexValidator('[0-9]',message='Card number must be Numeric'),],widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Card Number'})) 

    card_exp_date = forms.CharField(max_length=6, min_length=6, validators=[RegexValidator('[0-9]',message='Card number must be Numeric'),],widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card exp date'}))

    cvv = forms.CharField(max_length=4, min_length=3, validators=[RegexValidator('[0-9]',message='cvv must be Numeric'),],widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'CVV'}))    

    order_id = forms.CharField(max_length=50, min_length=1)    
    
    product_desc = forms.CharField(max_length=1024, min_length=3)
    #return_url = forms.CharField(max_length=1024, min_length=4)
    #txntype = forms.CharField(max_length=4)

    
    
    upi = forms.CharField(max_length=45, min_length=5, required=True,validators=[RegexValidator('^[\w.-]+@[\w.-]+$'),],widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'UPI'}))



    def clean(self):
        super(ContactForm, self).clean()
        return self.cleaned_data     
