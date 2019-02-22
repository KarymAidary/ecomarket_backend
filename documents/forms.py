from django import forms
from django.utils import timezone


class InvoiceForm(forms.Form):
    invoice_number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '135'}))
    date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
    seller_company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ООО"ПАК СТАР"'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '117303, г. Москва, ул. Юшуньская , д.1А, кор.3; ОГРН:1027739507795'}))
    inn_kpp_seller = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '7702013420/772701001'}))
    shipper_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'ООО"ПАК СТАР" 117303, г. Москва, ул. Юшуньская Б., д.1А, кор.3; ОГРН:1027739507795'}))

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['invoice_number'].label = "СЧЕТ-ФАКТУРА №"
        self.fields['date'].label = "Дата"
        self.fields['seller_company_name'].label = "Название фирмы"
        self.fields['address'].label = "Адрес фирмы"
        self.fields['inn_kpp_seller'].label = "ИНН/КПП покупателя"
        self.fields['shipper_address'].label = "Грузоотправитель и его адрес"
