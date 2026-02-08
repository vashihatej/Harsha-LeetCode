class MyCalendar:

    def __init__(self):
        # List to store booked events
        # Each event is stored as a tuple: (startTime, endTime)
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Check the new event against all existing events
        for s, e in self.events:
            # Two events DO NOT overlap if:
            # 1) Existing event ends before the new event starts
            #        e <= startTime
            # OR
            # 2) Existing event starts after the new event ends
            #        s >= endTime
            #
            # If neither of these is true, then the events overlap
            if not (e <= startTime or s >= endTime):
                # Overlap detected → cannot book this event
                return False

        # If no overlaps were found, add the event
        self.events.append((startTime, endTime))
        return True
