package solution;

public class RotateImage {
	public void rotate(int[][] matrix){
		int end = matrix.length - 1;
		for(int layer = 0; layer < matrix.length/2; layer++){
			for(int i = layer; i < end - layer; i++){
				int tmp = matrix[layer][i];
				matrix[layer][i] = matrix[end- i][layer];
				matrix[end - i][layer] = matrix[end - layer][end - i];
				matrix[end - layer][end - i] = matrix[layer + i][end - layer];
				matrix[layer + i][end - layer] = tmp;
			}
		}
	}
}
