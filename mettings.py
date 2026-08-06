intervals=[[0,30],[5,10],[15,20]]

start=sorted([interval[0] for interval in intervals])
end=sorted([interval[1] for interval in intervals])

def minMeeting (start, end):
    s=0
    e=0
    meeting=0
    max_Meeting=0
    while s<len(end):
        if start[s]<end[e]:
            meeting+=1
            s+=1
            if meeting>max_Meeting:
                max_Meeting=meeting

        else:
            meeting-=1
            e+=1
    return max_Meeting

print(minMeeting(start,end))