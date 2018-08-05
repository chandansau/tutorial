#from django.shortcuts import render,get_object_or_404,get_list_or_404
#from django.http import HttpResponse
#from . models import Person
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from frinds.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    return render(request, 'homepage.html')
def Aboutus(request):
    return render(request,'base.html')
def contactus(request):
    form_class = ContactForm(request.POST or None)
    if form_class.is_valid():
        subject = 'Thank you for Contacting us'
        messege = 'Your messege: ' + request.POST.get('content')
        from_email = settings.EMAIL_HOST_USER
        usermail = request.POST.get('contact_email')
        to_list = [usermail, settings.EMAIL_HOST_USER]
        send_mail(subject, messege, from_email, to_list, fail_silently=False)
        return HttpResponseRedirect('thankyou')
    return render(request, 'form.html', {'form': form_class})
def thankyou(request):
    response = HttpResponse()
    response.write('<body bgcolor=silver><center><h1><font color =red>Thanks for contacting us .</font><br><font color=blue>we just sent an email to you<blue></h1></center></body>')
    response.write('<body><button type="button"><a href="http://127.0.0.1:9999/"><h4><font color="blue">Home</font></h4></a></button></body>')
    return response
def tutorial(request):
    return render(request,'tutorial.html')
def pyone(request):
    return render(request,'pyone.html')
def pytwo(request):
    return render(request,'pytwo.html')
def pythree(request):
    return render(request,'pythree.html')
def pyfour(request):
    return render(request,'pyfour.html')
def pyfive(request):
    return render(request,'pyfive.html')
def pysix(request):
    return render(request,'pysix.html')
def pyseven(request):
    return render(request,'pyseven.html')
def pyeight(request):
    return render(request,'pyeight.html')

def pynine(request):
    return render(request,'pynine.html')
def pyten(request):
    return render(request,'pyten.html')
def pyeleven(request):
    return render(request,'pyeleven.html')
def pytwelve(request):
    return render(request,'pytwelve.html')
def pythirteen(request):
    return render(request,'pythirteen.html')
def pyfourteen(request):
    return render(request,'pyfourteen.html')
def pyfifteen(request):
    return render(request,'pyfifteen.html')
def pysixteen(request):
    return render(request,'pysixteen.html')

def swift(request):
    return render(request,'swift.html')
def swone(request):
    return render(request,'sw1.html')
def swtwo(request):
    return render(request,'sw2.html')
def swthree(request):
    return render(request,'sw3.html')
def swfour(request):
    return render(request,'sw4.html')
def swfive(request):
    return render(request,'sw5.html')
def swsix(request):
    return render(request,'sw6.html')
def swseven(request):
    return render(request,'sw7.html')
def sweight(request):
    return render(request,'sw8.html')
def swnine(request):
    return render(request,'sw9.html')
def swten(request):
    return render(request,'sw10.html')
def sweleven(request):
    return render(request,'sw11.html')
def swtwelve(request):
    return render(request,'sw12.html')
def swthirteen(request):
    return render(request,'sw13.html')
def swfourteen(request):
    return render(request,'sw14.html')