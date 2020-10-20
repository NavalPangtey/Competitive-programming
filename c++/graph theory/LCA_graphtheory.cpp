#include<bits/stdc++.h>
using namespace std;

void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

vector <int> v[10001];
int lvl[10001] , visited[10001], par[10001];

void dfs(int node, int d)
{
	visited[node] = 1;
	lvl[node] = d;

	for (int child : v[node])
	{
		if (visited[child] == 0)
		{
			par[child] = node;
			dfs(child, d + 1);
		}
	}
}

int lca(int a, int b)
{
	if (lvl[a] < lvl[b]) {
		swap(a, b);
	}
	int level = lvl[a] - lvl[b];

	while (level > 0)
	{
		a = par[a];
		level--;
	}

	if (a == b)return b;

	while (par[a] != par[b])
	{
		a = par[a];
		b = par[b];
	}
	return par[a];

}


int main()
{
	read();
	int n, m, u, e;
	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> u >> e;
		v[u].push_back(e);
		v[e].push_back(u);
	}

	dfs(1, 0);

	// for (int i = 1; i <= n; i++)
	// 	cout << lvl[i];

	int a , b;
	cin >> a >> b;
	cout << lca(a, b);

}
