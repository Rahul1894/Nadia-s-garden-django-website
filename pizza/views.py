from django.shortcuts import render
from . import forms
from django.forms import formset_factory
from .models import Pizza


# Create your views here.
def home(request):
    return render(request,"pizza/home.html")

def order(request):
    multiple_form=forms.multiplepizzaform()
    if request.method == "POST":
        # filled_form=forms.PizzaForm(request.POST,request.FILES)  # the form filled by the user with values   #Request.files is necessary to submit when there's a file attached 
        filled_form=forms.PizzaForm(request.POST)
        if filled_form.is_valid():  # it returns true if there are no erros in filled forms 
            created_pizza=filled_form.save()
            created_pizza_pk=created_pizza.id
            note='Thanks for ordering!! Your %s %s and %s pizza on its way !!' %(filled_form.cleaned_data['size'],
            filled_form.cleaned_data['topping1'],
            filled_form.cleaned_data['topping2'],)    
            new_form=forms.PizzaForm()  
            return render(request,"pizza/order.html",{'created_pizza_pk':created_pizza_pk,'pizzaform':new_form,'note':note,'multiple_form':multiple_form})

    else:
        form=forms.PizzaForm()
        return render(request,"pizza/order.html",{'pizzaform':form, 'multiple_form':multiple_form})
    
def pizzas(request):
    number_of_pizzas=2
    filled_mutiple_pizza_form=forms.multiplepizzaform(request.GET)
    if filled_mutiple_pizza_form.is_valid():
        number_of_pizzas=(filled_mutiple_pizza_form.cleaned_data['number'])
    pizzaformset=formset_factory(forms.PizzaForm,extra=number_of_pizzas)
    formset=pizzaformset()
    if request.method=="POST":
        filled_formset=pizzaformset(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
                print(form.cleaned_data['topping1'])
            note="Pizza have been ordered"
        else:
            note="order was not created, please try again "
        return render(request,'pizza/pizzas.html',{'note':note,'formset':formset})
    else:
        return render(request,'pizza/pizzas.html',{'formset':formset})
    
def edit_order(request,pk):
    pizza=Pizza.objects.get(pk=pk)
    form=forms.PizzaForm(instance=pizza)
    note=''
    if request.method=="POST":
        filed_form=forms.PizzaForm(request.POST,instance=pizza)
        if filed_form.is_valid():
            filed_form.save()
            form=filed_form
            note='Pizza order have been edited'
        else:
            note='Pizza order not edited'
    return render(request,'pizza/edit_order.html',{'pizzaform':form,'pizza':pizza,'note':note})


## Let me explain this Django view function that handles editing a pizza order. I'll break it down step by step to help you understand what's happening.

# The function `edit_order` takes two parameters:
# - `request`: This contains all the information about the current HTTP request
# - `pk`: This stands for "primary key" and is used to identify which specific pizza order we want to edit

# First, we retrieve the specific pizza order from the database:
# ```python
# pizza = Pizza.objects.get(pk=pk)
# ```
# This line uses Django's ORM (Object-Relational Mapper) to fetch the pizza record that matches the provided primary key.

# Next, we create an initial form:
# ```python
# form = forms.PizzaForm(instance=pizza)
# ```
# This creates a form that's pre-populated with the current pizza's data. The `instance=pizza` parameter tells Django to fill the form fields with values from our pizza object.

# The function then checks if the request is a POST request:
# ```python
# if request.method == "POST":
# ```
# This is important because browsers typically send POST requests when submitting forms. When a user clicks the "submit" button, this condition will be true.

# If it is a POST request, we create a new form with the submitted data:
# ```python
# filed_form = forms.PizzaForm(request.POST, instance=pizza)
# ```
# Here we're creating another form, but this time with two parameters:
# - `request.POST`: Contains the data the user submitted
# - `instance=pizza`: Tells Django which existing pizza record to update

# We then validate the form:
# ```python
# if filed_form.is_valid():
#     filed_form.save()
#     form = filed_form
# ```
# If the submitted data is valid (meets all the requirements we've set), we:
# 1. Save the changes to the database with `filed_form.save()`
# 2. Update our `form` variable to show the new data

# Finally, we render the template:
# ```python
# return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza})
# ```
# This sends the response back to the browser, using the 'edit_order.html' template. We pass two pieces of information to the template:
# - `pizzaform`: The form (either empty, pre-filled, or with validation errors)
# - `pizza`: The pizza object itself, which might be useful for displaying additional information

# This view function handles both scenarios of the editing process:
# 1. When users first visit the page (GET request), they see the form filled with current pizza data
# 2. When users submit changes (POST request), the function either saves the changes and shows the updated form, or shows the form again with any validation errors

# This pattern is very common in Django applications and follows the principle of being "DRY" (Don't Repeat Yourself) by using the same view for both displaying and processing the form.