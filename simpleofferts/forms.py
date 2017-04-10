from django import forms
from .models import SimpleOfert


"""
class SimpleOfertCreateModelForm(forms.ModelForm):
   # use_required_attribute = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #self.fields['tags'].required = False

    class Meta:
        model = SimpleOfert
        fields = ('title', 'content', 'price', 'image_field', 'author', 'category')
"""