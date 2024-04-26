class ListManager:
    def __init__(self, initial_list):
        self._list = initial_list

    def add_item(self, item):
        self._list.append(item)

    def remove_item(self, item):
        try:
            self._list.remove(item)
        except ValueError:
            print(f"{item} not found in the list.")

    def get_length(self):
        return len(self._list)

    def get_maximum_value(self):
        if self._list:
            return max(self._list)
        else:
            print("The list is empty.")

    def get_minimum_value(self):
        if self._list:
            return min(self._list)
        else:
            print("The list is empty.")

    def display_list(self):
        print("List contents:", self._list)

my_list = ListManager([10, 20, 30, 40, 50])

my_list.add_item(60)

my_list.remove_item(30)

print("Length of the list:", my_list.get_length())

print("Maximum value:", my_list.get_maximum_value())

print("Minimum value:", my_list.get_minimum_value())

my_list.display_list()