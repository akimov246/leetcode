class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:

        def get_bitmask(players: list[int]):
            pow = len(players) // 2
            for i in range(2 ** pow):
                mask = ''
                for char in bin(i)[2:].rjust(pow, '0'):
                    if char == '0':
                        mask += '01'
                    else:
                        mask += '10'

                yield mask

        earliest = float('inf')
        latest = 0

        def helper(round=1, players=None):
            nonlocal earliest
            nonlocal latest
            if players is None:
                players = list(range(1, n + 1))

            winners = [firstPlayer, secondPlayer]
            other = []

            if len(players) % 2:
                p = players.pop(len(players) // 2)
                if p not in winners:
                    winners.append(p)

            winners.sort()

            p1 = 0
            p2 = -1
            while players[p1] < players[p2]:
                if players[p1] not in winners and players[p2] not in winners:
                    other.append(players[p1])
                    other.append(players[p2])
                elif players[p1] in winners and players[p2] in winners:
                    earliest = min(earliest, round)
                    latest = max(latest, round)
                    return
                p1 += 1
                p2 = -(p1 + 1)

            if not other and len(winners) == 2:
                earliest = min(earliest, round + 1)
                latest = max(latest, round + 1)
                return

            if not other and len(winners) == 3:
                if winners[0] in [firstPlayer, secondPlayer] and winners[-1] in [firstPlayer, secondPlayer]:
                    earliest = min(earliest, round + 1)
                    latest = max(latest, round + 1)
                    return
                else:
                    earliest = min(earliest, round + 2)
                    latest = max(latest, round + 2)
                    return

            for bitmask in get_bitmask(other):
                players_to_next_round = []
                for i in range(len(bitmask)):
                    if bitmask[i] == '1':
                        players_to_next_round.append(other[i])
                players_to_next_round.extend(winners)
                helper(round + 1, sorted(players_to_next_round))

        helper()

        return [earliest, latest]

print(Solution().earliestAndLatest(n = 5, firstPlayer = 1, secondPlayer = 4))