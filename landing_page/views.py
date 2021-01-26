from landing_page.models import Work, Education, Skill, SiteConfiguration
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.


def home(request):
    web_info = SiteConfiguration.objects.latest('created_on')
    return render(request, 'landing_page/home.html', {
        'web_info': web_info
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            title = "Website Inquiry"
        body = {
            'subject': form.cleaned_data['subject'],
            'sender': form.cleaned_data['sender'],
            'email': form.cleaned_data['email_address'],
            'message': form.cleaned_data['message'],
        }
        message = "\n".join(body.values())

        try:
            send_mail(title, message, 'admin@example.com', ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('home')

    form = ContactForm()
    return render(request, 'landing_page/contact.html', {'form': form})


def cv(request):
    works = Work.objects.all()
    educations = Education.objects.all()
    web_info = SiteConfiguration.get_solo()
    skills = Skill.objects.all()
    return render(request, 'landing_page/cv.html', {
        'works': works,
        'educations': educations,
        'skills': skills,
        'web_info': web_info
    })
