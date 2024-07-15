from django.shortcuts import render

# Create your views here.
d={'a':100,'b':50000,'c':800}
def iff(request):
    return render(request,'iff.html',d)