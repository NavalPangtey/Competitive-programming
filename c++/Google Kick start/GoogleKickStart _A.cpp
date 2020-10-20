#include<bits/stdc++.h>
using namespace std;

vector <int> v;
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
	int t; cin >> t;
	int tt = 1;
	while (t--)
	{

		int ans = 0;
		string s;
		string s2, s3;
		cin >> s;
		for (int i = 0; i < s.length(); i++)
		{

			if (i + 3 < s.length())
			{
				for (int j = i; j < i + 4; j++)
				{
					s2 = s2 + s.at(j);
				}
			}
			if (i + 4 < s.length())
			{
				for (int j = i; j < i + 5; j++)
				{
					s3 = s3 + s.at(j);
				}
			}

			if (s2 == "KICK")v.push_back(1);
			if (s3 == "START") v.push_back(0);
			s2 = "";
			s3 = "";

		}

		if (v.empty() == true) ans = 0;
		else if (v.size() == 1) ans = 0;
		else
		{
			for (int i = 0; i < v.size(); i++)
			{
				if (v[i] == 1)
				{
					for (int j = i; j < v.size(); j++)
					{
						if (v[j] == 0)ans++;
					}
				}
			}
		}

		cout << "Case #" << tt << ": " << ans << endl;
		tt++;
		v.clear();

	}
	return 0;

}
