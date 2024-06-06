from django.http import HttpResponse

def mul_table(request,num):
    table=f"Table of {num}:<br>"

    for i in range(1,11):
        result=num*i 
        table += f"{num} x {i} = {result}<br>"
    return HttpResponse(table)
