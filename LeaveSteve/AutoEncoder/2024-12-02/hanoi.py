def move_everything_from_a(hanoi):
    # vvvvvvvv Your Code Here vvvvvvvv
    hanoi.move_from_to(Hanoi.A, Hanoi.B)
    hanoi.move_from_to(Hanoi.A, Hanoi.C)
    hanoi.move_from_to(Hanoi.B, Hanoi.C)
    hanoi.move_from_to(Hanoi.A, Hanoi.B)
    hanoi.move_from_to(Hanoi.C, Hanoi.A)
    hanoi.move_from_to(Hanoi.C, Hanoi.B)
    hanoi.move_from_to(Hanoi.A, Hanoi.B)
    # ^^^^^^^^ Your Code Here ^^^^^^^^

class Hanoi():
    # These are called "Class Variables"
    # Unlike instance variables, they are tied to the class as a whole, and
    # are shared by all instances.
    A = 'Hanoi.A'
    B = 'Hanoi.B'
    C = 'Hanoi.C'
    PEGS = [A, B, C]

    def __init__(self, number_of_disks):
        self.largest_disk = number_of_disks
        self.pegs = {
            Hanoi.A: list(range(number_of_disks, 0, -1)),
            Hanoi.B: [],
            Hanoi.C: [],
        }
    
    def move_from_to(self, peg_from, peg_to):
        if peg_from not in Hanoi.PEGS:
            raise ValueError(f'`peg_from` was {peg_from}, must be one of Hanoi.A, Hanoi.B, Hanoi.C')
        
        if peg_to not in Hanoi.PEGS:
            raise ValueError(f'`peg_to` was {peg_to}, must be one of Hanoi.A, Hanoi.B, Hanoi.C')

        peg_1 = self.pegs[peg_from]
        peg_2 = self.pegs[peg_to]

        if len(peg_1) == 0:
            raise ValueError(f'Cannot move elements from empty peg {peg_from}')

        if len(peg_2) == 0 or peg_2[-1] > peg_1[-1]:
            peg_2.append(peg_1.pop())
        else:
            raise RuntimeError(f'Disk {peg_1[-1]} cannot be placed on smaller disk of size {peg_2[-1]}')

        self.print_towers()
    
    def print_towers(self):
        def center(string, size=self.largest_disk*2+3, spacer=' '):
            while len(string) < size:
                string = string+spacer
                if len(string) < size:
                    string = spacer+string
            return string
        
        def disk_str(size):
            equalses = center(str(size), (2*size+1), '=')
            return center('['+equalses+']')
        
        string_lists = []
        for peg in Hanoi.PEGS:
            disks = self.pegs[peg]
            strings = []
            for disk in disks:
                strings.append(disk_str(disk))

            # Make the top of the peg stick out by at least one
            while len(strings) < self.largest_disk+1:
                strings.append(center('| |'))
            strings.reverse()

            strings.append(center(''))
            strings.append(center(peg.split('.')[1]))
            string_lists.append(strings)

        for line_strings in zip(*string_lists):
            print(' '.join(line_strings))
        
        input('\nPress Enter')

if __name__ == '__main__':
    game = Hanoi(4)
    game.print_towers()
    move_everything_from_a(game)