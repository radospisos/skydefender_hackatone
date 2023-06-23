class Flags:
    def __init__(self):
        self.flags = {
        'tracking': False,
        'detection': False,
        }

    def set_flag(self, flag, value):
        self.flag_validation(flag)
        self.flags[flag] = bool(value)

    def get_flag(self, flag):
        self.flag_validation(flag)
        return self.flags[flag]

    def flag_validation(self, flag):
        if flag not in self.flags:
            raise ValueError('There is no such Orchestrator flag')

    def reset_ai_flags(self):
        self.flags['tracking'] = False
        self.flags['detection'] = False
