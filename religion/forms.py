from django import forms
from .models import Message, Service

class MessageForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), )

    class Meta(object):
        model = Message
        fields = ['text', 'user', 'service']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            # 'service': forms.ModelChoiceField(attrs={'class': 'form-control'}),
        }
