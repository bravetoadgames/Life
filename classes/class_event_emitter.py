# -*- coding: utf-8 -*-

class EventEmitter:
    


    def __init__(self):
        self._listeners = {}



    # ------------------------------------------------------------------
    # Add an eventtype to the listener
    # ------------------------------------------------------------------
    def subscribe(self, event_type, callback):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)



    # ------------------------------------------------------------------
    # Respond on an event
    # ------------------------------------------------------------------
    def emit(self, event_type, data=None):
        if event_type in self._listeners:
            for callback in self._listeners[event_type]:
                callback(data)
                