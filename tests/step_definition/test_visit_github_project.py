from pytest_bdd import scenario, then, parsers, when

from api_objects.github_object.test_api_object import TestApiObject


@scenario("visit_github_project.feature", 'Sean wants to visit github project.')
def test_sean_wants_to_visit_github_project():
    """Sean can visit."""
    pass


@when(parsers.parse('Sean visits github project'))
def visits_github_project(context):
    """Sean should see snmp resources."""
    TestApiObject(context).visit_github_project()
