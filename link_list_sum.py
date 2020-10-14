class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def to_array(self):
        _arr = []
        cursor = self
        while(cursor.next):
            _arr.append(cursor.val)
            cursor = cursor.next
        _arr.append(cursor.val)      
        return _arr     
            
    def __str__(self):
        return " ".join(str(i) for i in self.to_array())
        
        
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def helper(val1, val2, remind):
        return (val1 + val2 + remind)%10, int((val1 + val2 + remind)/10)
    
    def append(root, data):
        if root.next:
            append(root.next, data)
        else:
            root.next = ListNode(data)
    
    _val, remind = helper(l1.val, l2.val, 0)
    result = ListNode(val=_val)

    while (l1.next is not None or l2.next is not None):
        l1 = l1.next if l1.next is not None else ListNode()
        l2 = l2.next if l2.next is not None else ListNode()
        _val, remind = helper(l1.val, l2.val, remind)
        append(result, _val)
        
    if remind != 0:
        append(result, remind)
            
    return result

if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(7, ListNode(1))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = addTwoNumbers(l1, l2)
    print(result)
        