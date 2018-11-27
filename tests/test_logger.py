import pytest
import logger
names = {'first','second'}
log_levels = {'info','debug','warning','error','critical'}


@pytest.fixture
def log_client():
    return logger.Client('test')


def test_default_log_level(log_client):
    assert log_client.get_log_level() == 'info'


@pytest.mark.parametrize("name", names)
def test_change_name(log_client, name):
    log_client.set_name(name)
    assert log_client.get_name() == name


@pytest.mark.parametrize("log_level", log_levels)
def test_set_log_level_at_init(log_level):
    log_client = logger.Client('test', log_level)
    assert log_client.get_log_level() == log_level


@pytest.mark.parametrize("log_level", log_levels)
def test_set_log_level(log_client, log_level):
    log_client.set_log_level(log_level)
    assert log_client.get_log_level() == log_level
