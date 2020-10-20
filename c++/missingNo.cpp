#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
int arr[10001];

void read()
{
#ifndef ONLINE_JUD
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

int main()
{
	read();
	ll n, a;
	cin >> n;
	ll sum1 = 0;
	ll sum2 = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> a, arr[i] = a;
		sum1 += a;
		sum2 += pow(a, 2);

	}

	ll s1 = (n * (n + 1)) / 2;
	ll s2 = (n * (n + 1) * ((2 * n) + 1)) / 6;
	ll eq1 = s1 - sum1;
	ll eq2 = s2 - sum2;
	ll eq3 = eq2 / eq1;
	ll missing = (eq1 + eq3) / 2;
	ll duplicate = eq3 - missing;
	cout << "missing: " << missing << "\n";
	cout << "duplicate: " << duplicate << "\n";

}
