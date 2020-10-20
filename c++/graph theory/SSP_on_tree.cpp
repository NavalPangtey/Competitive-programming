#include<bits/stdc++.h>
using namespace std;
#define INF 1000000000

vector<int> v[1001];
int vis[1001], dist[1001];

void read()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

void dfs(int node, int d)
{
    vis[node] = 1;
    dist[node] = d;
    for (int i = 0 ; i < v[node].size(); i++)
    {
        int child = v[node][i];
        if (vis[child] == 0)
            dfs(child, dist[node] + 1);
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
        dist[i] = 0;
    }
    for (int i = 1 ; i <= n - 1; i++)
    {
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    dfs(1, 0);

    cin >> q;
    int min_distace = INF, ans = -1;
    while (q--)
    {
        int girlcity;
        cin >> girlcity;

        if (dist[girlcity] < min_distace)
        {
            min_distace = dist[girlcity];
            ans = girlcity;
        }
        else if (dist[girlcity] == min_distace && girlcity < ans)
            ans = girlcity;

    }
    cout << ans;

}
