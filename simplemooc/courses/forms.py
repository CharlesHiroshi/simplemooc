from django import forms


class ContactCourseForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=75)
    message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)
