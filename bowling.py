
class Bowling:
    name = []

    def set_bowler(self, bowler_name):
        self.name.append(bowler_name)
        return len(self.name) - 1

    def get_bowler(self, bowler_id):
        if bowler_id >= len(self.name):
            return 'There is no such bowler'
        return self.name[bowler_id]


if __name__ == '__main__':
    GAME = Bowling()
    BOWLER1_NAME = 'Travis'
    BOWLER1_ID = GAME.set_bowler(BOWLER1_NAME)
    print('User {} has been added with id {}'.format(BOWLER1_NAME, BOWLER1_ID))
    print('User associated with id 0 is ', GAME.get_bowler(BOWLER1_ID))
