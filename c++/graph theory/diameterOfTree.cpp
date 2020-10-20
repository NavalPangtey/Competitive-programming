#include<bits/stdc++.h>
using namespace std;
#define INF 1000000000

vector<int> v[10001];
int vis[10001];

void read()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}
int maxd, dnode;
void dfs(int node, int d)
{
    vis[node] = 1;
    if (d > maxd)
    {
        maxd = d;
        dnode = node;
    }
    for (int i = 0 ; i < v[node].size(); i++)
    {
        int child = v[node][i];
        if (vis[child] == 0)
            dfs(child, d + 1);
    }

}


int main()
{

    read();
    int a , b, n, q;
    cin >> n ;
    for (int i = 0 ; i <= n; i++)
    {
        vis[i] = 0;
    }
    for (int i = 1 ; i <= n - 1; i++)
    {
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    maxd = -1;
    dfs(1, 0);
    int u = dnode;
    maxd = -1;
    for (int i = 0 ; i <= n; i++)
    {
        vis[i] = 0;
    }
    dfs(u, 0);
    cout << maxd;

}
