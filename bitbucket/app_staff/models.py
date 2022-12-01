from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Part(MPTTModel):
    name = models.CharField(max_length=150, verbose_name='name')
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='parent',
                            related_name='children')

    def get_absolute_url(self):
        return reverse('part_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name_plural = 'parts'
        verbose_name = 'part'

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    job_title = models.CharField(max_length=150, verbose_name='job_title')
    date_start = models.DateField(verbose_name='start_date')
    salary = models.PositiveIntegerField(verbose_name='salary')
    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name='workers', related_name='worker')

    def get_absolute_url(self):
        return reverse('worker_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name_plural = 'workers'
        verbose_name = 'worker'

    def __str__(self):
        return self.name
