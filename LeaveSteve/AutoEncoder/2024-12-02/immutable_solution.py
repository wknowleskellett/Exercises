# vvvvvvvv Your Code Here vvvvvvvv

# Uncomment each of the sections below as you have coded the solution for them.

class ImmutableList():
    def __init__(self, starter_list):
        self.list = starter_list[:]

    def get(self, i):
        return self.list[i]

    def length(self):
        return len(self.list)

    def as_list(self):
        return self.list[:]

# ^^^^^^^^ Your Code Here ^^^^^^^^

if __name__ == '__main__':
    # Section 1
    folks = ImmutableList(['Myself', 'Carrie', 'Elliot'])
    
    # Section 2
    print('We\'ve got several folks:\n')
    for i, ordinal in enumerate(['first', 'second', 'third']):
        print(f'The {ordinal} one is {folks.get(i)}')
    
    # Section 3
    print(f'\nFor a total of {folks.length()} folks.')

    # Section 4
    print()
    print(folks.as_list())
