#coding=utf-8
from django.db import models
#这里写的是数据库相关
# Create your models here.

from django.db import models
import ast

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField

    def __unicode__(self):
        return self.name


class CompressedTextField(models.TextField):
    ''' model Fields for storing text in a compressed format (bz2 by default) '''
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if not value:
            return value

        try:
            return value.decode('base64').decode('bz2').decode('utf-8')
        except Exception:
            return value

    def get_prep_value(self, value):
        if not value:
            return value

        try:
            value.decode('base64')
            return value
        except Exception:
            try:
                temp = value.encode('utf-8').encode('bz2').encode('base64')
            except Exception:
                return value

            else:
                if len(temp) > len(value):
                    return value

                return temp

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value) # use str(value) in Python 3

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)