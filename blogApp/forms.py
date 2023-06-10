from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))