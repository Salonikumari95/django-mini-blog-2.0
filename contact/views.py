from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    msg = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                subject=f"Contact from {name}",
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            msg = "Thank you! Acknowledgment mail sent."
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'msg': msg})
