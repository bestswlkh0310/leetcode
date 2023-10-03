/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <algorithm>

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) return nullptr;
        
        vector<ListNode*> v;
        ListNode* before = head;
        while (before != nullptr) {
            v.push_back(before);
            before = before -> next;
        }
        
        int k1 = k % v.size();
        
        if (k1 == 0 or v.size() == 1) return head;
        
        v.back() -> next = head;
        
        ListNode* headNode = v[v.size() - k1];
        
        v[v.size() - k1 - 1] -> next = nullptr;
        
        return headNode;
    }
};