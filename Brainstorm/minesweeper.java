public class MineSweeper {
	int width, height, mines;
	int[][] board;
	boolean[][] mines;
	boolean[][] flags;
	boolean firstClick;
	private void generateGame(int x, int y, int mines) {
		// Check for errors here
		for (int i = 0; i < mines; i++) {
			int tempX = random() * x;
			int tempY = random() * y;
			while (mines[tempX][tempY] != false) {
				tempX = random() * x;
				tempY = random() * y;
			}
			mines[x][y] = true;
		}
	}

	public boolean click(int x, int y) {
		if (this.firstClick) {
			this.firstClick = false;
			if (mines[x][y] == true) {
				int tempX = random() * this.width;
				int tempY = random() * this.height;
				while (mines[tempX][tempY] != false && x != ) {
					tempX = random() * this.width;
					tempY = random() * this.height;
				}
				mines[tempX][tempY] = true;
			}
		}
		if (mines[x][y] == true) {
			return false; // you lose
		}
		int minesAround = getMinesAround(x,y);
		if (minesAround > 0) {
			board[x][y] = minesAround;
			return true;
		}
		checkSurroundingSquares(x, y);
		for (int i = 0; i < width; i++) {
			for (int j = 0; j < height; j++) {
				if (board[i][j] == null && mines[i][j] != true) {
					return true;
				}
			}
		}
		// You win!
	}

	function flag(x,y) {
		flags[x][y] = !flags[x][y];
		if (flags == mines) {
			// you win!
		}
	}

	private int getMinesAround(x,y) {
		int minesAround = 0;
		for (int i = -1; i < 2; i++) {
			for (int j = -1; j < 2; j++) {
				if (x+i < 0 || y+j < 0 || x+i > this.width || y+j > this.height) {
					continue;
				}
				if (mines[x+i][y+j]) {
					minesAround++;
				}
			}
		}
		return minesAround;
	}

	private void checkSurroundingSquares(int x, int y) {
		// Error check here
		if (board[x][y] != null) {
			return;
		}
		int mineCount = 0;
		for (int i = -1; i < 2; i++) {
			for (int j = -1; j < 2; j++) {
				// also here
				mineCount = getMinesAround(x+i, y+j);
				if (mineCount == 0) {
					board[x+i][y+j] = 0;
					checkSurroundingSquares(x+i, y+j);
				} else {
					board[x+i][y+j] = mineCount;
				}
			}
		}
	}
}
