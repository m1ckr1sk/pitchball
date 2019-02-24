class Ball:
    def  __init__(self):
        self.current_position = -1
        self.new_position = -1
        self.owned_by  = None
        self.current_state_served = False
        self.new_state_served = False

    def swap_buffers(self):
        self.current_position = self.new_position
        self.current_state_served = self.new_state_served