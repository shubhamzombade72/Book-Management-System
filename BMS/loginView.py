from django.shortcuts import render,redirect
from loginForms.models import Registration


def AddReg(request):
    if request.method == "POST":
       
        name = request.POST.get("name")
        username = request.POST.get("username")
        email= request.POST.get("email")
        mobno = request.POST.get("mobno")
        password = request.POST.get("password")
        conpassword = request.POST.get("conpassword")
       
        saveData = Registration( 
            name=name,
            username=username,
            email=email,
            mobno=mobno,
            password=password,
            conpassword=conpassword,
            )
        saveData.save()

        
        request.session["success"] = "Record added successfully!"
        return render(request,"logins/index.html")
    
# def login(request):
#      loginData= Registration.objects.get(id=id)
#      if request.method=="GET":
#          loginData=Registration