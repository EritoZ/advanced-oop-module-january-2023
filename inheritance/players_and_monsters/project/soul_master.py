from project.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):

    def __init__(self, username: str, level: int):
        DarkWizard.__init__(self, username, level)
