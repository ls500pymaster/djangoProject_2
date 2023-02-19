from .tasks import send_feedback_email_task
from django import forms
from django import forms

from .tasks import send_feedback_email_task


# class ScheduleEmailForm(forms.Form):
#     # name = forms.CharField(label='Name', max_length=100)
#     # email = forms.EmailField(label='Email', max_length=100)
#     # subject = forms.CharField(label='Subject', max_length=100)
#     # message = forms.CharField(label='Message', widget=forms.Textarea)
#     # date = forms.DateTimeField(label='Date and Time', input_formats=['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#
#     def send_email(self, date):
#         # name = [self.cleaned_data['name']]
#         # email = self.cleaned_data['email']
#         # subject = self.cleaned_data['subject']
#         # message = self.cleaned_data['message']
#         # date_at = self.cleaned_data['date']
#         send_feedback_email_task.apply_async(**date)