from django.shortcuts import render
def home(request):
    result=1
    n1=6
    for i in range(1,n1+1,1):
        result=result*i
    return render(request,'app1/index.html',{'param1':result,'param2':n1})