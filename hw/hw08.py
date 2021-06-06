# Inheritance

class Error:
    """
    >>> err1 = Error(12, "error.py")
    >>> err1.write()
    error.py:12
    """
    def __init__(self, line, file):
        "*** YOUR CODE HERE ***"
        self.line = line
        self.file = file

    def format(self):
        return self.file + ':' + str(self.line)

    def write(self):
        print(self.format())

class SyntaxError(Error):
    """
    >>> err1 = SyntaxError(17, "lab10.py")
    >>> err1.write()
    lab10.py:17 SyntaxError : Invalid syntax
    >>> err1.add_code(4, "EOL while scanning string literal")
    >>> err2 = SyntaxError(18, "lab10.py", 4)
    >>> err2.write()
    lab10.py:18 SyntaxError : EOL while scanning string literal
    """
    type = 'SyntaxError'
    msgs = {0 : "Invalid syntax", 1: "Unmatched parentheses", 2: "Incorrect indentation", 3: "missing colon"}

    def __init__(self, line, file, code=0):
        "*** YOUR CODE HERE ***"
        self.line = line
        self.file = file
        self.code = code

    def format(self):
        "*** YOUR CODE HERE ***"
        return self.file + ':' + str(self.line) + ' ' + self.type + " : " + self.msgs[self.code]

    def add_code(self, code, msg):
        "*** YOUR CODE HERE ***"
        self.msgs[code] = msg


class ZeroDivisionError(Error):
    """
    >>> err1 = ZeroDivisionError(273, "lab10.py")
    >>> err1.write()
    lab10.py:273 ZeroDivisionError : division by zero
    """
    type = 'ZeroDivisionError'

    def __init__(self, line, file, message='division by zero'):
        "*** YOUR CODE HERE ***"
        self.line = line
        self.file = file
        self.message = message

    def format(self):
        end = self.type + ' : ' + self.message
        "*** YOUR CODE HERE ***"
        return self.file + ':' + str(self.line) + ' ' + end


def make_test_random():
    """A deterministic random function that cycles between
    [0.0, 0.1, 0.2, ..., 0.9] for testing purposes.

    >>> random = make_test_random()
    >>> random()
    0.0
    >>> random()
    0.1
    >>> random2 = make_test_random()
    >>> random2()
    0.0
    """
    rands = [x / 10 for x in range(10)]
    def random():
        rand = rands[0]
        rands.append(rands.pop(0))
        return rand
    return random

def reset_random():
    global random
    random = make_test_random()

random = make_test_random()

### Phase 1: The Player Class
class Player:
    """
    >>> reset_random()
    >>> p1 = Player('Hill')
    >>> p2 = Player('Don')
    >>> p1.popularity
    100
    >>> p1.debate(p2)  # random() should return 0.0
    >>> p1.popularity
    150
    >>> p2.popularity
    100
    >>> p2.votes
    0
    >>> p2.speech(p1)
    >>> p2.votes
    10
    >>> p2.popularity
    110
    >>> p1.popularity
    135
    >>> # Additional correctness tests
    >>> p1.speech(p2)
    >>> p1.votes
    13
    >>> p1.popularity
    148
    >>> p2.votes
    10
    >>> p2.popularity
    99
    >>> for _ in range(4):  # 0.1, 0.2, 0.3, 0.4
    ...     p1.debate(p2)
    >>> p2.debate(p1)
    >>> p2.popularity
    49
    >>> p2.debate(p1)
    >>> p2.popularity
    0
    """
    def __init__(self, name):
        self.name = name
        self.votes = 0
        self.popularity = 100

    def debate(self, other):
        "*** YOUR CODE HERE ***"
        if random() < max(0.1, self.popularity / (self.popularity + other.popularity)):
            self.popularity += 50
        else:
            self.popularity -= 50
        if self.votes == 50:
            return self.votes
        if other.votes == 50:
            return other.votes
        if self.votes < 0:
            self.votes = 0
        if other.votes < 0:
            other.votes
        if self.popularity < 0:
            self.popularity = 0
        if other.popularity < 0:
            other.popularity = 0


    def speech(self, other):
        "*** YOUR CODE HERE ***"
        if self.votes == 50:
            return self.votes
        if other.votes == 50:
            return other.votes
        if self.votes < 0:
            self.votes = 0
        if other.votes < 0:
            other.votes
        if self.popularity < 0:
            self.popularity = 0
        if other.popularity < 0:
            other.popularity = 0
        self.votes += self.popularity // 10
        self.popularity += self.popularity // 10
        other.popularity -= other.popularity // 10

    def choose(self, other):
        return self.speech


### Phase 2: The Game Class
class Game:
    """
    >>> p1, p2 = Player('Hill'), Player('Don')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True
    >>> # Additional correctness tests
    >>> winner is g.winner
    True
    >>> g.turn
    10
    >>> p1.votes = p2.votes
    >>> print(g.winner)
    None
    """
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.turn = 0

    def play(self):
        while not self.game_over:
            "*** YOUR CODE HERE ***"
            self.p1.choose(self.p2)(self.p2)
            self.turn += 1
            self.p2.choose(self.p1)(self.p1)
            self.turn += 1
        return self.winner

    @property
    def game_over(self):
        return max(self.p1.votes, self.p2.votes) >= 50 or self.turn >= 10

    @property
    def winner(self):
        "*** YOUR CODE HERE ***"
        if self.p1.votes > self.p2.votes:
            return self.p1
        elif self.p1.votes < self.p2.votes:
            return self.p2
        else:
            return None

### Phase 3: New Players
class AggressivePlayer(Player):
    """
    >>> reset_random()
    >>> p1, p2 = AggressivePlayer('Don'), Player('Hill')
    >>> g = Game(p1, p2)
    >>> winner = g.play()
    >>> p1 is winner
    True
    >>> # Additional correctness tests
    >>> p1.popularity = p2.popularity
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity += 1
    >>> p1.choose(p2) == p1.debate
    False
    >>> p2.choose(p1) == p2.speech
    True
    """
    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity <= other.popularity:
            return self.debate
        else:
            return self.speech

class CautiousPlayer(Player):
    """
    >>> reset_random()
    >>> p1, p2 = CautiousPlayer('Hill'), AggressivePlayer('Don')
    >>> p1.popularity = 0
    >>> p1.choose(p2) == p1.debate
    True
    >>> p1.popularity = 1
    >>> p1.choose(p2) == p1.debate
    False
    >>> # Additional correctness tests
    >>> p2.choose(p1) == p2.speech
    True
    """
    def choose(self, other):
        "*** YOUR CODE HERE ***"
        if self.popularity == 0:
            return self.debate
        else:
            return self.speech
