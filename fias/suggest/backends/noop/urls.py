# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.urls import re_path

from .views import *


urlpatterns = [
    re_path(r'^suggest.json$', EmptyResponseListView.as_view(), name='suggest'),
    re_path(r'^suggest-area.json$', EmptyResponseListView.as_view(), name='suggest-area'),
]
