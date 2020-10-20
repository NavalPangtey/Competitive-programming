#include<bits/stdc++.h>
using namespace std;
void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}



void solve()
{
	int x1, y1, x2, y2, ans = 0;
	cin >> x1 >> y1 >> x2 >> y2;

	int DirectionA = -1; //up 0
	int DirectionB = -1; //down 1



	if (x1 == x2 && y1 == y2) {
		cout << 0 << "\n";
		return;
	}

	if (x1 == -9 && y1 == 5)
	{
		ans++;
		x1 = 1;
		y1 = 5;
	}
	if (x2 == -9 && y2 == 5)
	{
		ans++;
		x2 = 1;
		y2 = 5;
	}
	if (x1 == 9 && y1 == 5)
	{
		ans++;
		x1 = -1;
		y1 = 5;
	}
	if (x2 == 9 && y2 == 5)
	{
		ans++;
		x2 = -1;
		y2 = 5;
	}

	if (x1 == 7 && y1 == 3)
	{
		ans++;
		x1 = 1;
		y1 = 3;
	}
	if (x2 == 7 && y2 == 3)
	{
		ans++;
		x2 = 1;
		y2 = 3;
	}
	if (x1 == -7 && y1 == 3)
	{
		ans++;
		x1 = -1;
		y1 = 3;
	}
	if (x2 == -7 && y2 == 3)
	{
		ans++;
		x2 = -1;
		y2 = 3;
	}

	if ((x1 == -7 && y1 == 9) && (x2 == 7 && y2 == 5) || (x2 == -7 && y2 == 9) && (x1 == 7 && y1 == 5) )
	{
		ans = 1;
		cout << ans << "\n";
		return;
	}


	if ((x1 == -7 && y1 == 9))
	{
		x1 = -3;
		y1 = 5;
		ans += 2;
	}
	if ((x2 == -7 && y2 == 9))
	{
		x2 = -3;
		y2 = 5;
		ans += 2;
	}

	if ((x1 == 7 && y1 == 5))
	{
		x1 = -3;
		y1 = 5;
		ans += 1;
	}
	if ((x2 == 7 && y2 == 5))
	{
		x2 = -3;
		y2 = 5;
		ans += 1;
	}



	if ((x1 == 7 && y1 == 9) && (x2 == -7 && y2 == 5) || (x2 == 7 && y2 == 9) && (x1 == -7 && y1 == 5) )
	{
		ans = 1;
		cout << ans << "\n";
		return;
	}


	if ((x1 == 7 && y1 == 9))
	{
		x1 = 3;
		y1 = 5;
		ans += 2;
	}
	if ((x2 == 7 && y2 == 9))
	{
		x2 = 3;
		y2 = 5;
		ans += 2;
	}

	if ((x1 == -7 && y1 == 5))
	{
		x1 = 3;
		y1 = 5;
		ans += 1;
	}
	if ((x2 == -7 && y2 == 5))
	{
		x2 = 3;
		y2 = 5;
		ans += 1;
	}



	if ((x1 == 7 && y1 == 9) && (x2 == -7 && y2 == 5) || (x2 == 7 && y2 == 9) && (x1 == -7 && y1 == 5) )
	{
		ans = 1;
		cout << ans << "\n";
		return;
	}


	if ((x1 == 7 && y1 == 9))
	{
		x1 = 3;
		y1 = 5;
		ans += 2;
	}
	if ((x2 == 7 && y2 == 9))
	{
		x2 = 3;
		y2 = 5;
		ans += 2;
	}

	if ((x1 == -7 && y1 == 5))
	{
		x1 = 3;
		y1 = 5;
		ans += 1;
	}
	if ((x2 == -7 && y2 == 5))
	{
		x2 = 3;
		y2 = 5;
		ans += 1;
	}

	if ((x1 == 9 && y1 == 7) && (x2 == -5 && y2 == 7) || (x2 == 9 && y2 == 7) && (x1 == -5 && y1 == 7))
	{
		ans = 1;
		cout << ans << "\n";
		return;
	}

	if ((x1 == 9 && y1 == 7) && (x2 == 5 && y2 == 3) || (x2 == 9 && y2 == 7) && (x1 == 5 && y1 == 3))
	{
		ans = 2;
		cout << ans << "\n";
		return;
	}

	if ((x1 == -5 && y1 == 7) && (x2 == 5 && y2 == 3) || (x2 == -5 && y2 == 7) && (x1 == 5 && y1 == 3))
	{
		ans = 1;
		cout << ans << "\n";
		return;
	}

	if ((x1 == 9 && y1 == 7) || (x1 == -5 && y1 == 7) || (x1 == 5 && y1 == 3))
	{
		if (x1 == 9)ans += 3;
		else if (x1 == -5)ans += 2;
		else ans += 1;
		x1 = -1;
		y1 = 3;
	}

	if ((x2 == 9 && y2 == 7) || (x2 == -5 && y2 == 7) || (x2 == 5 && y2 == 3))
	{
		if (x2 == 9)ans += 3;
		else if (x2 == -5)ans += 2;
		else ans += 1;
		x2 = -1;
		y2 = 3;
	}




	if ((x1 == -9 && y1 == 7) && (x2 == 5 && y2 == 7) || (x2 == -9 && y2 == 7) && (x1 == 5 && y1 == 7))
	{
		ans = 1;
		cout << ans << "\n";
		return;
	}

	if ((x1 == -9 && y1 == 7) && (x2 == -5 && y2 == 3) || (x2 == -9 && y2 == 7) && (x1 == -5 && y1 == 3))
	{
		ans = 2;
		cout << ans << "\n";
		return;
	}

	if ((x1 == 5 && y1 == 7) && (x2 == -5 && y2 == 3) || (x2 == 5 && y2 == 7) && (x1 == -5 && y1 == 3))
	{
		ans = 1;
		cout << ans << "\n";
		return;
	}

	if ((x1 == -9 && y1 == 7) || (x1 == 5 && y1 == 7) || (x1 == -5 && y1 == 3))
	{
		if (x1 == -9)ans += 3;
		else if (x1 == 5)ans += 2;
		else ans += 1;
		x1 = 1;
		y1 = 3;
	}

	if ((x2 == -9 && y2 == 7) || (x2 == 5 && y2 == 7) || (x2 == -5 && y2 == 3))
	{
		if (x2 == -9)ans += 3;
		else if (x2 == 5)ans += 2;
		else ans += 1;
		x2 = 1;
		y2 = 3;
	}





	// cout << x1 << " " << y1 << " " << x2 << " " << y2 << "\n";




	int a, b;
	a = y1 % x1;
	b = y2 % x2;
	if (x1 > 0)
	{
		if (a == 1)DirectionA = 0;
		else if (a == 0)DirectionA = 0;
		else DirectionA = 1;
	}
	else {
		if (a == 1)DirectionA = 1;
		else if (a == 0)DirectionA = 1;
		else DirectionA = 0;
	}

	if (x2 > 0)
	{
		if (b == 1)DirectionB = 0;
		else if (b == 0)DirectionB = 0;
		else DirectionB = 1;
	}
	else {
		if (b == 1)DirectionB = 1;
		else if (b == 0)DirectionB = 1;
		else DirectionB = 0;
	}


	if (abs(x1) == 1 && abs(x2) == 1)
	{
		if (x1 > 0)
		{
			if (x2 < 0)
			{
				while (1)
				{
					y1 = y1 - 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;

					if (x1 == x2 && y1 == y2)
						break;
				}

			}
			else if (y2 < y1)
			{
				while (y1 != y2)
				{
					y1 = y1 - 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}

			} else
			{
				while (y1 != y2)
				{
					y1 = y1 + 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}

			}

		} else {
			if (x2 > 0)
			{
				while (1)
				{
					y1 = y1 + 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
					if (x1 == x2 && y1 == y2)
						break;
				}

			}
			else if (y2 < y1)
			{
				while (y1 != y2)
				{
					y1 = y1 + 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}

			} else
			{
				while (y1 != y2)
				{
					y1 = y1 - 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}

			}

		}
		cout << ans << "\n";
	}
	else if (abs(x1) == abs(x2))
	{
		if (DirectionA == DirectionB)
		{
			if (x1 > 0)
			{
				if (x2 < 0)
				{
					while (y1 != y2)
					{
						y1 = y1 - 2 * x1;
						if (y1 < 0)y1 = abs(y1), x1 = -x1;
						ans++;
					}
					cout << ans << "\n";
				}
				else if (y2 > y1)
				{

					while (y1 != y2)
					{
						y1 = y1 + 2 * x1;
						if (y1 < 0)y1 = abs(y1), x1 = -x1;
						ans++;
					}
					cout << ans << "\n";
				}
				else
				{
					while (y1 != y2)
					{
						y1 = y1 - 2 * x1;
						if (y1 < 0)y1 = abs(y1), x1 = -x1;
						ans++;
					}
					cout << ans << "\n";
				}
			}
			else {

				if (x2 > 0)
				{
					while (y1 != y2)
					{
						y1 = y1 + 2 * x1;
						if (y1 < 0)y1 = abs(y1), x1 = -x1;
						ans++;
					}
					cout << ans << "\n";

				}
				else if (y2 > y1)
				{
					while (y1 != y2)
					{
						y1 = y1 - 2 * x1;
						if (y1 < 0)y1 = abs(y1), x1 = -x1;
						ans++;
					}
					cout << ans << "\n";
				}
				else {
					while (y1 != y2)
					{
						y1 = y1 + 2 * x1;
						if (y1 < 0)y1 = abs(y1), x1 = -x1;
						ans++;
					}
					cout << ans << "\n";

				}

			}
		}
		else if (DirectionA != DirectionB)
		{
			while (y1 != 1)
			{
				if (x1 < 0)
				{
					y1 = y1 + 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}
				else
				{
					y1 = y1 - 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;

				}
			}

			if (x1 > 0)
			{
				int temp = x1;
				while (-temp != x1)
				{
					x1 = x1 - (2 * y1);
					ans++;
				}
			} else {
				int temp = x1;
				while (-temp != x1)
				{
					x1 = x1 + (2 * y1);
					ans++;
				}
			}

			if (x2 < 0)
			{
				while (y1 != y2)

				{	y1 = y1 - 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}
			}
			else {
				while (y1 != y2)
				{	y1 = y1 + 2 * x1;
					if (y1 < 0)y1 = abs(y1), x1 = -x1;
					ans++;
				}
			}

			cout << ans << "\n";

		}
	}
	else if (x1 != x2)
	{
		while (y1 != 1)
		{
			if (x1 < 0)
			{
				y1 = y1 + 2 * x1;
				if (y1 < 0)y1 = abs(y1), x1 = -x1;
				ans++;
			}
			else
			{
				y1 = y1 - 2 * x1;
				if (y1 < 0)y1 = abs(y1), x1 = -x1;
				ans++;

			}
		}
		while (y2 != 1)
		{
			if (x2 < 0)
			{
				y2 = y2 + 2 * x2;
				if (y2 < 0)y2 = abs(y2), x2 = -x2;
				ans++;
			}
			else
			{
				y2 = y2 - 2 * x2;
				if (y2 < 0)y2 = abs(y2), x2 = -x2;
				ans++;

			}
		}

		if (x1 > x2)
		{
			// int temp = x1;
			while (x1 != x2)
			{
				x1 = x1 - (2 * y1);
				ans++;
			}
		} else {
			// int temp = x1;
			while (x2 != x1)
			{
				x1 = x1 + (2 * y1);
				ans++;
			}
		}
		cout << ans << "\n";
	}


}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	read();
	int t; cin >> t;
	while (t--)
	{
		solve();
	}
}
