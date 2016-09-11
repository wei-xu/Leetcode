package solution;

public class SwapNodesInPairs {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public ListNode swapPairs(ListNode head){
        if (head.next == null) return firstNode;
        ListNode newHead = head.next;
        
        // p->q->
        ListNode p = head;
        ListNode q = head.next;
        while(true){
            nextP = p.next.next;
            // re-link p ang q;
            p.next = q.next;
            q.next = p;
            
            if(nextP == null) break;
            if(nextP.next == null) break;
            
            p = nextP;
            q = nextP.next;
        }
        return newHead;
	}
}
