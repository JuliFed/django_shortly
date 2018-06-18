from django import forms
from .models import Shortly
from .utils.helpers import is_valid_url


class ShortlyModelForm(forms.ModelForm):
    class Meta:
        model = Shortly
        fields = ['url', 'clicked']
        labels = {'url': 'Full URL:',
                  'clicked': 'Clicked:'}
        def clean_url(self):
            """
            Валидация поля full url
            :return:
            """
            url = self.cleaned_data['url']
            if not is_valid_url(url):
                raise forms.ValidationError('Not valid url.')

