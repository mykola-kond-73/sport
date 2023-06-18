from coolcite import settings
from django.core.cache import cache
import logging
from django.http import HttpResponse

error_logger=logging.getLogger('error_logger')

class DataMixin:
    def get_user_context(self,request,**kwargs):
        context=kwargs

        context['media_url']=settings.MEDIA_URL

        return context
    
def cache_handler(context,dict):
    for i in dict.keys():
        cache_data=cache.get(i)
        try:
            if not cache_data:
                data=dict[i]()
                cache.set(i,data,600)

        except Exception as exc:
                error_logger.error("STATUS - 500, {0}".format(exc))
                return HttpResponse(status=500)
        
        context[i]=cache_data or data

def edit_data(data):
     for elem in data:
            elem.descriptionList=elem.description.split("\r\n")
            del elem.description