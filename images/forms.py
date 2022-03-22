from tkinter import Widget
from django import forms
from multiupload.fields import MultiImageField
from .models import UserImage

class AddForm(forms.ModelForm):
    image = MultiImageField(min_num=1, max_num=20)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AddForm, self).__init__(*args, **kwargs)
    class Meta:
        model = UserImage
        fields = ('image',)

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        request = self.request
        first_images = self.cleaned_data.pop('first')
        instance = super(AddForm, self).save()
        for image in first_images:
           first = UserImage(image=image,user=request.user)
           first.save()

        return instance