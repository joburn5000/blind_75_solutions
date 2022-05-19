"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104

Difficulty: Medium
Completed: 5/19/2022

"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [item for item in lists if item]        # gets rid of all the NoneType ListNodes
        if not lists: return None                       # if there are no non-empty lists, return None
        
        head = ListNode()                               # output
        tail = head                                     # tail node      
        
        while (lists):
            smallest_val, index = 10000, 0              # smallest value, index of node with smallest value
            for i in range(len(lists)):
                if lists[i].val < smallest_val:         # check for smallest value
                    smallest_val = lists[i].val         # update smallest value
                    index = i                           # update index for node with smallest value
            
            if not lists[index].next: lists.pop(index)  # if the next node is None, remove that node
            else: lists[index] = lists[index].next      # otherwise, progress to the next node in that list
            
            tail.val = smallest_val                     # update the tail with the smallest value we just found
            
            if lists:                                   # if not lists, we are done
                tail.next = ListNode()                  # otherwise, there are still more nodes to be added
                tail = tail.next                        # progress to the next node to be updated
                
        return head
"""
Explanation:

After removing all the empty lists, we find the smallest value and add it to our new list.

Time Complexity: O(KN) where N is the number of lists and K is the number of items in a list
Space Complexity O(N)

"""
