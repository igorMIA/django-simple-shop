from django import forms


class AddCart(forms.Form):
    product_id = forms.CharField()
    count = forms.CharField()


class Order(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    tel = forms.CharField(max_length=100)
