from django.shortcuts import render
from django.http import HttpResponse


projects_list = [
    {
        'id':'1',
        'title':'Ecommerce website',
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'Portfolio website',
        'description':'This is my portfolio'
    },
    {
        'id':'3',
        'title':'Social network',
        'description':'Remember facebook?'
    },
]

def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projects_list}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projects_list:
        if i['id'] == str(pk):
            projectObj = i
    return render(request, 'projects/single-projects.html', {'project': projectObj})