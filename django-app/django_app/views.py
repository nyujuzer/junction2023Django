import django.http.response
import django.core.handlers.wsgi
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, get_user
from django.http import HttpResponseRedirect, JsonResponse
from .models import Video
from .forms import VideoForm

def upload(request):
    data = {"userid":get_user(request=request).pk,
            "video_file":request.FILES.get('video_file')}
    form = VideoForm(request.POST, request.FILES)
    if request.method == 'POST':
        print(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save()
            return render(request,'success.html',{
                "fake":"BOOL",
                "confidence":"FLOAT"+"%",
                "video":new_form.video_file.url
            })  # Replace 'success_page' with the name/url of the success page
    else:
        print(VideoForm(user=request.POST, video_file=request.FILES).is_valid())
        return render(request, 'upload.html')
    return JsonResponse({"isValid": form.is_valid(), "form":form.data,"form errors":form.errors})

def index(request:django.core.handlers.wsgi.WSGIRequest):
    response:django.http.response.HttpResponse = render(request, 'home.html',
    {"user":request.user,
        "testimonials":[
                            {
                                "name": "Jane Doe",
                                "company": "CyberGuard Solutions",
                                "rating": 5,
                                "testimonial": "Exceptional deepfake detection services! Their cutting-edge technology and vigilant team have proven invaluable in safeguarding our digital content. Highly recommended!",
                                "date": "November 15, 2023"
                            },
                            {
                                "name": "John Smith",
                                "company": "SecureNet Innovations",
                                "rating": 4,
                                "testimonial": "Reliable deepfake detection that exceeded our expectations. Their service has become an integral part of our security strategy. Great job!",
                                "date": "November 20, 2023"
                            },
                            {
                                "name": "Emily Thompson",
                                "company": "SafeMedia Solutions",
                                "rating": 5,
                                "testimonial": "Impressive results! The deepfake detection provided by this company is unparalleled. Our content is now safer, and we can trust in the authenticity of our digital assets.",
                                "date": "November 22, 2023"
                            }
                        ]
                     }
                )
    response['allow-access-control-origin'] = "localhost"
    return response

def register(request:django.core.handlers.wsgi.WSGIRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            return index(request)
        else:
            print(
                form.data,"\n",form.error_messages
                )
            print(
                form.data['password1'] == form.data['password2']
            )
        return render(request, "register.html", {'form':form })
    else:
        form = UserCreationForm()
        return render(request, "register.html", {'form':form })
    
def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if user is not None:
            print("user != none")
            login(request,user)
            print("return index____")
            return index(request)
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")
def try_demo(request):
    if request.method == "POST":
        return upload(request)
    return render(request,"upload.html")