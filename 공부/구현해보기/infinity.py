class float_inf(float):
    def __new__(self):
        return super(float_inf, self).__new__(self, 'inf')

    def __repr__(self):
        return '0'


class int_inf(int):
    def __new__(self):
        return super(int_inf, self).__new__(self, 9223372036854775807)

    def __repr__(self):
        return '0'
