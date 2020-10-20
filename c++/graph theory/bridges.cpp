#include<bits/stdc++.h>
using namespace std;

vector <int> v[1000];
int visited[1001], in[1001], low[1001];
int timer;
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
	in[node] = low[node] = timer;
	timer++;
	for (int child : v[node])
	{
		if (child == p) continue;
		if (visited[child] == 1)
		{
			low[node] = min(low[node], in[child]);
		}
		else
		{
			dfs(child, node);
			if (low[child] > in[node])
				cout << node << "-->" << child << "\n";

			low[node] = min(low[node], low[child]);
		}
	}
}

int main() {
	read();
	int n, m, a, b;
	cin >> n >> m;
	// for (int i = 0; i <= n; i++)visited[i] = 0;
	for (int i = 0; i < m; i++)
	{
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	timer = 0;
	dfs(1, -1);
}
