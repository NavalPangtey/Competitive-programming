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
	int n; cin >> n;
	int a1, a2, a3, b1, b2, b3;
	cin >> a1 >> a2 >> a3 >> b1 >> b2 >> b3;
	long long m = 1000000000000;
	int max = 0;
	if (a1 <= b2)max = a1;
	else max = b2;

	if (a2 <= b3)max += a2;
	else max += b3;

	if (a3 <= b1)max += a3;
	else max += b1;


	long long c1 = b2 - a2 - a3;
	if (c1 >= 0) m = min(m, c1);
	c1 = b3 - a3 - a1;
	if (c1 >= 0) m = min(m, c1);
	c1 = b1 - a1 - a2;
	if (c1 >= 0) m = min(m, c1);

	if (m == 1000000000000) m = 0;
	cout << m << " " << max << "\n";






}
