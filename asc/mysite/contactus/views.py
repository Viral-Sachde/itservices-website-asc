from django.contrib import messages
from django.shortcuts import redirect
from .forms import FeedbackForm
from .models import Category, ContactUs, Newsletter
from django.shortcuts import render
from django.core.mail import send_mail

# ...

def test_redirect(request):
    c = Category.objects.get(name='python')
    return redirect(c)


def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm()
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'feedback.html')


def savey(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        temp1 = email
        temp2 = 'Dear ' + name + ',\n\nThank you for reaching out to Anant Soft Computing through our website. We appreciate your interest in our company and we are thrilled to have the opportunity to connect with you.\n\nWe have received your message and our team will review it shortly. We pride ourselves on delivering exceptional customer service and providing innovative solutions to our clients, and we are committed to addressing your query as soon as possible.\n\nAt Anant Soft Computing, we strive to build long-lasting relationships with our clients based on trust, integrity, and mutual respect. We value your input and we are grateful for the opportunity to earn your business.\n\nWe will be in touch with you soon to discuss your inquiry further. In the meantime, if you have any additional questions or concerns, please do not hesitate to contact us at anantsoftcomputing@gmail.com 9638544455. We are always here to help.\n\nThank you again for contacting us. We look forward to speaking with you soon.\n\nBest regards,\nAnant Soft Computing Team'

        send_mail(
            'Thank you for Contacting Anant Soft Computing',
            temp2,
            'bhautikphotodump@gmail.com',
            [temp1],
            fail_silently=False
        )


        en = ContactUs(name=name, email=email, subject=subject, message=message)
        en.save()
        messages.success(request,'Your Message has been sent successfully!!')
    return render(request,'index.html')


def services(request):
    return render(request, 'services.html')


def home(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def blog(request):
    return render(request, 'blog.html')


def savey2(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        temp = email
        send_mail(
            'Welcome to the Anant Soft Computing Newsletter Community',
            'Dear Valued Subscriber,\n\nWe hope this email finds you in good health and spirits. We are thrilled to welcome you to the Anant Soft Computing newsletter community!\n\nThank you for subscribing to our newsletter. We appreciate your interest in our company and the work that we do. Our newsletter is designed to provide you with the latest updates and insights on the world of soft computing, including the latest trends, tips, and tricks to help you stay ahead of the curve.\n\nWe promise to deliver high-quality content that will add value to your knowledge and keep you informed about our upcoming events and product releases. We are excited to have you on board and look forward to sharing our passion for soft computing with you.\n\nIf you have any questions or feedback about our newsletter, please do not hesitate to reach out to us. We welcome your suggestions and ideas, as they will help us improve our newsletter and serve you better.\n\nOnce again, thank you for subscribing to our newsletter. We are grateful for your trust and support, and we look forward to building a long-lasting relationship with you.\n\nBest regards,\nAnant Soft Computing Team',
            'bhautikphotodump@gmail.com',
            [temp],
            fail_silently=False
        )

        en = Newsletter(email=email)
        en.save()
        messages.success(request, 'Your have subscribed to newsletter successfully!!')
    return render(request, 'index.html')


def tou(request):
    return render(request, 'tou.html')

def pp(request):
    return render(request, 'pp.html')