from django.core.management.base import BaseCommand
from django.conf import settings

from octofit_tracker.db_utils import get_db

import random

USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel", "members": ["Iron Man", "Captain America", "Black Widow"]},
    {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
]

ACTIVITIES = [
    {"user": "Superman", "activity": "Flying", "duration": 120},
    {"user": "Batman", "activity": "Martial Arts", "duration": 90},
    {"user": "Wonder Woman", "activity": "Lasso Training", "duration": 60},
    {"user": "Iron Man", "activity": "Flight Suit Training", "duration": 80},
    {"user": "Captain America", "activity": "Shield Throwing", "duration": 70},
    {"user": "Black Widow", "activity": "Espionage", "duration": 100},
]

LEADERBOARD = [
    {"team": "Marvel", "points": 250},
    {"team": "DC", "points": 270},
]

WORKOUTS = [
    {"name": "Strength Training", "suggested_for": ["Superman", "Batman", "Iron Man"]},
    {"name": "Agility Drills", "suggested_for": ["Black Widow", "Wonder Woman", "Captain America"]},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = get_db()
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        db.users.create_index("email", unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
