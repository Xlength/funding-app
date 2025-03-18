from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FundingApplication
from .forms import FundingApplicationForm, UserUpdateForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 自动登录
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def apply_funding(request):
    if request.method == "POST":
        form = FundingApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect("funding_success")
    else:
        form = FundingApplicationForm()
    return render(request, "funding/apply_funding.html", {"form": form})

@login_required
def funding_success(request):
    return render(request, "funding/funding_success.html")

@login_required
def view_applications(request):
    applications = FundingApplication.objects.filter(user=request.user)
    return render(request, 'funding/view_applications.html', {'applications': applications})

@login_required
def review_funding(request):
    applications = FundingApplication.objects.filter(status='pending')
    return render(request, 'funding/review_funding.html', {'applications': applications})

@login_required
def approve_or_reject(request, application_id):
    application = get_object_or_404(FundingApplication, id=application_id)
    if request.method == "POST":
        if "approve" in request.POST:
            application.status = "approved"
        elif "reject" in request.POST:
            application.status = "rejected"
        application.save()
        return redirect("review_funding")
    return render(request, "funding/approve_or_reject.html", {"application": application})

@login_required
def dashboard(request):
    return render(request, "funding/dashboard.html")

@login_required
def user_settings(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)

        if 'update_info' in request.POST and user_form.is_valid():
            user_form.save()
            messages.success(request, "Your account information has been updated!")
            return redirect('user_settings')

        if 'change_password' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed!")
            return redirect('user_settings')
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'funding/settings.html', {
        'user_form': user_form,
        'password_form': password_form,
    })
