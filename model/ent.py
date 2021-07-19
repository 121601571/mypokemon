import sys, os
import util.idgen


class entbase():
    def __init__(self, name, type1, meta):
        self.id = util.idgen.getuuid()
        self.name = name
        self.type = type1
        self.meta = meta

    def __str__(self):
        return str(self.name) + ' ' + str(self.type) + ' ' + str(self.meta)


