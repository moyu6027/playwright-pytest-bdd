@hotlink @Discovery
  Feature: As a new-monitor user,I can discovery snmp resources.

    Background:
      Given Sean has logged in

    Scenario Outline: Sean can discovery snmp resources
      When Sean wants to add snmp connection <connection_name> <port> <community>
      Then Sean should see <connection_name> in snmp connection list
      And I can delete snmp connection <connection_name>

      Examples:
        | connection_name   | port  | community |
        | snmp_connection_1 | 161   | xxxxx     |
        | vsu_connection_1  | 20003 | xxxxx     |
