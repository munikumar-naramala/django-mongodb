from django.urls import re_path as url, include

urlpatterns = [
    url('', include('log_parser_mongo.urls')),
]
