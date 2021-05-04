# my file deep3072
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    print(extraspaceremover)
    punctuations = '''!()-[]{};"',<>./?@#$%^&*_\\~'''
    if removepunc == "on":
        analyzed = ''
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
    if fullcaps == "on":
        analyzed=''
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed + i.upper()
            else:
                analyzed=analyzed+i
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
    if newlineremover == "on":
        analyzed=''
        for i in djtext:
            if i != "\n" and i!="\r":
                analyzed=analyzed+i
        params = {'purpose': 'Removed New line', 'analyzed_text': analyzed}
        djtext=analyzed
    if extraspaceremover == "on":
        analyzed=''
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on" and removepunc != "on":
        return HttpResponse("<h1>Bhai koi operation select kar le!</h1> ")
    return render(request,'analyze.html',params)