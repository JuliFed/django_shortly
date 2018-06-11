from django.shortcuts import render, redirect, get_object_or_404
from .models import Shortly
from urllib.parse import urlparse

def index(request, error=None):
    print('error', error)
    if not Shortly.objects.first():
        return render(request, 'appshortly/index.html', {"urls": []})

    urls = Shortly.objects.order_by('-clicked')[:10]
    return render(request, 'appshortly/index.html', {"urls": urls, "error": error})


def is_valid_url(url):
    parts = urlparse(url)
    return parts.scheme in ('http', 'https')

def create_new_url(request):
    if request.method == 'POST':

        unique_link = Shortly.objects.filter(url=request.POST.get('url_link')).first()
        if unique_link:
            return redirect('/%s' % unique_link.id)

        if is_valid_url(request.POST.get('url_link')):
            url = Shortly(url=request.POST.get('url_link'))
            url.save()
            return render(request, 'appshortly/detail.html', {"url": url, "host_name": request.build_absolute_uri()})
        else:
            # TODO - Передать ошибку !
            return redirect('/')

    return redirect('/')

def view_url(request, url_id):
    url = get_object_or_404(Shortly, id=url_id)
    return render(request, 'appshortly/detail.html', {"url": url, "host_name": request.get_host()})


def detail_url(request, url_id):
    url = get_object_or_404(Shortly, id=url_id)
    url.clicked += 1
    url.save()
    return redirect(url.url)
