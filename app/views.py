from django.shortcuts import render

# Create your views here.
def Jesus(request):
    dict={'Name':'Pujitha','Age':'22'}
    return render(request,'sample.html',dict)

