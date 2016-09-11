package solution;

import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	public static boolean isAnagram(String s, String t){
//		Map<Character, Integer> map = new HashMap<Character, Integer>();
		int[] index = new int[26];
		for(int i = 0; i < s.length(); i++) index[s.charAt(i) - 'a']++;
		for(int i = 0; i < t.length(); i++) index[s.charAt(i) - 'a']--;
		for(int i : index) if(i != 0) return false;
		return true;
	}
}
