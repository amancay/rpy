class AudioEvent(object):
    def __init__(self, priority, cmd, val):
        self.priority = priority
        self.cmd = cmd
        self.val = val
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)
