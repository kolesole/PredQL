class TimeManager:
    def __init__(self, cur_time):
        self.start_time = cur_time
    
    def create_time_intervals(self, start, end, time_lim):
        diff = end - start
        intervals = []    
        while end <= time_lim:
            intervals.append(())

