#
# Copyright oVirt Authors
# SPDX-License-Identifier: GPL-2.0-or-later
#
#

import pytest


@pytest.fixture(scope="session")
def system_service(engine_api):
    return engine_api.system_service()


@pytest.fixture(scope="session")
def hosts_service(system_service):
    return system_service.hosts_service()


@pytest.fixture(scope="session")
def disks_service(system_service):
    return system_service.disks_service()


@pytest.fixture(scope="session")
def events_service(system_service):
    return system_service.events_service()


@pytest.fixture(scope="session")
def networks_service(system_service):
    return system_service.networks_service()


@pytest.fixture(scope="session")
def storage_domains_service(system_service):
    return system_service.storage_domains_service()


@pytest.fixture(scope="session")
def templates_service(system_service):
    return system_service.templates_service()


@pytest.fixture(scope="session")
def vms_service(system_service):
    return system_service.vms_service()


@pytest.fixture(scope="session")
def get_vm_service_for_vm(vms_service):
    def service_for(vm_name):
        vms = vms_service.list(search='name={}'.format(vm_name))
        if len(vms) != 1:
            raise RuntimeError("Could not find vm: {}".format(vm_name))
        return vms_service.vm_service(vms[0].id)

    return service_for


@pytest.fixture(scope="session")
def users_service(system_service):
    return system_service.users_service()


@pytest.fixture(scope="session")
def get_user_service_for_user(users_service):
    def service_for(username):
        users = users_service.list(search=f'name={username}')
        if len(users) != 1:
            raise RuntimeError("Could not find user: {}".format(username))
        return users_service.user_service(users[0].id)

    return service_for