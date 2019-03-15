class Ball:
    def  __init__(self):
        self._current_position = -1
        self._previous_position = -1
        self._new_position = -1
        self._owned_by  = None
        self._current_state_served = False
        self._new_state_served = False

    def swap_buffers(self):
        self._previous_position = self._current_position
        self._current_position = self._new_position
        self._current_state_served = self._new_state_served

    @property
    def current_position(self):
        return self._current_position

    @current_position.setter
    def current_position(self, position):
        if not isinstance(position, int):
            raise TypeError("current position must be an integer value")

        self._current_position = position

    @property
    def previous_position(self):
        return self._previous_position

    @property
    def new_position(self):
        return self._new_position

    @new_position.setter
    def new_position(self, position):
        if not isinstance(position, int):
            raise TypeError("new position must be an int value")

        self._new_position = position

    @property
    def owned_by(self):
        return self._owned_by

    @property
    def current_state_served(self):
        return self._current_state_served

    @property
    def new_state_served(self):   
        return self._new_state_served

    @new_state_served.setter
    def new_state_served(self, serve_state):   
        if not isinstance(serve_state, bool):
            raise TypeError("New served state must be a bool")
        self._new_state_served = serve_state