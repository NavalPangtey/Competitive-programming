#include<iostream>
using namespace std;
int main()
{
  int t=0,n=0,m=0;
  cin>>t;
        while(t--)
        { 
                cin>>n;
                cin>>m;
                int F[n],P[n];
                for(int i=0;i<n;i++)
                cin>>F[i];
                for(int i=0;i<n;i++)
                cin>>P[i];
                int sum[m];
                int c[m];
                for(int i=0;i<m;i++)
                {
                   sum[i]=0;
                   c[i]=0;

                }
                
                for(int j=0;j<n;j++)
                {
                  sum[F[j]-1]+=P[j];
                  c[F[j]-1]++;
                }
              /*  while(v<m)
                {   
                    int s=0;
                    for(int i=0;i<n;i++)
                    {
                          if(F[i]==v+1)
                                s=P[i]+s;
                    }          
                    sum[v]=s;
                    v++;
                } */
                
                int temp =0;      
                
              //  for(int i=0;i<m;i++)
                //cout<<sum[i];
                
                temp = sum[0];
                for(int i=0; i<m; i++)
                {
                        if(temp>sum[i]) 
                        {
                             temp=sum[i];
                        }
              
   
                }  
                
                if(temp==0)
                { int k=m;
                  
                  for(int i=0;i<m;++i)
                  {
                  if(sum[i]==0)
		 {
		        int p=i;                                  
                        for(int j=p;j<m;j++)
                        sum[j]=sum[j+1];
                                                          
                        k--;
                 }  
                  }    	                        
		              	                         
                	                
                                     temp = sum[0];	
                                    for(int i =0; i<k; i++)
                                    {
                                            if(temp>sum[i]) 
                                            {
                                                     temp=sum[i];
                                            }
                     
                        
                                    }
                        
                }
                
                
           
     
         cout<<temp<<endl;
         
    
  
       
        }

  return 0;
}
   