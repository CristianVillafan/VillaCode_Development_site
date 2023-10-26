from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','phone_number','menssage']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
                })
