package solution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Subsets {
    public List<List<Integer>> subsets(int[] nums) {
    	List<List<Integer>> result = new ArrayList<List<Integer>>();
    	Arrays.sort(nums);
    	dfs(new ArrayList<Integer>(), 0, nums, result);
        return result;
    }
    public void dfs(List<Integer> path, int index, int[] nums, List<List<Integer>> result){
    	result.add(new ArrayList<Integer>(path));//should be new List
    	for (int i = index; i < nums.length; i++){
    		path.add(nums[i]);
    		dfs(path, i + 1, nums, result);
    		path.remove(path.size() - 1);
    	}
    }
}
