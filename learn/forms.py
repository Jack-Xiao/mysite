#coding=utf-8
__author__ = 'Jack'

from django import forms
class AddForm(forms.Form):
    a = forms.IntegerField
    b = forms.IntegerField
