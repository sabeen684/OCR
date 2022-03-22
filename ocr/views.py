from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from images.forms import AddForm
from images.models import ImageResult, UserImage
 
# Views
@login_required
def home(request):
    print(request.user)
    if request.method =='GET':
        form = AddForm()
        return render(request, "home.html",{'form':form})
    if request.method == 'POST':
        first_images = request.FILES.getlist('images')
        print(first_images)
        for image in first_images:
            print(image)
            if image:
                first = UserImage(image=image,user=request.user)
                first.save()
        return redirect('result')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

@login_required
def results_view(request):
    user_images = UserImage.objects.filter(user=request.user)
    data = []
    for user in user_images:
        ir = ImageResult.objects.get(image=user)
        temp_data = {
            "image":user.image.url,
            "result":ir.result,
        }
        data.append(temp_data)

    return render(request,"results.html",context={"data":data})