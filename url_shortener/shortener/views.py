from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.http import Http404

from .models import UrlModel


class CreateUrlView(CreateView):
    """Display form for url shortening.
       When url is submitted display the shortened link ready to use"""
    model = UrlModel
    fields = ['original_url']
    template_name = 'home.html'
    success_url = 'create-url'

    def form_valid(self, form):
        super(CreateUrlView, self).form_valid(form)
        context = UrlModel.objects.latest('id')
        return render(self.request, self.template_name, {'object':context})


def redirect_url(request, address):
    try:
        url = get_object_or_404(UrlModel, url_slug=address)
        return HttpResponseRedirect(url.original_url)
    except:
        raise Http404()
