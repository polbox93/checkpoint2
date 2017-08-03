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


    def find(self, search_phrase):
        results_list = []

        for element in self.addresses:
            if search_phrase.lower() in element.get_full_address().lower():
                results_list.append(element)

        return results_list
