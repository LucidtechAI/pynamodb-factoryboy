import factory.fuzzy
from pynamodb_factoryboy import PynamoDBFactory
from .models import TestModel


class TestFactory(PynamoDBFactory):
    class Meta:
        model = TestModel

    unicode_attr = factory.fuzzy.FuzzyText()
