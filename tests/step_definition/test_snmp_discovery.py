"""As a new-monitor user,I can discovery snmp resources. feature tests."""
from pytest_bdd import (
    scenario, then, parsers, when,
)
from page_objects.connection_info.connection_info_page_object import ConnInfoPageObject


@scenario("snmp_discovery.feature", 'Sean can discovery snmp resources')
def test_sean_can_discovery_snmp_resources():
    """Sean can discovery all resources."""
    pass


@then(parsers.parse('Sean should see {connection_name} in snmp connection list'))
def check_snmp_connection_list(page, connection_name):
    """Sean should see snmp resources."""
    ConnInfoPageObject(page).check_snmp_connection_list(connection_name)


@then(parsers.parse('I can delete snmp connection {connection_name}'))
def delete_snmp_connection(page, connection_name):
    """I can delete snmp connection."""
    ConnInfoPageObject(page).delete_conn(connection_name)
