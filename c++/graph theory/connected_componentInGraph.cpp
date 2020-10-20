#include<bits/stdc++.h>
using namespace std;

vector<int> v[100000];
int vis[100000];

void read()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

void dfs(int node)
{
    vis[node] = 1;
    for (int i = 0 ; i < v[node].size(); i++)
    {
        int child = v[node][i];
        if (vis[child] == 0)
            dfs(child);
    }

}


int main()
{

    read();
    int a , b, n, m;
    cin >> n >> m;
    for (int i = 0 ; i <= n; i++)
    {
        vis[i] = 0;
    }
    for (int i = 0 ; i < m; i++)
    {
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    int count = 0;
    for (int i = 1; i <= n; i++)
    {
        if (vis[i] == 0)
        {
            dfs(i);
            count++;
        }
    }
    cout << count;

}
