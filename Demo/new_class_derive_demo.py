class Fa(object):
    def __init__(self):
        print('Father init')

class So(Fa):
    def __init__(self):
        super(So, self).__init__()
        print('Son init')

s = So()
