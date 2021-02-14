from bisect import insort, bisect_left


class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        start_modifier, end_modifier = (start, 1), (end, -1)
        insert_start = bisect_left(self.calendar, start_modifier)
        self.calendar.insert(insert_start, start_modifier)
        insert_end = bisect_left(self.calendar, end_modifier)
        self.calendar.insert(insert_end, end_modifier)

        bookings = 0
        for _, modifier in self.calendar:
            bookings += modifier
            if bookings > 2:
                self.calendar.pop(insert_end)
                self.calendar.pop(insert_start)
                return False

        return True


calendar = MyCalendar()
for a1, a2 in [
    [10, 20],
    [50, 60],
    [10, 40],
    [5, 15],
    [5, 10],
    [25, 55],
]:
    print(calendar.book(a1, a2))
