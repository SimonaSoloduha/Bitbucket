from django.forms import ModelForm

from app_staff.models import Worker, Part


class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ('name', 'job_title', 'date_start', 'salary', 'part')


class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = ('name', 'parent')
