# views.py

from django.shortcuts import render
from .models import Job
from django.contrib.auth.forms import AuthenticationForm
# Create your views here
from django. contrib import messages
from .forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'index.html')

# employee or users section start...........................................................................................


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = form.save()
            user = authenticate(request, username=username,
                                password=password)  # for login
            # redirecting to login func for users
            return redirect('user_login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    messages.error(
                        request, 'Superuser cannot log in to user dashboard.')
                else:
                    login(request, user)
                    request.session['username'] = username  # create session
                    return redirect('empinfo')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'user_login.html', {'form': form})


def job_list(request):
    job_list = Job.objects.all()
    return render(request, 'home.html', {'job_list': job_list})


# views.py

from django.shortcuts import render
from .models import Candidate

def featured_candidates(request):
    featured_candidates = Candidate.objects.filter(featured=True)
    return render(request, 'home.html', {'featured_candidates': featured_candidates})


# views.py

from django.shortcuts import render, redirect
from .forms import CandidateApplicationForm
from .models import Job

def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        form = CandidateApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Associate the job with the candidate application
            application = form.save(commit=False)
            application.job_applied = job
            application.save()
            return redirect('job_list')  # Redirect to job listing page after successful application
    else:
        form = CandidateApplicationForm()
    
    return render(request, 'apply.html', {'form': form})



# views.py
from .models import *

from .forms import *

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'success_page' with the URL name of your success page.
    else:
        form = JobForm()

    return render(request, 'job_form.html', {'form': form})


def emplist(request):
    candi = Candidate.objects.all()
    return render(request, 'hire.html', {'candi': candi})


def empinfo(request):
    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('profile build sucess')
    else:
        form=EmpForm()
    return render(request,'empinfo.html',{'form': form})