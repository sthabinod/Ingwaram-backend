from django.shortcuts import render

from website.models import About, Company, Event, History, Front_Persons, Writer

from django.core.mail import send_mail

def index(request):
    company = Company.objects.get(id=1)
    events = Event.objects.all()
    front_person = Front_Persons.objects.all()[:5]
    about = About.objects.all()[:5]
    data = {
        'events':events,
        'company':company,
        'front_persons':front_person,
        'abouts':about
    }
    return render(request, "index.htm",data)

def about(request):
    history = History.objects.all()
    about = About.objects.all()
    data = {
        'aboutus':about,
        'histories':history
    }
    return render(request, "pages/about.htm", data)

def gallery(request):

    events = Event.objects.all()
    data = {
        'events':events
    }
    return render(request, "pages/gallery.html", data)

def history(request):
    front_person = Front_Persons.objects.all()
    histories=History.objects.all()
    data = {
        'histories':histories,
        'front_persons':front_person
    }
    return render(request, "pages/signs.htm", data)


def front_person(request):
    events = Event.objects.all()
    front_persons=Front_Persons.objects.all()
    data = {
        'front_persons':front_persons,
        'events':events
            }
    return render(request, "pages/front.htm", data)


def contact(request):
    company = Company.objects.get(id=1)
    message_sent = ''
    try:
        if request.method == "POST":
            full_name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            send_mail(subject  , "Full name: "+  full_name + "\n" + "Phone number: "+  phone_number + "\n" + "Message: " + message,
        email,('stha.binod1000@gmail.com',),
        fail_silently=False,    
    )
            message_sent = "Email sent successfully!"
    except Exception:
        message_sent = "Something went wrong. Please try again!"

    data = {
        'company':company,
        'message_sent':message_sent
    }
    return render(request, "pages/contact.htm", data)


def writer(request):

    writer=Writer.objects.get(id=1)
    data = {
        'writer':writer
    }
    return render(request, "pages/writer.htm",data)


def gene(request):

    # genes=Writer.objects.get(id=1)
    # data = {
    #     'writer':writer
    # }
    return render(request, "pages/gene.htm")
