import pytest

from pynamodb_factoryboy import __version__
from pytest_factoryboy import register

from .factories import TestFactory
from .models import TestModel


register(TestFactory)


def test_simple(test_model):
    assert TestModel.count() == 1
    assert isinstance(test_model.unicode_attr, str)


@pytest.mark.parametrize('test_model__unicode_attr', [
    'asdf',
])
def test_attributes_as_fixtures(test_model):
    assert test_model.unicode_attr == 'asdf'
