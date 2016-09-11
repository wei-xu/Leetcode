package solution;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Sum3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {-1, 0, 1, 2, 2, -1, -4};
		List<List<Integer>> output = threeSum(nums);
		System.out.println(output.toString());
	}
	
	public static List<List<Integer>> threeSum(int[] nums){
		List<List<Integer>> res = new ArrayList<List<Integer>>();
		Arrays.sort(nums);
		int start, end;
		for(int i = 0; i < nums.length; i++){
			start = i + 1;
			end = nums.length - 1;
			if(i > 0 && nums[i] == nums[i - 1]) continue;
			while(start < end){
				if(nums[start] + nums[end] < 0 - nums[i]) start++;
				else if(nums[start] + nums[end] > 0 - nums[i]) end--;
				else{
					res.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[start], nums[end])));
					while(start < end && nums[start] == nums[start + 1]) start++;
					while(start < end && nums[end] == nums[end - 1]) end--;
					start++;
					end--;
				}
			}
		}
		return res;
	}
}
