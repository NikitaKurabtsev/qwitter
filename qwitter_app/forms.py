from django import forms
from qwitter_app.models import Qweet


class QweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget = forms.widgets.Textarea(
            attrs={
                'placeholder': 'Qweet something...',
                'class': 'textarea is-info is-medium'
            }
        ),
        label = '',
    )

    class Meta:
        model = Qweet
        exclude = ('user',)
