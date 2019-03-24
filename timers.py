import time

class Timers():
    def __init__(self, items):
        self.timeouts = items
        self.timestamps = {}
        self.state = {}
        self.triggers = []

    def expired(self, id):
        now = time.time()
        if id not in self.state:
            print "added %s to states" % id
            self.state[id] = False
        if id not in self.timeouts:
            print "added %s to timeouts" % id
            self.timeouts[id] = 0
            self.state[id] = False

        if id not in self.timestamps:
            self.timestamps[id] = now
            return False
        elif id in self.triggers or (self.state[id] and now - self.timestamps[id] > 60 * self.timeouts[id]):
            if id in self.triggers:
                self.triggers.remove(id)
            self.timestamps[id] = now
            return True
        else:
            return False

    def get_state(self):
        return self.state

    def handle(self, state, triggers):
        if state is not None:
            for item in state:
                self.state[item] = state[item]

        if type(triggers) is list:
            self.triggers += triggers


#########################################################################

if __name__ == "__main__":
    timers = Timers({"One": 1, "Five": 5 })
    while True:
        if timers.expired("One"):
            print "One"
        if timers.expired("Five"):
            print "Five"
        time.sleep(10)
