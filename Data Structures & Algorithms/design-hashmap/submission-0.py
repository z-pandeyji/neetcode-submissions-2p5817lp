class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def hash(self,key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        bucket = self.buckets[index]
        for i in bucket:
            if i[0] == key:
                i[1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        index = self.hash(key)
        bucket = self.buckets[index]
        for i in bucket:
            if i[0] == key:
                return i[1]
        return -1

        
    def remove(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)