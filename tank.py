import random


class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = ''
        self.target = (random.randrange(-5, 6), random.randrange(-5, 6))
        self.shots_right = 0
        self.shots_left = 0
        self.shots_up = 0
        self.shots_down = 0
        self.lucky_shots = 0
        self.score = 100
        self.all_shots = 0

    def move_up(self):
        if self.y < 5:
            self.y += 1
            self.direction = 'up'
            self.score -= 10
            print(f'You have moved {self.direction}')
        else:
            print('You are at the border. You can not move up anymore.')

    def move_down(self):
        if self.y > -5:
            self.y -= 1
            self.direction = 'down'
            self.score -= 10
            print(f'You have moved {self.direction}')
        else:
            print('You are at the border. You can not move down anymore.')

    def move_right(self):
        if self.x < 5:
            self.x += 1
            self.direction = 'right'
            self.score -= 10
            print(f'You have moved {self.direction}')
        else:
            print('You are at the border. You can not move right anymore.')

    def move_left(self):
        if self.x > -5:
            self.x -= 1
            self.direction = 'left'
            self.score -= 10
            print(f'You have moved {self.direction}')
        else:
            print('You are at the border. You can not move left anymore.')

    def get_info(self):
        print(f'The coordinates of tank are: ({self.x}, {self.y})\nDirection is: {self.direction}\n'
              f'Shots up: {self.shots_up}\nShots down: {self.shots_down}\nShots left: {self.shots_left}\n'
              f'Shots right: {self.shots_right}\nShots total: {self.all_shots}\nYour score: {self.score}')

    def set_new_target(self):
        self.target = (random.randrange(-5, 6), random.randrange(-5, 6))
        print(f'New target set: {self.target}')

    def shoot(self):
        if self.direction == 'up':
            if self.x == self.target[0] and self.y < self.target[1]:
                print('Lucky shot.')
                self.lucky_shots += 1
                self.score += 50
                self.set_new_target()
            else:
                print('You missed it. Try again.')
            self.shots_up += 1
            self.all_shots += 1

        if self.direction == 'right':
            if self.x < self.target[0] and self.y == self.target[1]:
                print('Lucky shot.')
                self.lucky_shots += 1
                self.score += 50
                self.set_new_target()
            else:
                print('You missed it. Try again.')
            self.shots_right += 1
            self.all_shots += 1

        if self.direction == 'left':
            if self.x > self.target[0] and self.y == self.target[1]:
                print('Lucky shot.')
                self.score += 50
                self.lucky_shots += 1
                self.set_new_target()
            else:
                print('You missed it. Try again.')
            self.shots_left += 1
            self.all_shots += 1

        if self.direction == 'down':
            if self.x == self.target[0] and self.y > self.target[1]:
                print('Lucky shot.')
                self.score += 50
                self.lucky_shots += 1
                self.set_new_target()
            else:
                print('You missed it. Try again.')
            self.shots_down += 1
            self.all_shots += 1


# instructions
print('Hello! This is the game of tank. The board is 10x10. You start '
      'at 0,0.\nYou start with score 100, with every move you lose 10 points, '
      'with every lucky shot you gain 50. Game stops at 0.\nTo move up, down, left or right '
      'press "u", "d", "l", or "r" accordingly.\nTo shoot, press "s" (You can only shoot in the '
      'direction you are standing.)\nTo see, where you are standing,'
      'press "i".\nTo quit, press "q"\nGood luck.')

tank = Tank()
print(f'Target is: {tank.target}')
moves = {
    'u': tank.move_up,
    'd': tank.move_down,
    'l': tank.move_left,
    'r': tank.move_right,
    'i': tank.get_info,
    't': tank.set_new_target,
    's': tank.shoot
}

while True:
    user_input = input('Your move: ')
    try:
        moves[user_input]()
    except KeyError:
        if user_input == 'q':
            print('Game finished.')
            break
        print('Enter a different value')

    if tank.score == 0:
        print(f'Sorry, your score is 0,the game is finished. You have had {tank.lucky_shots} lucky shots.')
        break
