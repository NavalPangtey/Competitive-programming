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
	int t;
	cin >> t;
	while (t--)
	{
		int n, m, a;
		cin >> n >> m;
		set<int> s;
		s.clear();
		for (int i = 0; i < n; i++)
		{
			cin >> a;
			s.insert(a);
		}
		int SS = s.size();
		if (m == 1 && SS > 1)cout << "-1" << "\n";
		else
		{	int cc = 1;
			SS = SS - m;
			while (SS > 0) {
				SS -= m - 1;
				cc++;
			}
			cout << cc << "\n";
		}
	}
}
