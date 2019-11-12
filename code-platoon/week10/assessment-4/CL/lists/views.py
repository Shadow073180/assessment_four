from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Catagory, Post
from .forms import CatagoryForm, PostForm

# Create your views here.
def catagory_list(request):
    catagories = Catagory.objects.all()
    return render(request, './catagories/catagory_list.html', {'catagories': catagories})


def new_catagory(request):
    if request.method == "POST":
        form = CatagoryForm(request.POST)
        if form.is_valid():
            catagory = form.save(commit=False)
            catagory.save()
            return redirect('catagory_detail', catagory_id=catagory.id)
    else:
        form = CatagoryForm()
    return render(request, './catagories/catagory_form.html', {'form': form, 'type_of_request': 'New'})

def catagory_detail(request, catagory_id):
    catagory = get_object_or_404(Catagory, id=catagory_id)
    return render(request, './catagories/catagory_detail.html', {'catagory': catagory})

def edit_catagory(request, catagory_id):
    catagory = get_object_or_404(Catagory, id=catagory_id)
    if request.method == "POST":
        form = CatagoryForm(request.POST, instance=catagory)
        if form.is_valid():
            catagory = form.save(commit=False)
            catagory.save()
            return redirect('catagory_detail', catagory_id=catagory.id)
    else:
        form = CatagoryForm(instance=catagory)
    return render(request, 'catagories/catagory_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_catagory(request, catagory_id):
    if request.method == "POST":
        catagory = get_object_or_404(Catagory, id=catagory_id)
        catagory.delete()
    return redirect('catagory_list')   
