class TeleProg():
    nameOfProg = None
    h_start = None
    m_start = None
    h_end = None
    m_end = None
    def __init__(self, line):
        parts = line.split(" ")
        self.nameOfProg = parts[0]
        self.h_start = int((parts[1].split(':')[0]))
        self.m_start = int((parts[1].split(':')[1]))
        self.h_end = int((parts[2].split(':')[0]))
        self.m_end = int((parts[2].split(':')[1]))