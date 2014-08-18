import os.path

from service_wizard import config

HEALTHCHECKS = os.path.join('files', 'healthcheck', 'nail', 'sys',
                            'healthcheck', '_healthcheck_services')
SERVICEGROUPS = os.path.join('shared', 'prod-and-stage', 'servicegroups')
HOSTGROUPS = os.path.join('datacenters')
CHECKS = os.path.join('shared', 'prod-and-stage', 'services')


class SrvPathBuilder(object):
    """Builds paths to files in the puppet heirarchy for a given service."""

    def __init__(self, srvname, yelpsoa_config_root):
        self.srvname = srvname
        self.yelpsoa_config_root = yelpsoa_config_root

    @property
    def root_dir(self):
        return os.path.join(self.yelpsoa_config_root, self.srvname)

    def to_file(self, filename):
        """Return a filename under this service's directory"""
        return os.path.join(self.root_dir, filename)

    @property
    def healthcheck(self):
        """Path to the healthcheck for this service"""
        return os.path.join(
            config.PUPPET_ROOT, HEALTHCHECKS, self.srvname + '.py')

    @property
    def servicegroup(self):
        """Path to the servicegroup for this service"""
        return os.path.join(
            config.NAGIOS_ROOT, SERVICEGROUPS, 'soa.cfg')

    @property
    def hostgroup(self):
        """Path to the servicegroup for this service"""
        return os.path.join(
            config.NAGIOS_ROOT, HOSTGROUPS)

    @property
    def check(self):
        """Path to the check for this service"""
        return os.path.join(
            config.NAGIOS_ROOT, CHECKS, self.srvname + '.cfg')

    @property
    def service_yaml(self):
        """Path to the service.yaml for this service"""
        return os.path.join(
            self.root_dir, self.srvname + '.yaml')
