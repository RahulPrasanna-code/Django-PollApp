from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll

def index(request):
	polls = Poll.objects.all()
	context={
		'polls':polls
		}
	if request.method=="POST":
		primarykey=request.POST['deletebtn']
		deletepollobj=Poll.objects.get(pk=primarykey)
		deletepollobj.delete()
	return render(request,"home.html",context)

def create(request):
	if request.method == 'POST':
		form = CreatePollForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = CreatePollForm()

	context={
		'form':form
		}

	return render(request,'create.html',context)

def results(request):
	polls = Poll.objects.all()
	context={
		'polls':polls
	}
	return render(request,'result.html',context)

def vote(request,poll_id):
	poll = Poll.objects.get(pk=poll_id)
	if request.method =='POST':
		selected_option=request.POST['poll']
		if selected_option=='option1':
			poll.option1_count+=1
		elif selected_option=='option2':
			poll.option2_count+=1
		elif selected_option=='option3':
			poll.option3_count+=1
		else:
			return HttpResponse(400,"Ivalid form")

		poll.save()
		return redirect('detailedresult',poll_id)
	context={
		'poll':poll
		}
	return render(request,'vote.html',context)

def detailedresult(request,poll_id):
	poll = Poll.objects.get(pk=poll_id)
	context={
		'poll':poll
	}
	return render(request,'detailresult.html',context)