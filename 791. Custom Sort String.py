class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = list(s)
        self.order_dict = dict()
        order = list(order)
        order.reverse()
        for i in range(len(order)):
            self.order_dict[order[i]] = (i + 1) * 100

        return ''.join(sorted((char for char in s), key=self.sort_with_order, reverse=True))

    def sort_with_order(self, char):
        if char in self.order_dict:
            return ord(char) + self.order_dict[char]
        return ord(char)

print(Solution().customSortString(order = "cba", s = "abcdsjkdjlgljgcjsdjlgjdrmcgdjghjdfhgjkhdgjfjdkslhbjksfndjbndsfbnkjfdnbjskdfnbndfjbnjkfnbjksndgjbknsjdknbjkgnsjbkndfjvnjcvhdjkvsnjvhejrlvjerkvjrtelnvjtnvjr" ))