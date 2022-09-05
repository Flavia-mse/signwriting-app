from django.db import models
from django import forms
from .models import Palavra


class PalavraForm(forms.ModelForm):
    nome = forms.CharField(max_length=100)
    sinal = forms.ImageField()

    class Meta:
        model = Palavra
        fields = "__all__"

    def save(self, commit=True):
        print("passou no save")
        instance = super(PalavraForm, self).save(commit=False)
        instance.save()
        return instance
