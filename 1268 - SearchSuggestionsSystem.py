#Problem 1268 of LeetCode
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:   
        search = []
        searching = ''
        for char in searchWord:
            searching += char
            search.append(sorted([product for product in products if product.startswith(searching)])[:3])

        return search
