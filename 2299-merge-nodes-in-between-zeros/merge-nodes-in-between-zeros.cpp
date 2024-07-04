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
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        vector<int>l;
        vector<int>m;
        ListNode* b=new ListNode(0);
        ListNode* c=b;
        while(head!=NULL){
            l.push_back(head->val);
            head=head->next;
        }
        // for(int i=0;i<l.size();i++){
        //     cout<<l[i]<<" ";
        // }
        int s=0;
        for(int i=0;i<l.size();i++){
            if(l[i]==0){
                m.push_back(s);
                s=0;
            }
            s+=l[i];
        }
        for(int i=1;i<m.size();i++){
            ListNode* x=new ListNode(m[i]);
            b->next=x;
            b=b->next;
        }
        return c->next;
    }
};