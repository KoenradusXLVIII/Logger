import pytest
import logger


def test_default_log_level():
    log_client = logger.Client('test')
    assert log_client.get_log_level() == 'info'


def test_change_name():
    log_client = logger.Client('first_name')
    assert log_client.get_name() == 'first_name'
    log_client.set_name('second_name')
    assert log_client.get_name() == 'second_name'


def test_set_log_level_at_init():
    log_client = logger.Client('test', 'info')
    assert log_client.get_log_level() == 'info'
    log_client = logger.Client('test', 'debug')
    assert log_client.get_log_level() == 'debug'
    log_client = logger.Client('test', 'warning')
    assert log_client.get_log_level() == 'warning'
    log_client = logger.Client('test', 'error')
    assert log_client.get_log_level() == 'error'
    log_client = logger.Client('test', 'critical')
    assert log_client.get_log_level() == 'critical'


def test_set_log_level():
    log_client = logger.Client('test','critical')
    log_client.set_log_level('info')
    assert log_client.get_log_level() == 'info'
    log_client.set_log_level('debug')
    assert log_client.get_log_level() == 'debug'
    log_client.set_log_level('warning')
    assert log_client.get_log_level() == 'warning'
    log_client.set_log_level('error')
    assert log_client.get_log_level() == 'error'
    log_client.set_log_level('critical')
    assert log_client.get_log_level() == 'critical'
