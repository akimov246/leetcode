class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        muted_friends = set()
        for friendship in friendships:
            a = friendship[0] - 1
            b = friendship[1] - 1
            if not set(languages[a]).intersection(set(languages[b])):
                muted_friends.add(a)
                muted_friends.add(b)

        languages_counter = {}
        for friend in muted_friends:
            for language in languages[friend]:
                languages_counter[language] = languages_counter.get(language, 0) + 1

        return len(muted_friends) - max(languages_counter.values(), default=0)

#print(Solution().minimumTeachings(n = 11, languages = [[3,11,5,10,1,4,9,7,2,8,6],[5,10,6,4,8,7],[6,11,7,9],[11,10,4],[6,2,8,4,3],[9,2,8,4,6,1,5,7,3,10],[7,5,11,1,3,4],[3,4,11,10,6,2,1,7,5,8,9],[8,6,10,2,3,1,11,5],[5,11,6,4,2]], friendships = [[7,9],[3,7],[3,4],[2,9],[1,8],[5,9],[8,9],[6,9],[3,5],[4,5],[4,9],[3,6],[1,7],[1,3],[2,8],[2,6],[5,7],[4,6],[5,8],[5,6],[2,7],[4,8],[3,8],[6,8],[2,5],[1,4],[1,9],[1,6],[6,7]]))
#print(Solution().minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]))