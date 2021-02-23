from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from firstdbtest.models import Student
from django.template.context_processors import csrf
from django.views import generic

class StudentListView(generic.ListView):
	model = Student

def getstudentinfo(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('addstudentinfo.html', c)

def addstudentinfo(request):
	sname = request.POST.get('studentname', '')
	sdate = request.POST.get('birthdate', '')
	s = Student(student_name = sname, student_dob=sdate)
	s.save()
	return HttpResponseRedirect('/firstdbtest/addsuccess/')

def delstudentinfo(request):
	sname = request.POST.get('studentname', '')
	student = Student.objects.filter(student_name = sname)
	for s in student:
		s.delete()
	return render_to_response('delrecord.html')

def addsuccess(request):
	return render_to_response('addrecord.html')
