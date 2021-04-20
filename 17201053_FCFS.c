#include<stdio.h>

void findWaitingTime(int processes[], int n,
                          int bt[],int wt[])
{
    wt[0] = 0;
    int i=1;
    for (i = 1; i < n ; i++ )
        wt[i] =  bt[i-1] + wt[i-1] ;
}

void findavgTime( int processes[], int n, int bt[])
{
    int wt[n],total_wt = 0;
    findWaitingTime(processes, n, bt, wt);

    int i=0;

    for ( i=0; i<n; i++)
    {
        total_wt = total_wt + wt[i];
        printf("%d p%d %d %d|",wt[i],(i+1),bt[i],bt[i]+wt[i]);
    }

   float s=(float)total_wt / (float)n;
    printf("\n");
    printf("Average waiting time = %.2f",s);
}
int main()
{
    int processes[10];
    int i,n;
    printf("process:");
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &processes[i]);
    }


    int  burst_time[10];
    int j,n1;
    printf("burst time:");
    scanf("%d", &n1);
    for (j = 0; j < n1; j++) {

        scanf("%d", &burst_time[j]);
    }


    findavgTime(processes, n, burst_time);
    return 0;
}


