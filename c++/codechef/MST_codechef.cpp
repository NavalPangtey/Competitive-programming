#include<bits/stdc++.h>
using namespace std;

int vistited[200001];

void read()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

struct  edge {
	int a;
	int b;
	int w;
};
edge ar[12497502];
int par[200001];


int find(int a)
{
	if (par[a] == -1)return a;
	return  par[a] = find(par[a]);
}


void merge(int a, int b)
{
	par[a] = b;
}

struct vertex
{
	int a = 0;
	int b = 0;
	int c = 0;
	int d = 0;
	int e = 0;

};
vertex arr[200001];


bool comp(edge a , edge b )
{
	if (a.w < b.w)
		return true;
	return false;
}

int main()
{
	read();
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, d;
	cin >> n >> d;
	int D[5];
	for (int i = 0; i < 5; i++)D[i] = 0;
	for (int i = 0; i < n; i++)
	{

		par[i] = -1;
		for (int j = 0; j < d; j++)
			cin >> D[j];
		arr[i].a = D[0];
		arr[i].b = D[1];
		arr[i].c = D[2];
		arr[i].d = D[3];
		arr[i].e = D[4];
	}
	int a, b, w;
	int k = 0;

	for (int i = 0; i < n - 1; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			ar[k].a = i;
			ar[k].b = j;
			ar[k].w = -(abs(arr[j].a - arr[i].a) + abs(arr[j].b - arr[i].b) + abs(arr[j].c - arr[i].c) + abs(arr[j].d - arr[i].d) + abs(arr[j].e-arr[i].e));
			k++;
		}
	}
	int sum = 0;
	int m = (n * (n - 1)) / 2;
	sort(ar, ar + m, comp);

	// for (int i = 0; i < m; i++)
	// {
	// 	cout << ar[i].a << " " << ar[i].b << " " << ar[i].w << "\n";
	// }
	for (int i = 0; i < m; i++)
	{
		a = find(ar[i].a);
		b = find(ar[i].b);

		if (a != b)
		{
			sum += ar[i].w;
			merge(a, b);
		}

	}

	cout << abs(sum);
}
