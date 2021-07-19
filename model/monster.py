import ent


class monster(ent.entbase):

    def __init__(self, name, type1, meta):
        super().__init__(name, type1, meta)



if __name__ == '__main__':
    a = monster(1,2,1)
    print(a)