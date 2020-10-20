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
int main()
{
	read();
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t; cin >> t;
	while (t--)
	{
		int n , k, ans;
		cin >> n >> k;
		bool flag = false;
		for (int i = 0; i < n ; i++)cin >> arr[i];
		for (int i = 0; i < n - 1; i++)
		{
			if (arr[i] < k) {
				ans = i + 1;
				flag = true;
				break;
			}
			arr[i + 1] += arr[i] - k;
		}
		if (flag == true)cout << ans << "\n";
		else {
			if (arr[n - 1] < k)cout << n << "\n";
			else
			{
				ans = (arr[n - 1] / k) + (n - 1);
				cout << ans + 1 << "\n";
			}

		}



	}
}
