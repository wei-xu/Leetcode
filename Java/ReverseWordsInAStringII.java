package solution;

public class ReverseWordsInAStringII {
	public static void reverseWords(char[] s){
		reverse(s, 0, s.length - 1);
		int start=0;
		for(int i = 0; i < s.length + 1; i++){
			if(i >= s.length || s[i] == ' '){
				reverse(s, start, i - 1);
				start = i + 1;
			}
		}
	}
	public static void reverse(char[] s, int start, int end){
		while(start < end){
			char tmp = s[start];
			s[start] = s[end];
			s[end] = tmp;
			start++;
			end--;
		}
	}
	
	public static void main(String[] args){
		char[] strings = "sky is blue".toCharArray();
		System.out.println(strings);
		reverseWords(strings);
		System.out.println(strings);
	}
}
