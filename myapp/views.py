# Create your views here.

# Import necessary classes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from myapp.models import Author, Book, Course, Topic
from myapp.forms import *
from django.shortcuts import get_object_or_404

def index(request):
    #global user
    #user = None
    courselist = Course.objects.all().order_by('title')[:10]
    #if request.session.has_key('user'):
    #    user = request.session["user"]
    if request.user.is_authenticated.value:
        print(request.user.first_name)
        return render(request, 'myapp/index.html', {'user': request.user, 'courselist': courselist})
    else:
        return render(request, 'myapp/index.html', {'user': None, 'courselist': courselist})

def about(request):
    #global user
    #if request.session.has_key('user'):
    #    user = request.session["user"]
    if request.user is not None:
        return render(request,'myapp/about.html', {'user': request.user})
    else:
        return render(request, 'myapp/about.html')

def detail(request,course_num):
    #global user
    courselist=get_object_or_404(Course,course_no=course_num)
    #if request.session.has_key('user'):
    #    user = request.session["user"]
    if request.user is not None:
        return render(request,'myapp/detail.html', {'user': request.user, 'courselist': courselist })
    else:
        return render(request, 'myapp/detail.html', {'courselist': courselist})

def topics(request):
    #global user
    topiclist = Topic.objects.all()[:10]
    #if request.session.has_key('user'):
    #    user = request.session["user"]
    if request.user is not None:
        return render(request, 'myapp/topic.html', {'user': request.user, 'topiclist': topiclist})
    else:
        return render(request, 'myapp/topic.html', {'topiclist': topiclist})

def addtopic(request):
    #global user
    topiclist = Topic.objects.all()
    #user = request.session["user"]
    if(request.method=='POST'):
        form = TopicForm(request.POST)
        if(form.is_valid()):
            topic = form.save(commit=False)
            topic.num_responses = 1
            topic.save()
            return HttpResponseRedirect('/myapp/topics')
    else:
        form = TopicForm()
        if request.user is not None:
            return render(request, 'myapp/addtopic.html',{'user': request.user, 'form':form, 'topiclist':topiclist})
        else:
            return render(request, 'myapp/addtopic.html', {'form': form, 'topiclist': topiclist})

def topicdetail(request, topic_id):
    #global user
    topicdetails = Topic.objects.get(id=topic_id)
    #if request.session.has_key('user'):
    #    user = request.session["user"]
    if (request.method == 'POST'):
        form = InterestForm(request.POST)
        if (form.is_valid()):
            if (request.POST['interested'] == '1'):
                topicdetails.num_responses += 1;
                avg_age = (topicdetails.avg_age + int(request.POST['age'])) / 2
                topicdetails.avg_age = avg_age
                topicdetails.save()
        if request.user is not None:
            return render(request, 'myapp/topicdetail.html', {'user':request.user, 'topicdetails': topicdetails, 'form': form})
        else:
            return render(request, 'myapp/topicdetail.html', {'topicdetails': topicdetails, 'form': form})
    else:
        form = InterestForm()
        if request.user is not None:
            return render(request, 'myapp/topicdetail.html', {'user': request.user, 'topicdetails': topicdetails, 'form': form})
        else:
            return render(request, 'myapp/topicdetail.html', {'topicdetails': topicdetails, 'form': form})

def user_login(request):
    #global user
    #user = None
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #request.session["user"] = user
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        if request.user is not None:
            return render(request, 'myapp/login.html', {'user': request.user})
        else:
            return render(request, 'myapp/login.html')

@login_required(login_url='/myapp/index')
def user_logout(request):
    #global user
    logout(request)
    #if request.session.has_key('user'):
    #    del request.session['user']
    return render(request, 'myapp/logout.html')

def register(request):
    return render(request, 'myapp/register.html')

# Create your views here.
"""def index(request):
    #Courses
    courselist = Course.objects.all()[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of courses: ' + '</p>'
    response.write(heading1)
    for course in courselist:
        para = '<p>' + str(course) + '</p>'
        response.write(para)

    #Authors
    authorlist = Author.objects.filter().order_by('-birthdate')[:5]
    #response = HttpResponse()
    heading1 = '<p>' + 'List of Authors: ' + '</p>'
    response.write(heading1)
    response.write(str(type(authorlist)))
    for author in authorlist:
        para = '<p>' + str(author) + '</p>'
        response.write(para)

    return response
    return render(request, 'myapp/index0.html', {'courselist':courselist})

def about(request):
    response = HttpResponse()
    heading = 'This is a Course Listing APP.'
    response.write(heading)
    return render(request, 'myapp/about0.html')
    #return response

def detail(request, course_num):
    response = HttpResponse()
    heading = '<strong>Course details: <br/><br/></strong>'
    response.write(heading)
    #Print the course details
    #course_list = Course.objects.filter(course_no=course_num)[0]
    course_list = get_object_or_404(Course, course_no=course_num)
    response.write('Course Number: ' + str(course_list.course_no) + '<br/>Course Title: ' + str(course_list.title)
               + '<br/>Book Title: ' + str(course_list.textbook.title))
    return response
    return render(request, 'myapp/detail0.html', {'course': course_list})"""