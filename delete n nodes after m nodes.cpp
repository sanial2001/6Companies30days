class Solution
{
    public:
    void linkdelete(struct Node  *head, int M, int N)
    {
        while(head) {
            int tempM = M;
            while(head && --tempM) head = head -> next;
            int tempN = N;
            Node *prevNode = head;
            while(head && tempN--) head = head -> next;
            if(prevNode) {
                head = head ? head -> next : NULL;
                prevNode -> next = head;
            }
        }
    }
};
