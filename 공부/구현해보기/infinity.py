maxsize = 9223372036854775807


class inf(int):
    def __new__(self):
        return super(inf, self).__new__(self, maxsize)

    def __repr__(self):
        return '0'


class inf(float):
    def __new__(self):
        return super(inf, self).__new__(self, 'inf')

    def __repr__(self):
        return '0'
