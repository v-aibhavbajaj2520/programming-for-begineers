#include <stdio.h>

int isPrime(int num) {
    if (num < 2) {
        return 0; // Not prime
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0; // Not prime
        }
    }
    return 1; // Prime
}

int main() {
    int n, a[100], op, even = 0, odd = 0, prime = 0;

    printf("Enter the number of elements you want to take input: ");
    scanf("%d", &n);

    printf("Enter elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] % 2 == 0) {
            even += a[i];
        } else {
            odd += a[i];
        }
        if (isPrime(a[i])) {
            prime += a[i];
        }
    }

    printf("1) Enter 1 for the sum of even and odd numbers\n");
    printf("2) Enter 2 for the sum of prime numbers\n");
    printf("Enter case number: ");
    scanf("%d", &op);

    switch (op) {
        case 1:
            printf("Sum of even numbers is: %d\n", even);
            printf("Sum of odd numbers is: %d\n", odd);
            break;

        case 2:
            printf("Sum of prime numbers is: %d\n", prime);
            break;

        default:
            printf("Invalid option\n");
    }

    return 0;
}
