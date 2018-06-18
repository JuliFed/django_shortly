from django.shortcuts import render, redirect, get_object_or_404
from .models import Shortly
from .forms import ShortlyModelForm
from django.views.generic import View


class ShortlyView(View):
    def get(self, request, url_id=None):
        if not url_id:
            urls = Shortly.objects.order_by('-clicked')[:7]
            return render(request, 'appshortly/index.html', {"urls": urls, "form": ShortlyModelForm(initial={'clicked': 0})})
        else:
            url = get_object_or_404(Shortly, id=url_id)
            form = ShortlyModelForm(instance=url)
            return render(request, 'appshortly/detail.html', {"form": form, "host_name": request.get_host(), "url_id":url_id})

    def post(self, request):
        form = ShortlyModelForm(request.POST)
        if form.is_valid():
            try:
                url = Shortly.objects.get(url=form.cleaned_data['url'])
            except Shortly.DoesNotExist:
                url = form.save()
            return redirect('/%s/detail' % url.pk)
        else:
            urls = Shortly.objects.order_by('-clicked')[:7]
            return render(request, 'appshortly/index.html', {"urls": urls, "form": form})


class RedirectByShortId(View):
    def get(self, request, url_id):
        url = get_object_or_404(Shortly, id=url_id)
        url.clicked += 1
        url.save()
        return redirect(url.url)


