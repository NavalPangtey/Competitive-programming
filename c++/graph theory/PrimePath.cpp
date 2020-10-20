#include<bits/stdc++.h>
using namespace std;

#define pb push_back

vector<int> v[10000];
vector<int> primes;
int visited[10000], dis[10000];

void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

bool isPrime(int p)
{
	for (int i = 2; i * i <= p; i++)
	{
		if (p % i == 0)
			return false;
	}
	return true;
}

bool isValid(int a, int b)
{
	int count = 0;
	while (a)
	{
		if ((a % 10) != (b % 10))
			count++;
		a /= 10, b /= 10;
	}
	if (count == 1) return true;
	else return false;
}

void buildGraph() {
	for (int i = 1000; i <= 9999; i++)
	{
		if (isPrime(i))
		{
			primes.pb(i);
		}
	}

	for (int i = 0; i < primes.size(); i++)
	{
		for (int j = 0; j < primes.size(); j++)
		{
			int a = primes[i];
			int b = primes[j];

			if (isValid(a, b))
			{
				v[a].pb(b);
				v[b].pb(a);
			}
		}
	}

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
		for (auto child : v[curr])
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





int main()
{
	read();
	buildGraph();
	int t;
	cin >> t;
	while (t--)
	{
		int a, b; cin >> a >> b;
		for (int i = 1000; i <= 9999; i++)
		{
			visited[i] = 0;
			dis[i] = -1;
		}
		bfs(a);

		if (dis[b] == -1)
			cout << "Impossible\n";
		else
			cout << dis[b] << endl;



	}
}
