package solution;

public class WordSearch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[][] b = {
				{'C', 'A', 'A'},
				{'A', 'A', 'A'},
				{'B', 'C', 'D'}
		};
		System.out.println(exist(b, "AAB"));
	}
	
	public static boolean exist(char[][] board, String word){
		boolean[][] visited = new boolean[board.length][board[0].length];
		for (int y = 0; y < board.length; y++){
			for (int x = 0; x < board[0].length; x++){
				if(match(board, y, x, word, 0, visited)) return true;
			}
		}
		return false;
	}
	
	public static boolean match(char[][] board, int j, int i, String word, int index, boolean[][] visited){
		if(index == word.length()){
			return true;
		}
		if(i < 0 || j < 0 || i >= board[0].length || j >= board.length){
			return false;
		}
		if(word.charAt(index) != board[j][i]) return false;
		if(visited[j][i] == true) return false;
		visited[j][i] = true;
		boolean exist = match(board, j + 1, i, word, index + 1, visited) || 
				match(board, j, i + 1, word, index + 1, visited) || 
				match(board, j - 1, i, word, index + 1, visited) || 
				match(board, j, i - 1, word, index + 1, visited);
		visited[j][i] = false;
		return exist;
	}
}
