import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


""" tasks/main.yml tests """


@pytest.mark.parametrize('packages', [
    'python-pip',
    'python-openssl',
    'python-pyasn1',
    'setuptools',
    'ndg-httpsclient'
])
def test_file_paths_ubuntu1404(host, packages):
    if host.system_info.release == '14.04' \
            and host.system_info.distribution == 'Ubuntu':
        test_files = [packages]
        for x in test_files:
            assert host.package(x)


@pytest.mark.parametrize('packages', [
    'epel-release',
    'python-pip',
    'pyOpenSSL',
    'python-pyasn1',
    'python-setuptools',
    'python-urllib3'
])
def test_file_paths_centos6(host, packages):
    if host.system_info.release == '6' \
            and host.system_info.distribution == 'CentOS':
        test_files = [packages]
        for x in test_files:
            assert host.package(x)


@pytest.mark.parametrize('packages', [
    'epel-release',
    'python-pip',
    'pyOpenSSL',
    'python-pyasn1',
    'python-setuptools',
    'python-urllib3'
])
def test_file_paths_centos7(host, packages):
    if host.system_info.release == '7' \
            and host.system_info.distribution == 'CentOS':
        test_files = [packages]
        for x in test_files:
            assert host.package(x)
