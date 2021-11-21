from django.db import models
from api.constants import BASE_POWER

# Create your models here.


class SimpleUser(models.Model):
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username


class SimpleGroup(models.Model):
    group_name = models.CharField(max_length=50, unique=True)


class Power(models.Model):
    power = models.IntegerField()
    user = models.ForeignKey(to=SimpleUser, on_delete=models.CASCADE)
    group = models.ForeignKey(to=SimpleGroup, on_delete=models.CASCADE)


class Election(models.Model):
    group = models.ForeignKey(to=SimpleGroup, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)

    def propose(self, text, user: SimpleUser):
        """Makes a proposal, throws ValueError if not enough power"""
        group = self.group
        user_power = Power.objects.get(user=user, group=group)
        if user_power.power >= BASE_POWER:
            user_power.power -= BASE_POWER
            user_power.save()
            Proposal.objects.get_or_create(
                election=self, power=BASE_POWER, text=text)
        else:
            raise ValueError("not enough power")


class Proposal(models.Model):
    election = models.ForeignKey(to=Election, on_delete=models.CASCADE)
    power = models.IntegerField()
    text = models.CharField(max_length=50)

    def vote(self, user, power_to_add):
        """Adds power to this proposal, if user has enough. If not, ValueError"""
        group = self.election.group
        user_power = Power.objects.get(user=user, group=group)
        if user_power.power >= power_to_add:
            user_power.power -= power_to_add
            self.power += power_to_add
            user_power.save()
        else:
            raise ValueError("not enough power")
