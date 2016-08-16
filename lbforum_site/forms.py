from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField

from allauth.account.forms import SignupForm as AllAuthSignupForm


class SignupForm(AllAuthSignupForm):

    captcha = CaptchaField(label=_("Captcha"))
