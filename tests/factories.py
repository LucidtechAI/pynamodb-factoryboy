from factory import faker
from faker.providers import BaseProvider
from pynamodb_factoryboy import PynamoDBFactory
from .models import TestModel


class FakeProvider(BaseProvider):
    __provider__ = 'pynamodb'

    def binary_set(self):
        return {x.encode() for x in self.generator.words()}


faker.Faker.add_provider(FakeProvider)


class TestFactory(PynamoDBFactory):
    class Meta:
        model = TestModel

    unicode_attr = faker.Faker('sentence')
    binary_attr = faker.Faker('binary', length=100)
    binary_set_attr = faker.Faker('binary_set')
    boolean_attr = faker.Faker('boolean')
