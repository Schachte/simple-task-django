from django import forms
from .models import TaskItem
from crispy_forms.bootstrap import AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms.layout import Field
from django.contrib.auth.models import User

class TaskItemForm(forms.ModelForm):
    # task is changed to taskn
    taskn = forms.CharField(max_length = 300, required = True,)
    due_date = forms.CharField(max_length = 10, required = True,)
    # information = forms.TextField()
    def __init__(self, *args, **kwargs):
        super(TaskItemForm, self).__init__(*args, **kwargs)

        self.fields['taskn'].label = False
        self.fields['due_date'].label = False
      	
        self.helper = FormHelper()
        self.helper.layout = Layout(
        	PrependedText('taskn', 'Task', placeholder="Enter Task Here"),
            PrependedText('due_date', 'Due', placeholder="Select Due Date", id = "datepicker"),
            ButtonHolder(
                Submit('Submit', 'Submit', css_class='btn-primary' , css_id = "floater")
            ), 	  
        )

    # An inline class to provide additional information on the form.
    class Meta:
        fields = ('taskn', 'due_date')
        #This is the association between the model and the model form
        model = TaskItem

class AdvancedAddForm(forms.ModelForm):
    # task is changed to taskn
    taskn = forms.CharField(max_length = 300, required = True,)
    due_date = forms.CharField(max_length = 10, required = True,)
    due_time = forms.CharField(max_length = 7, required = False)
    information = forms.CharField(widget = forms.Textarea,  required = False)
    def __init__(self, *args, **kwargs):
        super(AdvancedAddForm, self).__init__(*args, **kwargs)

        self.fields['taskn'].label = False
        self.fields['due_date'].label = False
        self.fields['information'].label = False
        self.fields['due_time'].label = False
        
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
                PrependedText('taskn', 'Task', placeholder="Enter Task Here"),
                PrependedText('due_date', 'Due', placeholder="Select Due Date", id = "datepicker"),
                PrependedText('due_time', 'Time', placeholder="Select Due Time", id = "time"),
                'information',
                

            #PrependedText('information', 'information', placeholder="Additional Information"),
            ButtonHolder(
                Submit('Submit', 'Submit', css_class='btn-primary' , css_id = "floater")
            ),    
        )

    # An inline class to provide additional information on the form.
    class Meta:
        fields = ('taskn', 'due_date', 'due_time','information',)
        #This is the association between the model and the model form
        model = TaskItem

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            
            self.helper = FormHelper()
            self.helper.layout = Layout(
                'username',
                'password',
                ButtonHolder(
                    Submit('Submit', 'Submit', css_class='btn-primary' , css_id = "floater")
                ),    
            )
    class Meta:
        model = User
        fields = ('username', 'password')
