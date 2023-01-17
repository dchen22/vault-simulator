import _pickle as pickle

class S:

    def __init__(self):
        self.x = 0
        self.y = 0


class A:

    def __init__(self):
        self.arr = []

    def save(self):
        with open('testerpickle.pkl', 'wb') as acc_file:
            pickle.dump(self, acc_file)

    def load(self):
        with open('testerpickle.pkl', 'rb') as acc_file:
            pickle.load(acc_file)



with open('testerpickle.pkl', 'rb') as acc_file:
    v = pickle.load(acc_file)
    v.arr[0].x += 1
    print(v.arr[0].x)
    v.save()


