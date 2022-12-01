import random
from datetime import datetime

from django.core.management.base import BaseCommand

from app_staff.models import Part, Worker

GENDER = ['male', 'female']

FIRST_NAMES_WOMAN = ['Ольга', 'Елена', 'Марина', 'Екатерина', 'Светлана']
FIRST_NAMES_MAN = ['Игорь', 'Олег', 'Иван', 'Владимир', 'Евгений']
MIDDLE_NAMES_WOMAN = ['Игоревна', 'Олеговна', 'Владимировна', 'Евгеньевна', 'Петровна']
MIDDLE_NAMES_MAN = ['Игоревич', 'Олегович', 'Владимирович', 'Евгеньевич', 'Петрович']
LAST_NAMES = ['Пономаренко', 'Шевченко', 'Владиченко', 'Сидоренко', 'Жук', 'Волк', 'Заяц', 'Пчела', 'Оса', 'Рыба',
              'Кот']

JOBS = ['управляющий', 'глава', 'начальник', 'секретарь', 'стажер', 'менеджер', 'помощник']

DATE_NOW = datetime.today()


def create_workers():
    parts_id = list(Part.objects.values_list('id', flat=True))
    for part_id in parts_id:
        part = Part.objects.get(id=part_id)
        for i in range(1, 67):
            gender = random.choice(GENDER)
            if gender == 'male':
                first_name = random.choice(FIRST_NAMES_MAN)
                middle_name = random.choice(MIDDLE_NAMES_MAN)
                last_name = random.choice(LAST_NAMES)
            else:
                first_name = random.choice(FIRST_NAMES_WOMAN)
                middle_name = random.choice(MIDDLE_NAMES_WOMAN)
                last_name = random.choice(LAST_NAMES)
            name = f'{first_name} {middle_name} {last_name}'
            job_title = random.choice(JOBS)
            salary = random.randrange(40000, 10000000, 100)

            Worker.objects.create(
                name=name,
                job_title=job_title,
                date_start=DATE_NOW,
                salary=salary,
                part=part,
            )


def create_parts():
    part1 = Part.objects.create(
        name='Администрация',
        parent=None
    )

    for number_part2 in range(1, 10):
        part2 = Part.objects.create(
            name=f'Департамент {number_part2}',
            parent=part1
        )
        for number_part3 in range(1, 5):
            part3 = Part.objects.create(
                name=f'Управление {number_part3}',
                parent=part2
            )
            for number_part4 in range(1, 5):
                part4 = Part.objects.create(
                    name=f'Отдел {number_part4}',
                    parent=part3
                )
                for number_part5 in range(1, 5):
                    Part.objects.create(
                        name=f'Сектор {number_part5}',
                        parent=part4
                    )


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_parts()
        create_workers()
