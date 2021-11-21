"""Test Models"""

from django.test import TestCase
from api.constants import STARTING_POWER

from api.models import Election, Power, SimpleGroup, SimpleUser


class TestCreation(TestCase):
    def setUp(self):
        dylan = SimpleUser.objects.create(username="dylan")
        akbar = SimpleUser.objects.create(username="akbar")
        frens = SimpleGroup.objects.create(group_name="frens")
        Power.objects.create(user=dylan, group=frens, power=STARTING_POWER)
        Power.objects.create(user=akbar, group=frens, power=STARTING_POWER)
        Election.objects.create(group=frens, question="Who is the best?")

    def test_existence(self):
        SimpleUser.objects.get(username="dylan")
        SimpleUser.objects.get(username="akbar")
        frens = SimpleGroup.objects.get(group_name="frens")
        Election.objects.get(group=frens, question="Who is the best?")
