from .state_tracker import StateTracker


class DialogManager:
    def __init__(self, rounds=None, slot_tree=None, q_tree=None):
        if rounds is None:
            rounds = []

        self.rounds = rounds
        self.q_tree = q_tree
        self.slot_tree = slot_tree
        self.state_tracker = StateTracker()

    def append_round(self, rd):
        if isinstance(rd, Round):
            self.rounds.append(rd)

    def action(self):
        pass

    def reward(self):
        pass


class Round:
    def __init__(self, bot=None, human=None):
        if human is None:
            human = []
        if bot is None:
            bot = []

        self.bot = bot
        self.human = human
