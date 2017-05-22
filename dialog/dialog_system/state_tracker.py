class StateTracker:
    def __init__(self, vector=None):
        if vector is None:
            vector = []
        self.vector = vector

    def update(self, action):
        pass

    def step(self, action):
        pass

