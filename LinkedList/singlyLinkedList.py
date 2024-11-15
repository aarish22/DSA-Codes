class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self,start=None):
        self.start = start
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n
    
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start=n
    
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next=n
    
    def show_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
        print()
        
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start is None
        else: 
            temp = self.start
            while temp.next.next is None:
                temp = temp.next
            temp.next=None
    
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp = self.start
            if temp.item == data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                    
    def __iter__(self):
        return LinkedListIterator(self.start)

class LinkedListIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data            



mylist = LinkedList()
mylist.insert_at_start(20)
mylist.insert_after(mylist.search(20),89)
## mylist.delete_item(20)
mylist.show_list()

for x in mylist:
    print(x,end=" ")
