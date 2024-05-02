
from application.models import enquiry_table
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

def home(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('message')

        info = enquiry_table(
            name=a,
            email=b,
            message=c
        )
        info.save()
    
        messages.success(request, 'Successfully Submitted')

        return render(request, 'index.html')
    else:  # Handle non-POST requests here
        # You might want to fetch any necessary data or perform actions for GET requests
        # For instance, fetch data from the database or perform other operations
        # Then render the 'index.html' template
        return render(request, 'index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # is not None is keyword None 'N' is capital which check above user (username and password) is available in database or not

            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
            # redirect('dashboard') - dashboard is a technical name not a path name, give technical name of that function from where dashboard.html page will render
            
            # from django.shortcuts import redirect, render - this module we need to import in same file, to access redirect() where only path name should be call
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')   
    return render(request,'login.html')

def dashboard_user(request):
    info = enquiry_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}
    return render(request, 'dashboard.html',data)
