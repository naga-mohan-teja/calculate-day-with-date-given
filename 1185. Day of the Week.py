class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        you={0:"Saturday",1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday"}
        if month==1:
            month=13
            year-=1
        if month==2:
            month=14
            year-=1
        q=day
        m=month
        K=year%100
        J=floor(year/100)
        h = (q + floor((13 * (m + 1)) / 5) + K + floor(K / 4) + floor(J / 4) - 2 * J) % 7 
        return you[h]
