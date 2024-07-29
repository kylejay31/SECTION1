import heapq

class Listnode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next
        
        
def Merge_k_sorted_list(lists):
     # initializing a min- heap
    min_heap = []
    
    # Define a comparator for the heap to handle ListNode Objects
    Listnode.__it__ = lambda self, other: self.val < other.val

    # push the head node of each list into the heap       
    for i in lists:
        if i:
            heapq.heappush(min_heap, i)
            
        
    # Dummy node to help with the merge process
    dummy = Listnode()
    current = dummy
    
    # Pop the smallest elememt from the heap and add it to the merged list
    while min_heap:
        smallest_node = heapq.heappop(min_heap)    
        current.next = smallest_node
        current =current.next
        if smallest_node:
            heapq.heappush(min_heap, smallest_node.next)
    
    # Return the head of the merged linked list
    return dummy.next         
            
# Helper function to convert a list of Lists to a list of ListNode objects
def build_linked_lists(lists):
    result = []
    for sublist in lists:
        dummy = Listnode()
        current = dummy
        for value in sublist:
            current.next = Listnode(val=value)
            current = current.next
        result.append(dummy.next)        
    return result        
        
# Helper function to convert a linked lists to apython list (for easy printing) 
def linked_list_to_lists(node):
    result = []           
    while node:
        result.append(node.val)
        node = node.next
    return result

# fuzz data
list1 = [[1, 3, 5], [2, 4 ,6], [7, 8, 9]]
list2 = [[1, 4, 5], [1, 3, 4], [2, 6]]     

# Convert thr input list to linked list

linked_lists1 = build_linked_lists(list1)
linked_lists2 = build_linked_lists(list2)    

# Merge list
Merge_list1 = Merge_k_sorted_list(linked_lists1)
Merge_list2 = Merge_k_sorted_list(linked_lists2)

# Covert the merged linked list back to python for easy read
print(linked_list_to_lists(Merge_list1))
print(linked_list_to_lists(Merge_list2))







    