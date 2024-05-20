from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, send_mass_mail, BadHeaderError


# def send_email(request):
#     send_mail('Hey your estate',
#               'Hi i buy it',
#               'django@gmail.com',
#               ['slang6682@gmail.com'])
#     return HttpResponse('HI')