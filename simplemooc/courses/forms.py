from django import forms


class ContactCourseForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)
