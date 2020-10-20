#include<bits/stdc++.h>
using namespace std;

#define pb push_back

vector<int> v[10001];
int visited[10001], dis[10001];


void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

void bfs(int node)
{
	visited[node] = 1;
	dis[node] = 0;
	queue <int> q;
	q.push(node);
	while (!q.empty())
	{
		int curr = q.front();
		q.pop();
		for (int child : v[curr])
		{
			if (visited[child] == 0)
			{
				q.push(child);
				dis[child] = dis[curr] + 1;
				visited[child] = 1;
			}
		}
	}
}

void solve()
{

	int n , m, a, b;
	cin >> n >> m;
	for (int i = 0; i <= n; i++)
	{
		visited[i] = 0;
		v[i].clear();
	}
	for (int i = 0; i < m; i++)
	{
		cin >> a >> b, v[a].pb(b), v[b].pb(a);
	}
	bfs(1);
	cout << dis[n] << "\n";


}


int main()
{
	read();
	int t;
	cin >> t;
	while (t--)
	{
		solve();
	}
}
