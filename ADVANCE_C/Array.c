#include <stdio.h>

int main() {
    int marks[4] = {85, 92, 78, 95};
    int total = 0; // Shuruat mein total 0 hoga

    for(int i = 0; i < 4; i++) {
        total = total + marks[i]; // Ek-ek karke sab plus ho rahe hain
    }

    printf("Saare students ke total marks hain: %d\n", total);

    return 0;
}