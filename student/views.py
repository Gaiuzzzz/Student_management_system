from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import SignUpForm


def home(request):
    return render(request, 'student/home.html')


def student_list(request):

    students = Student.objects.all()

    return render(request, 'student/student_list.html', {
        'students': students
    })


def signup(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            # Create the Django User
            user = form.save()

            # Get student information from the form
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            course = form.cleaned_data['course']

            # Create the Student profile
            Student.objects.create(
                user=user,
                name=name,
                email=user.email,
                phone=phone,
                course=course
            )

            # Log the user in
            login(request, user)

            # Go to dashboard
            return redirect('dashboard')

    else:
        form = SignUpForm()

    return render(request, 'student/signup.html', {
        'form': form
    })


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            return render(request, 'student/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'student/login.html')


@login_required
def dashboard(request):

    return render(request, 'student/dashboard.html')


def user_logout(request):

    logout(request)

    return redirect('home')