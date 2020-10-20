#include<bits/stdc++.h>
using namespace std;
long long arr[100001];
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

int find(int a)
{
	while (arr[a] > 0)
		a = arr[a];

	return a;
}

void Union(int a, int b)
{
	arr[a] += arr[b];
	arr[b] = a;
}

int main()
{
	read();
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m, a, b;
	cin >> n >> m;
	for (int i = 1; i <= n; i++)arr[i] = -1;

	while (m--)
	{
		cin >> a >> b;
		a = find(a);
		b = find(b);
		if (a != b)Union(a, b);
	}

	long long int result = 1;
	for (int i = 1; i <= n; i++)
	{
		if (arr[i] < 0)
		{
			result = (result * abs(arr[i])) % 1000000007;
		}

	}

	cout << result;
}
