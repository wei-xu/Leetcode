package solution;

import java.util.ArrayList;
import java.util.List;

public class Tester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Subsets s = new Subsets();
//		int[] nums = {1,2,3};
//		List<List<Integer>> result = new ArrayList<List<Integer>>();
//		result = s.subsets(nums);
//		System.out.println(result.toString());
		
		rotate();
	}
	public static void rotate(){
		RotateImage rotateImage = new RotateImage();
		int[][] m = {
				{1, 2, 3, 4},
				{5, 6, 7, 8},
				{9, 10, 11, 12},
				{13, 14, 15, 16},
		};
		int[][] n = {
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
		};
		rotateImage.rotate(n);
//		System.out.println(n);
	}
	
	public static void reverseWords(){
		ReverseWordsInAStringII r = new ReverseWordsInAStringII();
	}
}
