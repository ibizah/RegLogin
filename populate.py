import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','demo.settings')

import django
django.setup()

from faker import Faker
from demoapp.models import Employee
fake= Faker()

def populte(N):
    for i in range(N):

        fake_name= fake.name()
        fake_email=fake.email()
        fake_age= fake.zipcode()[:1]

        employee= Employee.objects.get_or_create(fname=fake_name,email=fake_email,age=fake_age)[0]

if __name__=='__main__':
    print('start populating')
    populte(5)
    print('population finished')
