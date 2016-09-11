package solution;

public class MaximumSubarray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public int maxSubArray(int[] nums){
		int max = 0;
		for(int num : nums){
			max = Math.max(num, max);
		}
		if (max <= 0) return max;
		else max = 0;
		
		int sum = 0;
		for(int num : nums){
			sum += num;
			if(sum <= 0) sum = 0;
			else if(sum > max) max = sum;
		}
		return max;
	}
}
