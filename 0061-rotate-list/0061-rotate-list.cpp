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
        vector<int> v;
        ListNode* before = head;
        while (before != nullptr) {
            v.push_back(before -> val);
            before = before -> next;
        }
        
        if (head == nullptr) return nullptr;
        
        int k1 = k % v.size();
        
        rotate(v.begin(), v.end() - k1, v.end());
        
        for (int i: v) {
            std::cout << i << std::endl;
        }
        
        ListNode* headNode = new ListNode(v[0]);
        ListNode* beforeNode = headNode;
        for (int i = 1; i < v.size(); i++) {
            ListNode* newNode = new ListNode(v[i]);
            beforeNode -> next = newNode;
            beforeNode = newNode;
        }
        
        return headNode;
    }
};