class MyHashMap:

    def __init__(self):
        self.x=defaultdict(int)

    def put(self, key: int, value: int) -> None:
        self.x[key]=value

    def get(self, key: int) -> int:
        return -1 if key not in self.x else self.x[key]

    def remove(self, key: int) -> None:
        x=self.x.pop(key,None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)