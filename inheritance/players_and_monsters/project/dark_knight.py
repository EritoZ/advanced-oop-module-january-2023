from project.knight import Knight


class DarkKnight(Knight):

    def __init__(self, username: str, level: int):
        Knight.__init__(self, username, level)
