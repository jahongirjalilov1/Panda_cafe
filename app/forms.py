from django.forms import ModelForm, forms

from app.models import Food, Chef, Contact


class FoodModelForm(ModelForm):

    class Meta:
        model = Food
        fields = '__all__'

class ChefModelForm(ModelForm):

    class Meta:
        model = Chef
        fields = '__all__'

class ContactModelForm(forms.Form):

    class Meta:
        model = Contact
        fields = '__all__'

