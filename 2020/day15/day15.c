#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int target = 30000000;
    int numbers[] = {2, 20, 0, 4, 1, 17};
    size_t n = sizeof(numbers) / sizeof(int);
    int last_spoken = numbers[n - 1];
    int *track = malloc(target * sizeof(int));
    memset(track, 0, target * sizeof(int));
    int i;
    for (i = 0; i < n - 1; i++) {
        *(track + numbers[i]) = i + 1;
    }
    int prev_turn;
    for (prev_turn = n; prev_turn < target; prev_turn++) {
        int new_spoken;
        int v = *(track + last_spoken);
        if (v == 0) {
            new_spoken = 0;
        } else {
            new_spoken = prev_turn - v;
        }
        *(track + last_spoken) = prev_turn;
        last_spoken = new_spoken;
    }
    printf("%d\n", last_spoken);
}
