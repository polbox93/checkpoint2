from csv import *
from address import Address
from work_address import WorkAddress


class AddressBook():

    def __init__(self, name):
        self.name = name
        self.addresses = []


    def add_address(self, address):

        if isinstance(address, Address):
            self.addresses.append(address)
        else:
            raise TypeError('Address object must be an instance of Address class')
