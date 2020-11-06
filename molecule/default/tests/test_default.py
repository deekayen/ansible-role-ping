import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_saltstack_installed(host):
    assert host.package("firewalld").is_installed


def test_saltstack_service(host):
    service = host.service("firewalld")

    assert service.is_enabled
    assert service.is_running
