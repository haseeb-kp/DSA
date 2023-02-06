def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
    
def reverse_linked_list_recursive(head, prev=None):
    if not head:
        return prev
    next_node = head.next
    head.next = prev
    return reverse_linked_list_recursive(next_node, head)