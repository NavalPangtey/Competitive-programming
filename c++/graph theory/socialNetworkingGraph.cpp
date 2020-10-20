#include<bits/stdc++.h>
using namespace std;

vector <int> v[1000001];
int visited[1000001], dist[1000001], lvl[1000001];

void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

void solve(int m)
{
	visited[m] = 1;
	dist[m] = 0;
	queue<int> q;
	q.push(m);
	while (!q.empty())
	{
		int curr = q.front();
		q.pop();
		for (int child : v[curr])
		{
			if (visited[child] == 0)
			{
				q.push(child);
				visited[child] = 1;
				dist[child] = dist[curr] + 1;
				lvl[dist[child]]++;
			}
		}
	}


}

int main()
{
	read();
	int n, e;
	cin >> n >> e;
	int u, r;
	for (int i = 0; i < e; i++)
	{
		cin >> u >> r;
		v[u].push_back(r);
		v[r].push_back(u);
	}
	int q, m, t;
	cin >> q;
	while (q--)
	{
		cin >> m >> t;
		for (int i = 0; i <= n ; i++)
		{	visited[i] = 0;
			dist[i] = 0;
			lvl[i] = 0;
		}
		solve(m);
		cout << lvl[t] << "\n";

	}

}
