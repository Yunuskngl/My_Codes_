//SOLUTION:

//https://leetcode.com/problems/middle-of-the-linked-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        if(head==nullptr || head->next==nullptr) {
            return head;
        }
        int count=0;
        ListNode *temp=head;
        while(temp!=nullptr) {
            count++;
            temp=temp->next;
        }
        int mid=count/2;
        ListNode *h=head;
        for(int i=0; i<mid; i++) {
            h=h->next;
        }

        return h;
    }
}; */