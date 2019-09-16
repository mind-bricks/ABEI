from abc import (
    ABC,
    abstractmethod,
)


def service_entry(interface, name=None):
    return ServiceEntry(interface, name)


class ServiceEntry(object):
    def __init__(self, interface, name):
        self.interface = interface
        self.name = name or ''


class IService(ABC):
    """
    the root interface for service
    """


class IServiceSite(ABC):
    @abstractmethod
    def get_service(self, entry):
        """
        get service instance by service entry
        raise exception if no service found
        """

    @abstractmethod
    def query_service(self, entry):
        """
        query service instance by service entry
        """

    @abstractmethod
    def register_service(self, entries, service_class, **kwargs):
        """
        register service with service entries
        """


class IServiceConfiguration(ABC):
    @abstractmethod
    def load_json(self, service_site, file_or_filename):
        """
        register service to service site by reading configuration file
        """

    @abstractmethod
    def save_json(self, service_site, file_or_filename):
        """
        save service from service site to configuration file
        """

    @abstractmethod
    def load_yaml(self, service_site, file_or_filename):
        """
        register service to service site by reading configuration file
        """

    @abstractmethod
    def save_yaml(self, service_site, file_or_filename):
        """
        save service from service site to configuration file
        """