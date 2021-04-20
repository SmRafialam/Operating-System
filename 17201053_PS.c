#include<stdio.h>

int main()
{
    int bt[10],p[10],wt[10],pr[10],i,j,n,total=0,pos,temp;
    printf("Enter Total Number of Process:");
    scanf("%d",&n);

    printf("\nEnter Burst Time and Priority\n");
    for(i=0;i<n;i++)
    {
        printf("\nP[%d]\n",i+1);
        printf("Burst Time:");
        scanf("%d",&bt[i]);
        printf("Priority:");
        scanf("%d",&pr[i]);
        p[i]=i+1;
    }

    for(i=0;i<n;i++)
    {
        pos=i;
        for(j=i+1;j<n;j++)
        {
            if(pr[j]<pr[pos])
                pos=j;
        }

        temp=pr[i];
        pr[i]=pr[pos];
        pr[pos]=temp;

        temp=bt[i];
        bt[i]=bt[pos];
        bt[pos]=temp;

        temp=p[i];
        p[i]=p[pos];
        p[pos]=temp;
    }

    wt[0]=0;
    for(i=1;i<n;i++)
    {
        wt[i]=0;
        for(j=0;j<i;j++)
            wt[i]+=bt[j];

        total+=wt[i];
    }

    float avg_wt=(float)total/(float)n;
    total=0;

    printf("\nProcess\t    Burst Time    \tWaiting Time\t");

    for ( i=0; i<n; i++)
    {
        total = total + wt[i];
        printf("%d p%d %d %d|",wt[i],(i+1),bt[i],bt[i]+wt[i]);
    }


    for(i=0;i<n;i++)
    {

        total+=bt[i]+wt[i];
        printf("\nP[%d]\t\t  %d\t\t    %d\t\t\t",p[i],bt[i],wt[i]);
    }


    printf("\n\nAverage Waiting Time=%.2f",avg_wt);


	return 0;
}
