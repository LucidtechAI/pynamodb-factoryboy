import pytest

from pynamodb_factoryboy import __version__
from pytest_factoryboy import register, LazyFixture

from .factories import TestFactory
from .models import TestModel


register(TestFactory)


def test_simple(test_model):
    assert TestModel.count() == 1
    assert isinstance(test_model.unicode_attr, str)
    assert isinstance(test_model.binary_attr, bytes)
    assert isinstance(test_model.binary_set_attr, set)
    assert isinstance(test_model.boolean_attr, bool)


@pytest.mark.parametrize('value', ['asdf'])
@pytest.mark.parametrize('test_model__unicode_attr', [
    LazyFixture(lambda value: value),
])
def test_attributes_as_fixtures(test_model, value):
    assert test_model.unicode_attr == value
