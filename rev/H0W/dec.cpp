#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define __ROL__(x, y) __rotl__(x, y)       // Rotate left
#define __ROR__(x, y) __rotr__(x, y)       // Rotate right
// inline int rol (int in, int x) {
//         int res;
//         __asm__ __volatile__("rol  %%eax, %%cl"  :"=a"(res) :"a"(in), "c"(x));
//         return res;
// }

// inline int ror (int in, int x) {
//         int res;
//         __asm__ __volatile__("ror  %%eax, %%cl" :"=a"(res) :"a"(in), "c"(x));
//         return res;
// }
 
// int f0(int a) {
//     return a ^ 0xFACEB00C;
// }
// int f1(unsigned int a) {
//     return a - 74628;
// }
// int f2(unsigned int a1) {
//     return (rol(a1 & 0xAAAAAAAA, 2) | ror(a1 & 0x55555555, 4));
// }
// int f3(unsigned int a) {
//     return f0(f1(f2(a)));
// }
int main(){
    struct tm tm1;
    time_t t1;
    tm1.tm_year = 119;
    tm1.tm_mon = 8;
    tm1.tm_wday = 3;
    tm1.tm_hour = 5;
    tm1.tm_min = 25;
    tm1.tm_sec = 14;
    t1 = mktime(&tm1);
    // printf("%u\n", t1);4294967295
    srand(1567574714);
    // FILE * f = fopen64("secret", "r");
    (3749744-14)/4;
    for(int i=0;i<937421;++i) {
        printf("%d\n",rand());
    }
}