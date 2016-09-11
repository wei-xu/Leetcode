package solution;

public class MergeTwoSortedLists {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	public ListNode mergeTwoLists(ListNode l1, ListNode l2){
		if (l1 == null) return l2;
		if (l2 == null) return l1;
		ListNode head = null;
		if (l1.val > l2.val){
			head = l2;
			head.next = mergeTwoLists(l1, l2.next);
		}
		else{
			head = l1;
			head.next = mergeTwoLists(l1.next, l2);
		}
		return head;
	}

}
