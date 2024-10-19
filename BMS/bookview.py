from django.shortcuts import render,redirect
from django.http import response
from book.models import Books
def book(request):
    bookData = Books.objects.all()
    if not request.session.get("success"): 
        bookData={
            "bookData":bookData
        }
    else:
        message = request.session.get("success")
        bookData={
            "bookData":bookData,
            "Message":message
        }
        del request.session["success"]
    return render(request,"book/index.html",bookData)

def view(request,id):
    bookData= Books.objects.get(id=id)
    print(id)
    data = {
        "bookData":bookData,
        "id":int(id)
    }
    return render(request,'book/view.html',data)


def delete(request,id):
    bookData= Books.objects.get(id=int(id))
    bookData.delete() 
    return redirect(book)

def edit(request, id):
    bookData = Books.objects.get(id=int(id))
    if request.method == "GET":
        return render(request, "book/edit.html", {"bookData": bookData})
    else:
        name = request.POST.get("b_name")
        author = request.POST.get("b_author")
        prize = request.POST.get("b_prize")  # Ensure this is not None or empty
        category = request.POST.get("b_category")
        
        # Ensure that all fields are being set before saving
        bookData.b_name = name
        bookData.b_author = author
        bookData.b_prize = prize  # This could be causing the issue if prize is None
        bookData.b_category = category
        bookData.save()

        return redirect(book)    

def Addbook(request):
    if request.method == "GET":
        return render(request,"book/addform.html")
    else:
        name = request.POST.get("b_name")
        author = request.POST.get("b_author")
        prize= request.POST.get("b_prize")
        category = request.POST.get("b_category")
        #pass models classs (eg.Books)
        saveData = Books( 
            b_name=name,
            b_author=author,
            b_prize=prize,
            b_category=category,
            )
        saveData.save()
        
        request.session["success"] = "Record added successfully!"
        return redirect(book)
