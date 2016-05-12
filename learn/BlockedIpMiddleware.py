from django import http
from mysite import settings

__author__ = 'Jack'

class BlockedIpMiddleware(object):
    def process_request(self,request):
        if request.META['REMOTE_ADDR'] in getattr(settings,'BLOCKED_IPS',[]):
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')
