class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
    
class FileSystem:
    def __init__(self):
        self.root = Node(0)

    def createPath(self, path: str, value: int) -> bool:
        if len(path) <= 1:
            return False
        dir_names = path.split("/")
        iterator = self.root
        for dir_name in dir_names[1:-1]:
            if dir_name not in iterator.children:
                return False
            iterator = iterator.children[dir_name]
        
        if dir_names[-1] in iterator.children:
            return False
        iterator.children[dir_names[-1]] = Node(value)
        return True

    def get(self, path: str) -> int:
        if len(path) <= 1:
            return -1
        dir_names = path.split("/")
        iterator = self.root
        for dir_name in dir_names[1:]:
            if dir_name not in iterator.children:
                return -1
            iterator = iterator.children[dir_name]
        return iterator.val
            


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)