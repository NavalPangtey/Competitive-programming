#include<bits/stdc++.h>
using namespace std;
int arr[100001];
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

bool isvalid(int n) {
	int k = (log2(n));

	int a = (pow(2, k));
	if (a == n)return true;
	else return false;

}

int main()
{
	read();
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t; cin >> t;

	while (t--)
	{
		int n ;
		cin >> n;
		if (n == 1)cout << 1 << "\n";
		else if (isvalid(n))cout << -1 << "\n";
		else if (n == 3)cout << 1 << " " << 3 << " " << 2 << "\n";
		else {
			for (int i = 1; i <= n; i++)
			{
				arr[i] = i;
			}

			arr[1] = 2;
			arr[2] = 3;
			arr[3] = 1;
			int i = 4;
			while ( i < n)
			{
				if (isvalid(arr[i]))
				{	arr[i] = arr[i + 1], arr[i + 1] = i;
					i += 2;
				}
				i++;
			}
			for (int i = 1; i <= n; i++)
			{
				cout << arr[i] << " ";
			}
			cout << "\n";

		}

	}
}
