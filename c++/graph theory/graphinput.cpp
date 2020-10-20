//Adjacency list implimantaion

#include<bits/stdc++.h>
using namespace std;

void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

int main()
{
	read();
	int a , b, n, m;
	cin >> n >> m;
	vector<int> v[n + 1];
	for (int i = 0 ; i < m; i++)
	{
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}

	for (int i = 1; i <= n; i++)
	{
		for (auto x : v[i])
			cout << x << " ";
		cout << "\n";
	}


}
