from django import forms
from .models import Pizza,Size

# class PizzaForm(forms.Form):
#     topping1=forms.CharField(max_length=100,label="Topping 1")
#     topping2=forms.CharField(max_length=100,label="Topping 2")
#     size=forms.ChoiceField(label="Size", choices=[("Small","Small"),("Medium","Medium"),("Large","Large")])

#here we are using model to create forms 
# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model=Pizza
#         fields=['topping1','topping2','size']
#         labels={
#             'topping1':'Topping 1',
#             'topping2':'Topping 2',
#         }

class PizzaForm(forms.ModelForm):
    # size=forms.ModelChoiceField(queryset=Size.objects,empty_label=None,widget=forms.RadioSelect)
    class Meta:
        model=Pizza
        fields=['topping1','topping2','size']
        labels={
            'topping1':'Topping 1',
            'topping2':'Topping 2',
        }
       
class multiplepizzaform(forms.Form):
    number=forms.IntegerField(min_value=2,max_value=6)

# class PizzaForm(forms.ModelForm):
#     # size=forms.ModelChoiceField(queryset=Size.objects,empty_label=None,widget=forms.RadioSelect)
#     image=forms.ImageField()
#     class Meta:
#         model=Pizza
#         fields=['topping1','topping2','size']
#         labels={
#             'topping1':'Topping 1',
#             'topping2':'Topping 2',
#         }
        
# class PizzaForm(forms.Form):
#     topping1=forms.CharField(max_length=100,label="Topping 1",widget=forms.Textarea)
#     # topping1=forms.CharField(max_length=100,label="Topping 1",widget=forms.PasswordInput)
#     topping2=forms.CharField(max_length=100,label="Topping 2")
#     size=forms.ChoiceField(label="Size", choices=[("Small","Small"),("Medium","Medium"),("Large","Large")])

# class PizzaForm(forms.Form):
#     toppings=forms.MultipleChoiceField(choices=[('pep','Pepperoni'),('cheese','Cheese'),('olives','Olives')],widget=forms.CheckboxSelectMultiple)
#     size=forms.ChoiceField(label="Size", choices=[("Small","Small"),("Medium","Medium"),("Large","Large")])
