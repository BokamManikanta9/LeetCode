class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True)
        sorted_names = [name for _, name in people]
        return sorted_names