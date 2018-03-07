import datetime

from peewee import *


DATABASE = MySQLDatabase('flaskrestapi', user='root', password='')


class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Form(Model):
    libraryName = CharField(unique=True)
    libraryLocation = CharField()
    managerName = CharField()
    managerEmail = CharField()
    managerPhonenumber = CharField()
    capacityOfAudiences = IntegerField()
    facilities = CharField()
    requirementsForSpeaker = CharField(default="")
    personalInfoAgreement = BooleanField()
    noVolunteerAgreement = BooleanField()
    otherFacilities = CharField(default="")
    createdAt = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Review(Model):
    course = ForeignKeyField(Course, related_name='review_set')
    rating = IntegerField()
    comment = TextField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Course, Review, Form], safe=True)
    DATABASE.close()

