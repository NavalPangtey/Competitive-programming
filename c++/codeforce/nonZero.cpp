#include<bits/stdc++.h>
using namespace std;
int a[2000001];
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
	int n; cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	long long ans = 0, sum = 0;
	set <long long> s;
	s.insert(0);
	for (int i = 0; i < n; i++)
	{
		sum += a[i];
		if (s.count(sum) == 1)
		{
			ans += 1;
			s.clear();
			s.insert(0);
			sum = a[i];
		}
		s.insert(sum);
	}
	cout << ans << "\n";
}
