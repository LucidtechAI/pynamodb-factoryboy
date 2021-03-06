import os

from pynamodb import attributes
from pynamodb.models import Model


class TestModel(Model):
    class Meta:
        table_name = 'test-table'
        host = os.environ['AWS_DYNAMODB_HOST']
        read_capacity_units = 10
        write_capacity_units = 10

    unicode_attr = attributes.UnicodeAttribute(hash_key=True)
