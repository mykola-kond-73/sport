from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView,DetailView,CreateView
from django.shortcuts import get_object_or_404, render,redirect
import logging
from django.http import HttpResponse,HttpResponseNotFound,Http404
from .utils import *
from .forms import *

info_logger=logging.getLogger('info_logger')
error_logger=logging.getLogger('error_logger')

class Index(DataMixin,TemplateView):
    template_name='sport/index.html'
    extra_context={'title':'Sport'}
    allow_empty: False

    def get_context_data(self,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        field_dict={
            'data':lambda:SeasonTicket.objects.all().order_by('price')
        }
        cache_handler(context,field_dict)
        edit_data(context['data'])

        c_def=self.get_user_context(self.request)
        context=dict(list(context.items())+list(c_def.items()))

        return context

class About(DataMixin,TemplateView):
    def get(self,request):
        ctx={}

        c_def=self.get_user_context(request,title='Про нас')
        context=dict(list(ctx.items())+list(c_def.items()))

        return render(request,'sport/about.html',context=context)

class Pricing(DataMixin,TemplateView):
    template_name='sport/pricing.html'
    extra_context={'title':'Абонементи'}
    allow_empty: False

    def get_context_data(self,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        field_dict={
            'data':lambda:SeasonTicket.objects.all().order_by('price')
        }
        cache_handler(context,field_dict)
        edit_data(context['data'])

        c_def=self.get_user_context(self.request)
        context=dict(list(context.items())+list(c_def.items()))

        return context

def add_order(request,season_ticket_id):
    if request.method=='POST':
        c_def={
            'season_ticket_id':int(season_ticket_id),
        }
        model_data=dict(list(request.POST.items())+list(c_def.items()))
        del model_data['submit']

        form=AddOrder(model_data)
        ctx={
            'title':'Add-order',
            'form':form,
            'season_ticket_id':str(season_ticket_id)
        }

        if form.is_valid():
            try:
                form.save()
            except:
                error_logger.error('user doesn`t ordered')

                form.add_error(None,'Помилка при створенні замовлення')
                return render(request,'sport/add-order.html',context=ctx)
            
            return redirect('home')
    else:
        info_logger.info('form doesn`t valid')
        
        form=AddOrder()
        ctx={
            'title':'Add-order',
            'form':form,
            'season_ticket_id':season_ticket_id
        }            

        return render(request,'sport/add-order.html',context=ctx)

        

def page_not_fount(request,*args,**kwargs):
    return render(request,'triangle/404.html',)

def handle_error_400(request,exception):
    error_logger.error("STATUS - 400, {0}".format(exception))

    return HttpResponse(status=400)

def handle_error_403(request,exception):
    error_logger.error("STATUS - 403, {0}".format(exception))

    return HttpResponse(status=403)

def handle_error_500(request):
    error_logger.error("STATUS - 500, {0}")
    return HttpResponse(status=500)