# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    answer = 0
    monthDict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    for elem in S.split('\n'):
        size, _, month, year, _ = elem.strip().split(' ')
        size, year = int(size), int(year)
        if size >= 245760:
            if year > 1990:
                answer += 1
            elif year == 1990:
                if monthDict[month] >= 2:
                    answer += 1
    
    return "NO FILES" if answer == 0 else str(answer)


# size date name
S = "779091968 23 Sep 2009 system.zip\n284164096 14 Aug 2013 to-do-list.xml\n714080256 19 Jun 2013 blockbuster.mpeg\n329 12 Dec 2010 notes.html\n444596224 17 Jan 1950 delete-this.zip\n641 24 May 1987 setup.png\n245760 16 Jul 2005 archive.zip\n839909376 31 Jan 1990 library.dll"
solution(S)

'''
245760 이상의 크기
31 Jan 1990 이후에 수정
'''
