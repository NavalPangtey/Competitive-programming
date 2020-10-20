#include <iostream>
using namespace std;

int main() {
     long int i,j,t;
	cin>>t;
	for(i=0;i<t;i++)
	{
	     long int n,m;
	     cin>>n>>m;
	     int f[n],p[n];
	     for(j=0;j<n;j++)
	     cin>>f[j];
	     for(j=0;j<n;j++)
	     cin>>p[j];
	     
	     int count[m],c[m];
	     for(j=0;j<m;j++){
	     count[j]=0;
	     c[j]=0;
	     }
	     for(j=0;j<n;j++){
	     count[f[j]-1]+=p[j];
	     c[f[j]-1]++;
	     }
	     
	     
	     long int min;
	     for(j=0;j<m;j++)
	     {
	          if(c[j]!=0)
	          {
	               min=count[j];
	               break;
	          }
	     }
	     for(j=0;j<m;j++)
	     {
	          if(count[j]<=min && c[j]!=0)
	          min=count[j];
	     }
	     cout<<min<<endl;
	}
	return 0;
}