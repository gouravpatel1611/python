#include <stdio.h>

int main()
{

    int user_input;
    printf("Enter your number :- ");
    scanf("%d", &user_input);

    int arr[user_input + 1];

    int temp = 1;

    while (1)
    {
        int t = 0;
        for (int i = 0; i < user_input - temp; i++)
        {
            printf("1+");
            arr[t] = 1;
            t++;
        }
        printf("%d", temp);
        arr[t] = temp;
        printf("\n");

        if (temp == user_input)
        {
            break;
        }
        int t2 = 1;
        while(arr[t] - arr[t - t2] > 1)
        {
            arr[t]--;
            arr[t - t2]++;

            for (int i = 0; i <= t - 1; i++)
            {
                printf("%d+",arr[i]);
            }
            printf("%d", arr[t]);
            printf("\n");
            if (arr[t] - arr[t - t2] ==1 || arr[t] - arr[t - t2] ==0)
            {
            t2++;
            }
        }
        temp++;
    }

    return 0;
}