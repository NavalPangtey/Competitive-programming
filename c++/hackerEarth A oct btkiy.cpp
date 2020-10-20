#include<bits/stdc++.h>
using namespace std;

void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

string getString(char x)
{

	string s(1, x);

	return s;
}
vector <char> v;
int main()
{
	read();
	int t; cin >> t;
	while (t--)
	{

		double n;
		int a;
		cin >> n >> a;
		string s = to_string(n);
		bool flag = false, flag2 = true;
		int cc = 0;
		for (int i = s.length() - 1; i >= 0; i--) {
			if (flag == true)
			{
				v.push_back(s.at(i));
				cc++;
				if ((cc == 3 && flag2 == true && i != 0) || (cc == 2 && flag2 == false && i != 0))
				{
					flag2 = false;
					v.push_back(',');
					cc = 0;
				}

			}
			else if (s.at(i) == '.')
			{
				v.push_back('.');
				flag = true;
			}
			else v.push_back(s.at(i));
		}
		bool flag3 = false;
		int cc2 = 0;
		for (auto it = v.rbegin() ; it != v.rend(); it++)
		{

			if (flag3 == true)
			{
				cc2++;
				if (cc2 == a)
				{
					int sss = stoi(getString(*(it + 1))) ;
					if (sss >= 5)
						cout << stoi(getString(*it)) + 1;
					else cout << *it;
				} else cout << *it;

				if (cc2 == a)break;

			}
			else if (*it == '.')
			{	if (a == 0)break;
				cout << *it;
				flag3 = true;

			} else {
				if (a == 0 &&  *(it + 1) == '.')
				{
					int sss = stoi(getString(*(it + 2))) ;
					if (sss > = 5)
						cout << stoi(getString(*it)) + 1;
					else cout << *it;
				} else cout << *it;
			}
		}
		cout << "\n";
		v.clear();

	}





}

