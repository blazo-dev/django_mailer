from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.shortcuts import render
from .forms import NewsletterUserForm
from .models import NewsletterUser

# Create your views here.


def newsletter_subscribe(request):
    form = NewsletterUserForm(request.POST or None)

    print(form)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, "Email already exists!")
        else:
            instance.save()
            messages.success(
                request, "Subscribe successful! Thank you for choosing to stay connected with us.")

            # Building email
            subject = "Law book"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            html_template = "newsletter/email_templates/welcome.html"
            html_message = render_to_string(html_template)

            message = EmailMessage(
                subject,
                html_message,
                from_email,
                to_email
            )

            message.content_subtype = "html"
            message.send()
    context = {"form": form}
    return render(request, 'subscribe.html', context)


def newsletter_unsubscribe(request):
    form = NewsletterUserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        posible_user = NewsletterUser.objects.filter(email=instance.email)
        if posible_user.exists():
            posible_user.delete()
            messages.success(request, "Unsubscribe successful.")
        else:
            print("Email not found")
            messages.error(request, "Email not found.")

    context = {"form": form}
    return render(request, "unsubscribe.html", context)
