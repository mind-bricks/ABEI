from .procedure import (
    abstractmethod,
    IService,
)


class IProcedureData(IService):
    @abstractmethod
    def clone(self):
        """
        clone current procedure data
        :return:
        """

    @abstractmethod
    def get_signature(self):
        """
        get signature of procedure data
        :return:
        """

    @abstractmethod
    def get_label(self):
        """
        get label of procedure data
        :return:
        """

    @abstractmethod
    def get_value(self):
        """
        get data value
        :return:
        """

    @abstractmethod
    def set_value(self, value):
        """
        set data value
        :param value:
        :return:
        """


class IProcedureDataFactory(IService):

    @abstractmethod
    def create(self, signature, **kwargs):
        """
        create data
        :param signature:
        :param kwargs:
        :return:
        """

    @abstractmethod
    def register_class(self, signature, procedure_data_class, **kwargs):
        """
        :param signature:
        :param procedure_data_class:
        :param kwargs:
        :return:
        """

    @abstractmethod
    def iterate_classes(self):
        """
        :return:
        """
