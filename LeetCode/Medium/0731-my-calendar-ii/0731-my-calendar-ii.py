class MyCalendarTwo:

    def __init__(self):
        self.event=[]
        self.overlaps=[]
        

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.overlaps:
            if max(s,startTime)<min(e,endTime):
                return False
        for s,e in self.event:
            if max(s,startTime)<min(e,endTime):
                maxstart=max(s,startTime)
                minend=min(e,endTime)
                self.overlaps.append((maxstart,minend))
        self.event.append((startTime,endTime))
        return True

#-------------------------------_#
class MyCalendarTwo:

    def __init__(self):
        """
        bookings  -> stores all events that were successfully booked
        overlaps  -> stores intervals where two events already overlap
        """
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        """
        Try to add a new event [start, end).

        If adding this event creates a triple booking,
        return False.

        Otherwise add the event and return True.
        """

        # STEP 1: Check if new event overlaps with any existing
        # double-booked interval.
        # If yes → triple booking would happen.
        for s, e in self.overlaps:
            if max(start, s) < min(end, e):
                return False

        # STEP 2: Find intersections with existing bookings.
        # These intersections become new double-booked intervals.
        for s, e in self.bookings:

            # check overlap
            if max(start, s) < min(end, e):

                # store the overlapping region
                overlap_start = max(start, s)
                overlap_end = min(end, e)

                self.overlaps.append((overlap_start, overlap_end))

        # STEP 3: Add this booking
        self.bookings.append((start, end))

        return True