package solution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupAnagrams {
	public static void main(){
		
	}
	public List<List<String>> groupAnagrams(String[] strs){
		Map<String, List<String>> map = new HashMap<String, List<String>>();
		Arrays.sort(strs);
		for(String s : strs){
			char[] ch = s.toCharArray();
			Arrays.sort(ch);
			String key = String.valueOf(ch);
			if(!map.containsKey(key)) map.put(key, new ArrayList<String>());
			map.get(key).add(s);
		}
		return new ArrayList<List<String>>(map.values());
	}
}
