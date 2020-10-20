#include<bits/stdc++.h>
using namespace std;

vector <int> v[1000];
vector <int> res;
int ind[10001];
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

void khan(int n) {
	queue <int> q;
	for (int i = 1; i <= n; i++)
		if (ind[i] == 0)
			q.push(i);
	while (!q.empty())
	{
		int curr = q.front();
		q.pop();
		res.push_back(curr);
		for (int child : v[curr])
		{
			ind[child]--;
			if (ind[child] == 0)
				q.push(child);
		}
	}

	for (int node : res)
		cout << node << " ";
}

int main()
{
	read();
	int n, m, a, b;
	cin >> n >> m;
	while (m--) {
		cin >> a >> b;
		v[a].push_back(b);
		ind[b]++;
	}
	khan(n);
}
