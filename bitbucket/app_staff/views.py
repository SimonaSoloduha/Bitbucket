from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from app_staff.forms import WorkerForm, PartForm
from app_staff.models import Worker, Part


class WorkerListView(ListView):
    model = Worker
    template_name = 'staff/worker_list.html'
    context_object_name = 'worker_list'
    queryset = Worker.objects.order_by('-date_start')


class WorkerCreateView(CreateView):
    model = Worker
    template_name = 'staff/worker_create.html'
    fields = ['name', 'job_title', 'date_start', 'salary', 'part']


class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'staff/worker_detail.html'
    fields = ['name', 'job_title', 'date_start', 'salary', 'part']


class WorkerEditView(UpdateView):

    def get(self, request, id):
        worker = Worker.objects.get(id=id)
        form = WorkerForm(instance=worker)

        return render(
            request,
            'staff/worker_edit.html',
            context={
                'form': form,
                'worker_id': worker.id,
            }
        )

    def post(self, request, id):
        worker = Worker.objects.get(id=id)
        form = WorkerForm(request.POST, instance=worker)

        if form.is_valid():
            worker.save()
            return redirect('worker_detail', pk=id)


class PartListView(ListView):
    model = Part
    template_name = 'staff/part_list.html'
    context_object_name = 'part_list'
    queryset = Part.objects.all()


class PartCreateView(CreateView):
    model = Part
    template_name = 'staff/part_create.html'
    fields = ['name', 'parent']


class PartDetailView(DetailView):
    model = Part
    template_name = 'staff/part_detail.html'
    fields = ['name', 'job_title', 'date_start', 'salary', 'part']


class PartEditView(UpdateView):

    def get(self, request, id):
        part = Part.objects.get(id=id)
        form = PartForm(instance=part)

        return render(
            request,
            'staff/part_edit.html',
            context={
                'form': form,
                'part_id': part.id,
            }
        )

    def post(self, request, id):
        part = Part.objects.get(id=id)
        form = PartForm(request.POST, instance=part)

        if form.is_valid():
            part.save()
            return redirect('part_detail', pk=id)


def show_parts_and_workers(request):
    parts_and_workers = Part.objects.prefetch_related('worker').all()

    return render(request, "staff/parts_and_workers.html", {'parts_and_workers': parts_and_workers})
