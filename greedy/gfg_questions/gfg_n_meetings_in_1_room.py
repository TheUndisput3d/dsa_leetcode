## T.C: O(nlogn) + O(n) ~ O(n)
## S.C: O(n)
class Solution:
    def maximumMeetings(self,start,end):
        n = len(start)
        
        class Meeting:
            def __init__(self, start, end, pos):
                self.start = start
                self.end = end
                self.pos = pos
                
        meetings = [Meeting(start[i], end[i], i+1) for i in range(n)]
        
        meetings.sort(key=lambda x: (x.end, x.start))
        
        count = 1
        res = [1]
        lastTime = meetings[0].end
        
        for i in range(1, n):
            meeting = meetings[i]
            if meeting.start > lastTime:
                count += 1
                res.append(meeting.pos)
                lastTime = meeting.end
        
        return count
    
## T.C: O(n)
## S.C: O(n)
class Solution:
    def maximumMeetings(self,start,end):
        n = len(start)
        
        class Meeting:
            def __init__(self, start, end, pos):
                self.start = start
                self.end = end
                self.pos = pos
                
        meetings = [Meeting(start[i], end[i], i+1) for i in range(n)]
        
        meetings.sort(key=lambda x: (x.end, x.start))
        
        count = 1
        res = [1]
        lastTime = meetings[0].end
        
        for i in range(1, n):
            meeting = meetings[i]
            if meeting.start > lastTime:
                count += 1
                res.append(meeting.pos)
                lastTime = meeting.end
        
        return count