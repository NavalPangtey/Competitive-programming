#include<bits/stdc++.h>
using namespace std;

vector <int> v[100000];
int visited[100001], in[100001], low[100001], timer;
set <int> s;
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
			if (low[child] >= in[node] && p != -1)
				s.insert(node);
			subtree++;

		}
	}
	if (p == -1 && subtree > 1)
	{
		s.insert(node);
	}
}

void solve(int n, int m)
{
	int a, b;
	for (int i = 0; i <= n; i++)
	{
		visited[i] =  0;
		v[i].clear();
	}
	timer = 1;
	s.clear();
	for (int i = 0; i < m; i++)cin >> a >> b, v[a].push_back(b), v[b].push_back(a);

	for (int i = 1; i <= n; i++)
		if (visited[i] == 0)
			dfs(i, -1);

	cout << s.size() << "\n";
}

int main()
{
	read();
	int n, m;
	while (1) {
		cin >> n >> m;
		if (n == 0 && m == 0)break;
		else solve(n , m);
	}
}
