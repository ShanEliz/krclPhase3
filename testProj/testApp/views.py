from django.shortcuts import render, redirect
from .forms import TimelineForm
from .models import Episode
import json
import os
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


# Create your views here.

# def timeline_view(request):

#     return render(request, 'submit')

def home(request):
    return render(request, 'home.html')

def submit_story(request):
    if request.method == 'POST':
        form = TimelineForm(request.POST)
        if form.is_valid():
            file_path = os.path.join(settings.BASE_DIR, 'static/dataTL.json')
            with open(file_path, 'r', errors='ignore', encoding="utf8") as roar:
                new = json.load(roar)
                new['events'].append({
                "media": {
                    "url": str(form.cleaned_data['media_url']), 
                    "caption": form.cleaned_data['caption'], 
                    "credit": form.cleaned_data['credit']
                }, 
                "start_date": {
                    "month": str(form.cleaned_data['startDate'].month), 
                    "day": str(form.cleaned_data['startDate'].day), 
                    "year": str(form.cleaned_data['startDate'].year)
                }, 
                "text": {
                    "headline": form.cleaned_data['title'], 
                    "text": form.cleaned_data['story']
                }
                })
                with open(file_path, 'w', errors='ignore', encoding="utf8") as hehe:
                    json.dump(new, hehe)
                return render(request, 'tl_success.html')
    else:
        form = TimelineForm()  
        
    return render(request, 'submit_story.html', {'form' : form})  
    
def playlists(request):
    return render(request, 'playlists.html')

def episodes(request):
    episodes_list = Episode.objects.order_by('-pub_date')
    context = {'episodes_list' : episodes_list}
    return render(request, 'episodes.html', context)  

@csrf_exempt
def vn_success(request):
    if request.method == 'POST':
        email = EmailMessage(
        subject = 'Your Voicenote from KRCL',
        body = 'Hello, ' + request.POST['name'] + "\n\nAttached is your Voicenote!\n\nThank you for taking the time to test this feature!",
        from_email = 'face151@windowslive.com',
        to = [request.POST['email']]
        )
        upload_file = request.FILES['audio']
        content = upload_file.read()
        email.attach(request.POST['name'] + ".mp3", content, 'audio/mp3')
        email.send(fail_silently=False)
        return JsonResponse({
            'success': True,
            'url': 'success',
        })
    return render(request, 'vn_success.html')

@csrf_exempt
def voicenote(request):
    return render(request, 'voicenote.html')  