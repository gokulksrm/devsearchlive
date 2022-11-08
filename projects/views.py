from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Project
from .Forms import ProjectForm
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'fully functional ecommerce website'
    },
     {
        'id': '2',
        'title': 'Portfolio website',
        'description': 'A personal website to write articles and display'
    },
     {
        'id': '3',
        'title': 'Social Network',
        'description':'An open source project built by the community'
    }
]

def projects(request):
    projects=Project.objects.all()
    #print(project)
    context={'projects':projects}
    return render(request,'projects/projects.html',context)
def project(request,pk):
    projectobject=Project.objects.get(id=pk)
   # tags=projectobject.tags.all()
   # reviews=projectobject.review_set.all()
    context={'project':projectobject}
    return render(request,'projects/single-projects.html',context)
def CreateProject(request):
    form=ProjectForm()
    if request.method =='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context={'form':form}
    return render(request,'projects/project-form.html',context)
def UpdateProject(request,pk):
    project=Project.objects.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method == 'POST':
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context={'form':form}
    return render(request,'projects/project-form.html',context)
def DeleteProject(request,pk):
    project=Project.objects.get(id=pk)
    print(request.method)
    if request.method == 'POST':
        print('54254527576527576527657626424726476427624767647')
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request,'Projects/delete.html',context)
