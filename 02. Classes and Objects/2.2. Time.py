class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        self.hours = self.hours if self.hours > 9 else f'0{self.hours}'
        if __name__ == '__main__':
            self.minutes = self.minutes if self.minutes > 9 else f'0{self.minutes}'
        self.seconds = self.seconds if self.seconds > 9 else f'0{self.seconds}'
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def next_second(self):
        self.seconds = self.seconds + 1 if self.seconds < Time.max_seconds else 0
        if self.seconds == 0:
            self.minutes = self.minutes + 1 if self.minutes < Time.max_minutes else 0
            if self.minutes == 0:
                self.hours = self.hours + 1 if self.hours < Time.max_hours else 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())

time = Time(0, 0, 0)
print(time.next_second())

t = Time(16, 35, 54)
print(t.next_second())
t = Time(1, 2, 3)
t.set_time(3, 2, 1)
print(t.next_second())
t = Time(1, 20, 30)
print(t.next_second())