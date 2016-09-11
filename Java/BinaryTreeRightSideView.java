package solution;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreeRightSideView {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	

	public class Solution {
	    public List<Integer> rightSideView(TreeNode root) {
	        ArrayList<Integer> views = new ArrayList<Integer>();
	        DFS(root, 1, views);
	        return views;
	    }
	    public void DFS(TreeNode root, int height, ArrayList<Integer> views){
	    	if(root == null) return;
	    	if(height > views.size()){
	    		views.add(root.val);
	    	}
	    	DFS(root.right, height + 1, views);
	    	DFS(root.left, height + 1, views);
	    }
	}
}
