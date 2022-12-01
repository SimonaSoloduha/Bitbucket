from django.urls import path

from app_staff.views import WorkerListView, WorkerCreateView, WorkerDetailView, WorkerEditView, PartListView, \
    PartCreateView, PartDetailView, PartEditView, show_parts_and_workers

urlpatterns = [
    path('', WorkerListView.as_view(), name='worker_list'),
    path('create/', WorkerCreateView.as_view(), name='worker_create'),
    path('<int:pk>/', WorkerDetailView.as_view(), name='worker_detail'),
    path('<slug:id>/edit/', WorkerEditView.as_view(), name='worker_edit'),
    path('part/', PartListView.as_view(), name='part_list'),
    path('part/create/', PartCreateView.as_view(), name='part_create'),
    path('part/<int:pk>/', PartDetailView.as_view(), name='part_detail'),
    path('part/<slug:id>/edit/', PartEditView.as_view(), name='part_edit'),
    path('all/', show_parts_and_workers, name='parts_and_workers'),
]
