from django import forms
from media.models import MediaCategory, MediaItem, MediaType


class MediaItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'size':
                self.fields[field].widget = forms.HiddenInput()
            else:
                self.fields[field].widget.attrs.update(
                    {'class': "form-control"})

    class Meta:
        model = MediaItem
        fields = '__all__'


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': "form-control"})

    class Meta:
        model = MediaCategory
        fields = '__all__'
