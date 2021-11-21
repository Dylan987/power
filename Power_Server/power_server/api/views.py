from django.shortcuts import render

from django.http.response import HttpResponseBadRequest
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse

from api.constants import STARTING_POWER

import json

from api.models import Election, SimpleUser, SimpleGroup, Power, Proposal

# Create your views here.

def parse_json(req):
    return json.loads(req.body.decode('utf-8'))


@require_POST
def create_user(request):
    req = parse_json(request)
    username = req['username']
    SimpleUser.objects.get_or_create(username=username)
    return JsonResponse({
        "message": f"User {username} created successfully"
    }, status=201)


@require_GET
def list_user(_, username):
    """Returns info about a user. Name, groups, and powers"""
    try:
        user = SimpleUser.objects.get(username=username)
        powers = Power.objects.filter(user=user)
        data = {
            "username": user.username,
            "groups": []
        }
        for power in powers:
            data["groups"].append({
                "name": power.group.group_name,
                "power": power.power
            })
            if Election.objects.filter(group=power.group).count() > 0:
                data["groups"][-1]["election_id"] = Election.objects.get(
                    group=power.group).id

        return JsonResponse({
            "data": data
        })
    except SimpleUser.DoesNotExist:
        return JsonResponse({
            "error": f"User {username} not found"
        }, status=400)


@require_POST
def create_group(request):
    req = parse_json(request)
    group_name = req['group_name']
    SimpleGroup.objects.get_or_create(group_name=group_name)
    return JsonResponse({
        "message": f"Group {group_name} created successfully"
    }, status=201)


@require_POST
def add_user_to_group(request):
    req = parse_json(request)
    username = req['username']
    group_name = req['group_name']

    try:
        user = SimpleUser.objects.get(username=username)
        group = SimpleGroup.objects.get(group_name=group_name)
        Power.objects.get_or_create(
            user=user, group=group, power=STARTING_POWER)
        return JsonResponse({
            "message": f"User {username} added to group {group_name} with {STARTING_POWER} power"
        }, status=201)
    except SimpleUser.DoesNotExist:
        return JsonResponse({
            "error": f"User {username} not found"
        }, status=400)
    except SimpleGroup.DoesNotExist:
        return JsonResponse({
            "error": f"Group {group_name} not found"
        }, status=400)


@require_POST
def create_election(request):
    req = parse_json(request)
    group_name = req['group_name']
    question = req['question']

    try:
        group = SimpleGroup.objects.get(group_name=group_name)
        if Election.objects.filter(group=group).count() > 0:
            return JsonResponse({
                "error": f"Election already running in group {group_name}"
            }, status=400)
        Election.objects.get_or_create(group=group, question=question)
        return JsonResponse({
            "message": f"Election started in group {group_name} to discuss {question}"
        }, status=201)
    except SimpleGroup.DoesNotExist:
        return JsonResponse({
            "error": f"Group {group_name} does not exist"
        }, status=400)


@require_GET
def list_election(_, election_id):
    """Returns election state -- proposals and their power"""
    try:
        election = Election.objects.get(id=election_id)
        question = election.question
        data = {
            "question": question,
            "proposals": []
        }
        for proposal in Proposal.objects.filter(election=election):
            data['proposals'].append({
                "text": proposal.text,
                "power": proposal.power,
            })
        return JsonResponse({
            "data": data
        })
    except Election.DoesNotExist:
        return JsonResponse({
            "error": f"Election {election_id} not found"
        }, status=404)


@require_POST
def make_proposal(request, election_id):
    req = parse_json(request)
    username = req['username']
    option = req['option']

    try:
        user = SimpleUser.objects.get(username=username)
        election: Election = Election.objects.get(id=election_id)
        try:
            election.propose(option, user)
            return JsonResponse({
                "message": f"User {username} proposed {option}"
            }, status=201)
        except ValueError:
            return JsonResponse({
                "error": "User {username} doesn't have enough power"
            })
    except SimpleUser.DoesNotExist:
        return JsonResponse({
            "error": f"User {username} not found"
        }, status=400)
    except Election.DoesNotExist:
        return JsonResponse({
            "error": f"Election {election_id} not found"
        }, status=400)


@require_POST
def vote_in_election(request, election_id):
    req = parse_json(request)
    username = req['username']
    option = req['option']
    power = req['power']

    try:
        user = SimpleUser.objects.get(username=username)
        election = Election.objects.get(id=election_id)
        proposal: Proposal = Proposal.objects.get(
            election=election, text=option)
        try:
            proposal.vote(user, power)
            proposal.save()
            return JsonResponse({
                "message": f"User {username} voted for {option} with {power} power"
            }, status=201)
        except ValueError:
            return JsonResponse({
                "error": "User {username} doesn't have enough power"
            })
    except SimpleUser.DoesNotExist:
        return JsonResponse({
            "error": f"User {username} not found"
        }, status=400)
    except Election.DoesNotExist:
        return JsonResponse({
            "error": f"Election {election_id} not found"
        }, status=400)
    except Proposal.DoesNotExist:
        return JsonResponse({
            "error": f"Proposal {option} not found"
        }, status=400)
