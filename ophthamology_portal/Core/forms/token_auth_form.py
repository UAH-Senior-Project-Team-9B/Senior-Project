from django import forms

from ophthamology_portal.Core.models import TokenAuthModel


class TokenAuthForm(forms.ModelForm):
    class Meta:
        model = TokenAuthModel
        fields = {"group"}
