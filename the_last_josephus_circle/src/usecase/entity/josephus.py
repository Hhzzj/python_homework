class JosephusCircle():
    def __init__(self, people_list, interval, start_pos):
        assert type(people_list)==list  and type(interval)==int and type(start_pos)==int
        assert interval > 0
        self.people_list = people_list
        self.interval = interval
        self.start_pos = start_pos
    
    def __iter__(self):
        return self 

    def __next__(self):
        if len(self.people_list)>0:
            out_pos = (self.start_pos+self.interval-1) % len(self.people_list)
            self.out_person = self.people_list.pop(out_pos)
            self.start_pos = out_pos
            return self.out_person
        else:
            raise StopIteration

            