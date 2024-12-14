#include <iostream>
#include <vector>
#include <fstream>
#include <utility>
using namespace std;

vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

bool is_valid(int x, int y, int r, int c) {
	return (0 <= x && x < r) && (0 <= y && y < c);
}

int solve(vector<vector<int>> &grid, int x, int y, vector<vector<bool>> &visited) {
	int r = grid.size(), c = grid[0].size();
	int total = 0;

	visited[x][y] = true;
	if(grid[x][y] == 9) {
		total++;
	}

	for(auto [dx, dy]: directions) {
		if(is_valid(x + dx, y + dy, r, c) && !visited[x + dx][y + dy]) {
			int dist = grid[x + dx][y + dy] - grid[x][y];
			if(dist == 1) {
				total += solve(grid, x + dx, y + dy, visited);
			}
		}
	}

	return total;
}

int main(int argc, char** argv) {
	ifstream file(argv[1]);
	vector<vector<int>> grid;
	string s;

	while(file >> s) {
		vector<int> row;
		for(char c: s) {
			row.push_back(c - '0');
		}
		grid.push_back(row);
	}

	int r = grid.size(), c = grid[0].size();
	vector<pair<int, int>> trail_start;
	for(int i = 0; i < r; i++) {
		for(int j = 0; j < c; j++) {
			if(grid[i][j] == 0) trail_start.push_back({i, j});
		}
	}

	int answer = 0;
	for(int i = 0; i < trail_start.size(); i++) {
		auto [x, y] = trail_start[i];
		vector<vector<bool>> visited(r, vector<bool>(c, false));
		answer += solve(grid, x, y, visited);
	}
	cout << answer << endl;

	return 0;
}
