from __future__ import absolute_import
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views import generic
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import login as contrib_login, logout as contrib_logout
from django.conf import settings
from bkmks.forms import TaskItemForm, AdvancedAddForm, UserForm
from django.views.generic import CreateView
from bkmks.models import TaskItem
from bkmks.forms import TaskItemForm
from django.shortcuts import render_to_response, RequestContext, redirect, render
from .forms import TaskItemForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView # this is the generic view
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User


def deleter(request,username, id):

	if username == request.user.username:

		user = User.objects.get(username=username)

		ti = TaskItem.objects.get(pk = id)

		ti.delete()

		return redirect("/user/%s/overview" %(request.user.username))
	return HttpResponse('not deleted')


def main_page(request, **kwargs):
	context = RequestContext(request)
	if request.user.is_authenticated():
		return redirect('/user/%s' %(request.user))
	else:
		return render_to_response('base.html', {}, context)

class login_page(generic.TemplateView):
	template_name = 'login.html'

def profile_page(request, username):

	context = RequestContext(request)
	if username == request.user.username:
		if request.user.is_authenticated():
			user = User.objects.get(username=username)
			taskitems = request.user.taskitem_set.all()
			taskitems2 = request.user.taskitem_set.all().order_by('-created_date')[:3]


			if request.method == 'POST':
				form = TaskItemForm(request.POST)

				# Have we been provided with a valid form?
				if form.is_valid():
					# Save the new category to the database.
					task = form.save(commit=False)
					if not task.due_date:
						return HttpResponse('hi')
					task.usern = request.user
					task.save()
					return redirect("/user/%s/submitted" %(request.user.username))

			form = TaskItemForm()

			return render_to_response('profile.html', {'form':form, 'tasks': taskitems, 'tasks2': taskitems2, 'time':datetime.now(),}, context)
		else:
			return render_to_response('login.html', {}, context)
	else:
		return render_to_response('already.html', {}, context)

def user_login(request):
	# Like before, obtain the context for the user's request.
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/user/%s' %(username))

		else:
			# Bad login details were provided. So we can't log the user in.
			#print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render_to_response('login.html', {}, context)

def profile_overview(request, username):

	context = RequestContext(request)
	if username == request.user.username:
		if request.user.is_authenticated():
			user = User.objects.get(username=username)
			taskitems = request.user.taskitem_set.all()


			if request.method == 'POST':
				form = TaskItemForm(request.POST)

				# Have we been provided with a valid form?
				if form.is_valid():
					# Save the new category to the database.
					task = form.save(commit=False)
					task.usern = request.user
					task.save()

			form = TaskItemForm()

			return render_to_response('viewtasks.html', {'form':form, 'tasks': taskitems,'time':datetime.now(),}, context)
		else:
			return render_to_response('login.html', {}, context)
	else:
		return render_to_response('viewtasks.html', {}, context)


def adder(request, username):

	context = RequestContext(request)
	if username == request.user.username:
		if request.user.is_authenticated():
			user = User.objects.get(username=username)
			taskitems = request.user.taskitem_set.all()

			if request.method == 'POST':
				form = AdvancedAddForm(request.POST)

				# Have we been provided with a valid form?
				if form.is_valid():
					# Save the new category to the database.
					task = form.save(commit=False)
					task.usern = request.user
					task.save()
					return redirect("/user/%s/submitted" %(request.user.username))

			form = AdvancedAddForm()

			return render_to_response('addtask.html', {'form':form, 'tasks': taskitems, 'time':datetime.now(),}, context)
		else:
			return render_to_response('adk.html', {}, context)
	else:
		return render_to_response('addtadsk.html', {}, context)

def task_submission(request, username):
	#make sure the user is authenticated before they have access to view the submission page that is assocaited with their account
	context = RequestContext(request)

	if username == request.user.username:

		if request.user.is_authenticated():

			user = User.objects.get(username=username)
			taskitems = request.user.taskitem_set.all()
			return render_to_response('submission.html', {}, context)

	else:
		return render_to_response('login.html', {}, context)



# else:
#         book = Book.objects.get(pk = book_id)
#         book_form = BookForm(instance=book)

#         return render_to_response('editbook.html',{ 'form':book_form }, context_instance=RequestContext(request))


def register(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()


			# Update our variable to tell the template registration was successful.
			registered = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()


	# Render the template depending on the context.
	return render(request,
			'register.html',
			{'user_form': user_form,'registered': registered} )
