from time import sleep

import docker
import pytest


@pytest.fixture(autouse=True, scope='session')
def dynamodb_local():
    docker_client = docker.from_env()
    container = docker_client.containers.run(
        'amazon/dynamodb-local',
        ports={8000:8000},
        detach=True,
        remove=True,
    )

    try:
        sleep(2)
        yield container
    finally:
        container.stop()


@pytest.fixture(autouse=True, scope='session')
def create_tables(dynamodb_local):
    from .models import TestModel

    TestModel.create_table(wait=True)
    yield
    TestModel.delete_table()
