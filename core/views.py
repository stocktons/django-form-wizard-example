from django.http import HttpResponse
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from core.forms import GuestDetailForm, BusinessDetailForm, BookingDetailForm

class BookingWizardView(SessionWizardView):
    form_list = [GuestDetailForm, BusinessDetailForm, BookingDetailForm] # list of all forms in our Wizard
    template_name = "core/index.html" #template for all forms in our Wizard

    def done(self, form_list, **kwargs):
        return HttpResponse("Form submitted!")
