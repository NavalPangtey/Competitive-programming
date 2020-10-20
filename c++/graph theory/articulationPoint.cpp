#include<bits/stdc++.h>
using namespace std;

vector <int> v[100000];
int visited[100001], in[100001], low[100001], timer, articulationPoint;
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

void dfs(int node, int p)
{

	visited[node] = 1;
	in[node] = low[node] = timer++;
	int subtree = 0;
	for (int child : v[node])
	{
		if (p == child)continue;
		if (visited[child] == 1)low[node] = min(low[node], in[child]);
		else {
			dfs(child, node);
			low[node] = min(low[node], low[child]);
			if (low[child] >= in[node] && p != -1)articulationPoint++;
			subtree++;

		}
	}
	if (p == -1 && subtree > 1)
	{
		articulationPoint++;
	}
}

int main()
{
	read();
	int n, m, a, b;
	cin >> n >> m;
	for (int i = 0; i < m; i++)cin >> a >> b, v[a].push_back(b), v[b].push_back(a);
	timer = 0;
	articulationPoint = 0;
	dfs(2, -1);
	cout << articulationPoint;
}
