from django import forms
from core.models import Guest

class GuestDetailForm(forms.ModelForm):
    BOOL_CHOICES = [(True, "Yes"), (False, "No")]
    is_business_guest = forms.BooleanField(
        widget=forms.RadioSelect(choices=BOOL_CHOICES),
        required=False,
    )

    class Meta:
        model = Guest
        fields = ("first_name", "last_name", "email", "phone")
