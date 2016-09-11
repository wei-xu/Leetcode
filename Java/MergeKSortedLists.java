package solution;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MergeKSortedLists {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ListNode[] lists = new ListNode[3];
		lists[0] = new ListNode(3);
		lists[1] = new ListNode(1);
		lists[2] = new ListNode(10);
		ListNode res = mergeKLists(lists);

	}
	public static ListNode mergeKLists(ListNode[] lists){
		PriorityQueue<ListNode> q = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
			@Override
			public int compare(ListNode n1, ListNode n2){
				if(n1.val > n2.val) return 1;
				else if(n1.val < n2.val) return -1;
				else return 0;
			}
		});
		
		for(ListNode node : lists){
			if(node != null) q.add(node);
		}
		ListNode result = new ListNode(0);
		ListNode p = result;
		
		while(!q.isEmpty()){
			p.next = q.poll();
			p = p.next;
			if(p.next != null) q.add(p.next);
		}
		return result.next;
	}
}
