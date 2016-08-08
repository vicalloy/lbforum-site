from django import forms
from django.utils.translation import ugettext_lazy as _

from allauth.account.forms import SignupForm as AllAuthSignupForm


class SignupForm(AllAuthSignupForm):

    captcha = forms.CharField(label=_("Captcha"))

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        if captcha != 'captcha':
            raise forms.ValidationError(_('Captcha is not correct'))
        return captcha
