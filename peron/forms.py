from django import forms
from . models import Line, Station


class AddForm(forms.ModelForm):
    
      class Meta:
          model = Line
          fields = "__all__"


