#include <stdio.h>
#include <stdlib.h>

// Counting Sort for each digit place
void CountingSort(int A[], int n, int exp) {
    // Creates count & output array
    int B[n];
    int C[10] = {0};  

    // Counts occurrences of digits
    for (int i= 0; i < n; i++)
        C[(A[i] / exp)% 10]++;

    // Gets the final position of digits in sorted order
    for (int i = 1; i < 10; i++)
        C[i] += C[i -1];

    // Places the elements into the output array
    for (int i =n - 1; i >= 0; i--) {
        B[C[ (A[i] / exp) % 10] - 1] = A[i];
        C[ (A[i] / exp) % 10]--;
    }

    // copy sorted elements back to A
    for (int i= 0; i < n; i++)
        A[i] = B[i];
}

int getMax(int A[], int n) {
    int max = A[0];
    for (int i = 1; i < n; i++)
        if (A[i] > max)
            max = A[i];
    return max;
}

void RadixSort(int A[], int n) {

    int max = getMax(A, n); // getting the max number

    // for loop to apply counting sort to each digit starting at lease to most significant 
    for (int exp= 1; max /exp >0; exp *= 10) {
        CountingSort(A, n, exp);
    }
}

int main() {
    int A[] = {12, 23, 76, 876, 34, 6, 34 ,87, 4}; 
    int n = sizeof(A) / sizeof(A[0]); // Gets the number of elements

    RadixSort(A, n);

    // Prints the sorted array
    for (int i= 0; i < n; i++)
        printf("%d ", A[i]);
    printf("\n");

}