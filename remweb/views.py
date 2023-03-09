from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'ind.html')

def analyze(request):
    # Get the text
    abc = request.POST.get('text','default')
    # Check the checkbox values
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newline = request.POST.get('newline','off')
    space = request.POST.get('space','off')
    count = request.POST.get('count','off')
    # Performing the operation
    if removepunc=='on':
        punctuation ='''^.,*()$%#'@!~`_-":;|\?/<>'''
        pqr =" "
        for i in abc:
            if i not in punctuation:
                pqr = pqr + i
        dicty={'name':'Shubham','purpose':'removing punctuation','class':'FYCS','analysed_text':pqr}
        abc = pqr

    if capitalize=='on':
        if abc=="":
            return HttpResponse("Enter Something")
        else:
            pqr=abc.upper()
            dicty={'name':'Shubham','purpose':'Changing to upper case','class':'FYCS','analysed_text':pqr}
            abc = pqr
     
    if newline=='on':
        pqr=''
        for i in abc:
            if i != '\n' and i!='\r':
                pqr=pqr+i
        dicty={'name':'Shubham','purpose':'New Line Removing','class':'FYCS','analysed_text':pqr}
        abc = pqr

    if space=='on':
        pqr=''
        for index,i in enumerate(abc):
            if not(abc[index] == ' ' and abc[index+1]==" "):
                pqr=pqr+i
        dicty={'name':'Shubham','purpose':'Space Removing','class':'FYCS','analysed_text':pqr}
        abc = pqr

    if count=='on':
        pqr=len(abc)
        dicty={'name':'Shubham','purpose':'Character Counting','class':'FYCS','analysed_text':pqr}

    # If none of the checkbox is on perform operation        
    if (removepunc!='on' and capitalize != 'on' and newline != 'on' and space != 'on' and count != 'on'):
        return HttpResponse("You haven't clicked on any button, Please click on it!!!")
    return render(request,'analyzer.html',dicty)
