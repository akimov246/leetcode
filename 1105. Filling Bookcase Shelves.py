from dataclasses import dataclass

@dataclass
class Level:
    height: int
    width: int

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:


        def fill_one_shelve(books):
            selects = []
            selects_idxs = []
            left = 0
            right = 1

            # for book in books:
            #     selects.append(book)

            while right <= len(books):
                current = books[left:right]
                dbg = sum(book[0] for book in current)
                if sum(book[0] for book in current) <= shelfWidth:
                    selects.append(current)
                    selects_idxs.append((left, right))
                    right += 1
                else:
                    left += 1

            #print(selects)
            #print(selects_idxs)

            def my_max(value):
                # t = sum(v[0] for v in value)
                # h = sum(v[1] for v in value)
                # return sum(v[0] for v in value) + sum(v[1] for v in value)
                #return max(v[1] for v in value)
                h = sum(v[1] for v in value)
                t = sum(v[0] for v in value)
                l = len(value)
                return h, t, -l

            idx = selects.index(max(selects, key=my_max))
            #idx = selects.index(max(selects, key=lambda value: (max(v[1] for v in value), -(sum(v[0] for v in value)), len(value))))
            left, right = selects_idxs[idx]
            #new_books = [books[:left], books[right:]]
            new_books = []
            if books[:left]:
                new_books.append(books[:left])
            if books[right:]:
                new_books.append(books[right:])

            #print(max(selects, key=my_max))
            return max(selects, key=my_max), new_books

        books = [books]
        print(books)
        shelve = []
        while books:
            dbg = len(books)
            level, new_books = fill_one_shelve(books.pop(0))
            shelve.append(level)
            if new_books:
                books.extend(new_books)

        print(shelve)
        total_height = 0
        for level in shelve:
            total_height += max(level, key=lambda value: value[1])[1]
        print(total_height)
        return total_height

print(Solution().minHeightShelves(books = [[11,83],[170,4],[93,80],[155,163],[134,118],[75,14],[122,192],[123,154],[187,29],[160,64],[170,152],[113,179],[60,102],[28,187],[59,95],[187,97],[49,193],[67,126],[75,45],[130,160],[4,102],[116,171],[43,170],[96,188],[54,15],[167,183],[58,158],[59,55],[148,183],[89,95],[90,113],[51,49],[91,28],[172,103],[173,3],[131,78],[11,199],[77,200],[58,65],[77,30],[157,58],[18,194],[101,148],[22,197],[76,181],[21,176],[50,45],[80,174],[116,198],[138,9],[58,125],[163,102],[133,175],[21,39],[141,156],[34,185],[14,113],[11,34],[35,184],[16,132],[78,147],[85,170],[32,149],[46,94],[196,3],[155,90],[9,114],[117,119],[17,157],[94,178],[53,55],[103,142],[70,121],[9,141],[16,170],[92,137],[157,30],[94,82],[144,149],[128,160],[8,147],[153,198],[12,22],[140,68],[64,172],[86,63],[66,158],[23,15],[120,99],[27,165],[79,174],[46,19],[60,98],[160,172],[128,184],[63,172],[135,54],[40,4],[102,171],[29,125],[81,9],[111,197],[16,90],[22,150],[168,126],[187,61],[47,190],[54,110],[106,102],[55,47],[117,134],[33,107],[2,10],[18,62],[109,188],[113,37],[59,159],[120,175],[17,147],[112,195],[177,53],[148,173],[29,105],[196,32],[123,51],[29,19],[161,178],[148,2],[70,124],[126,9],[105,87],[41,121],[147,10],[78,167],[91,197],[22,98],[73,33],[148,194],[166,64],[33,138],[139,158],[160,19],[140,27],[103,109],[88,16],[99,181],[2,140],[50,188],[200,77],[73,84],[159,130],[115,199],[152,79],[1,172],[124,136],[117,138],[158,86],[193,150],[56,57],[150,133],[52,186],[21,145],[127,97],[108,110],[174,44],[199,169],[139,200],[66,48],[52,190],[27,86],[142,191],[191,79],[126,114],[125,100],[176,95],[104,79],[146,189],[144,78],[52,106],[74,74],[163,128],[34,181],[20,178],[15,107],[105,8],[66,142],[39,126],[95,59],[164,69],[138,18],[110,145],[128,200],[149,150],[149,93],[145,140],[90,170],[81,127],[57,151],[167,127],[95,89]], shelfWidth = 200))