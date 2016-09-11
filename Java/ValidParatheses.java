package solution;

import java.util.Stack;

public class ValidParatheses {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str1 = "()[]{}";
		String str2 = "()";
		String str3 = "(]";
		String str4 = "";
		System.out.println(isValid(str1));
		System.out.println(isValid(str2));
		System.out.println(isValid(str3));
		System.out.println(isValid(str4));
	}

	public static boolean isValid(String s){
		Stack<Character> stack = new Stack<Character>();
		for(int i = 0; i < s.length(); i++){
			char c = s.charAt(i);
			if(c == '[' || c == '{' || c == '('){
				stack.push(c);
			}
			else if(stack.empty()) return false;
			else if(c == ')'){
				if (!stack.pop().equals('(')) return false;
			}
			else if(c == '}'){
				if (!stack.pop().equals('{')) return false;
			}
			else if(c == ']'){
				if (!stack.pop().equals('[')) return false;
			}
		}
		return stack.empty();
	}
}
