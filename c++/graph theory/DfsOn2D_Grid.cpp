#include<bits/stdc++.h>
using namespace std;
int n, m;
int vis[1001][1001];
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

bool isvalid(int x, int y)
{
	if (x < 1 || x > n || y < 1 || y > m)return false;

	if (vis[x][y] == 1)return false;

	return true;
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

void dfs(int x, int y)
{
	vis[x][y] = 1;
	cout << x << " " << y << endl;

	for (int i = 0; i < 4; i++)
	{
		if (isvalid(x + dx[i], y + dy[i]))dfs(x + dx[i], y + dy[i]);
	}

	// if (isvalid(x , y + 1))dfs(x, y + 1);
	// if (isvalid(x + 1, y ))dfs(x + 1, y );
	// if (isvalid(x, y - 1))dfs(x, y - 1);
	// if (isvalid(x - 1, y))dfs(x - 1, y);


}

int main()
{
	read();
	cin >> n >> m;
	dfs(1, 1);

}
