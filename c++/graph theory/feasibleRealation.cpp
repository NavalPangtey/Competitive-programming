#include<bits/stdc++.h>
using namespace std;

vector <int> v[1000001];
int visited[1000001], check[1000001];
int cc;
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

void dfs(int node)
{
	visited[node] = 1;
	check[node] = cc;
	for (int child : v[node])
		if (visited[child] == 0)
			dfs(child);
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	read();
	int t; cin >> t;
	while (t--)
	{
		int n , k, a, b;
		string op;
		cin >> n >> k;
		vector <pair<int, int>> p;
		p.clear();
		for (int i = 0; i <= n; i++)
		{
			visited[i] = 0;
			v[i].clear();

		}
		for (int i = 0 ; i < k; i++)
		{
			cin >> a >> op >> b;
			if (op == "=")
			{
				v[a].push_back(b);
				v[b].push_back(a);
			}
			else {
				p.push_back({a, b});
			}
		}
		cc = 1;
		for (int i = 1; i <= n; i++)
		{
			if (visited[i] == 0)
			{
				dfs(i);
				cc++;
			}
		}
		bool flag = true;

		for (int i = 0; i < p.size(); i++)
		{
			a = p[i].first;
			b = p[i].second;
			if (check[a] == check[b])
			{
				flag = false;
				break;
			}

		}
		if (flag == true)cout << "YES\n";
		else cout << "NO\n";




	}
}
