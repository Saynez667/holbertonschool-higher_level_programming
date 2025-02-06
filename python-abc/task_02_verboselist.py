#!/usr/bin/env python3


class VerboseList(list):

    def append(self, object):
        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value):
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        if index == -1:
            count = len(self) - 1
            pop = super().pop(count)
            print(f"Popped [{pop}] from the list.")
        else:
            pop = super().pop(index)
            print(f"Popped [{pop}] from the list.")
