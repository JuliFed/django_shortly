from django.shortcuts import render, redirect, get_object_or_404
from .models import Shortly
from .utils import helpers


def index(request):
    urls = Shortly.objects.order_by('-clicked')[:7]
    return render(request, 'appshortly/index.html', {"urls": urls})


def create_new_url(request):
    if request.method == 'POST':
        if Shortly.objects.filter(url=request.POST.get('url_link')).exists():
            url = Shortly.objects.filter(url=request.POST.get('url_link')).first()
            return redirect('/%s' % url.id)
        else:
            if helpers.is_valid_url(request.POST.get('url_link')):
                url = Shortly(url=request.POST.get('url_link'))
                url.save()
                return render(request, 'appshortly/detail.html', {"url": url, "host_name": request.get_host()})
            else:
                urls = Shortly.objects.order_by('-clicked')[:7]
                return render(request, 'appshortly/index.html', {"urls": urls, "error": "Can't create new short link. Invalid URL."})
    return redirect('/')


def view_url(request, url_id):
    url = get_object_or_404(Shortly, id=url_id)
    return render(request, 'appshortly/detail.html', {"url": url, "host_name": request.get_host()})


def detail_url(request, url_id):
    url = get_object_or_404(Shortly, id=url_id)
    url.clicked += 1
    url.save()
    return redirect(url.url)
