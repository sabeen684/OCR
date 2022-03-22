from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import UserImage,ImageResult
from ocr.ocr import text_detection

@receiver(post_save,sender=UserImage)
def set_result(sender,created,instance,*args,**kwargs):
    if created:
        print(instance.image.url)
        text = text_detection(instance.image.url)
        ImageResult.objects.create(image=instance,result=text)
