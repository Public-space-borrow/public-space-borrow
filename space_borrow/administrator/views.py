from django.shortcuts import render
#新加入的function
def printfunction(request):
    return render(request, "blacklist.html")