package solution;

import java.util.Stack;

public class MinStack {
	private Stack<Integer> s = new Stack<Integer>();
	private Stack<Integer> minS = new Stack<Integer>();
	
    public void push(int x) {
        s.push(x);
        if(minS.size() == 0) minS.push(x);
        else minS.push(x < minS.peek() ? x : minS.peek());
    }

    public void pop() {
        minS.pop();
        s.pop();
    }

    public int top() {
        return s.peek();
    }

    public int getMin() {
    	return minS.peek();
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
