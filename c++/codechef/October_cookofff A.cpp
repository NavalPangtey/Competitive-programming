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
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	read();
	int a, n, k;
	cin >> n >> k;
	priority_queue<int, vector<int>, greater<int>> q;
	for (int i = 0; i < n; i++)
	{
		cin >> a;
		q.push(a);
		if (q.size() > k)q.pop();
	}
	cout << q.top();

}
