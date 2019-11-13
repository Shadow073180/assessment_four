from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import User_Profile,Pet_Profile,Questionaire,Match
from .forms import User_ProfileForm, Pet_ProfileForm, QuestionaireForm, MatchForm


# -------------------------User
def user_profile_list(request):
    user_profiles = User_Profile.objects.all()
    return render(request, './users/user_profile_list.html', {'user_profiles':user_profiles})

def user_profile_detail(request, user_profile_id):
    user_profile = get_object_or_404('User_Profile', user_profile_id)
    return render(request, './users/user_profile_detail.html', {'user_profile':user_profile})

def new_user_profile(request):
    if request.method == 'POST':
        form = User_ProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.save()
        return redirect('user_profile_detail', user_profile_id=user_profile.id)
    else:
        form = User_ProfileForm()
    return render(request, './users/user_profile_form.html', {'form': form, 'type_of_request': 'New'} )

def edit_user_profile(request, user_profile_id):
    user_profile = get_object_or_404('User_Profile', id = user_profile_id)
    if request.method == 'POST':
        form = User_ProfileForm(request.POST, instance=user_profile)
        user_profile.save()
        return redirect('user_profile_detail', user_profile_id=user_profile.id)
    else:
        form = User_ProfileForm(instance=user)
    return render(request, './users/user_profile_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_user_profile(request, user_profile_id):
    if request.method == 'POST':
        user_profile = get_object_or_404('User_Profile', id=user_profile_id)
        user_profile.delete()
    return redirect('user_profile_list')





