from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

user_list = []

def userreg(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user_list.append({'name': username, 'email': email, 'password': password})
        # print(user_list)
        return redirect(userlogin)
        
    return render(request,'userreg.html')

def userlogin(request):
     if request.method=='POST':
        email=request.POST['email']
        # username=request.POST['name']
        userpassword=request.POST['password']
        for i in user_list:                    
            if i['email']==email and i['password']==userpassword:
                print("logged in")
                return redirect(userhome)
     return render(request,'userlogin.html')
    


adminusername="adm123"
adminpassword="adm@123"
def admlogin(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        if username==adminusername and password==adminpassword:
            print("logged in")
            return redirect('admhome')
    return render(request,'admlogin.html')

def admhome(request):
    print(user_list)
    return render(request,'admhome.html', {'userreg': user_list})

def userhome(request):
    return render(request,'userhome.html',{'userreg': user_list})
