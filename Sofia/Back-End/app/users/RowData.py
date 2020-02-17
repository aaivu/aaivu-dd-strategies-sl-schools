from mongoengine import *


class RowData(Document):
    name = StringField()
    data = MapField(field=StringField())


def test_update():

    pass
