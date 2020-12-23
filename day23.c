#include <stdio.h>

unsigned int big_fat_array[1000001] = {0};

int main(int argc, char * argv[]) {
	if (argc < 2) return 1;
	char * c = argv[1];
	while (*(c+1)) {
		big_fat_array[*c - '0'] = *(c + 1) - '0';
		c++;
	}

	big_fat_array[*c-'0'] = 10;
	for (unsigned int i = 10; i <= 1000000; ++i) {
		big_fat_array[i] = i + 1;
	}
	big_fat_array[1000000] = argv[1][0] - '0';

	unsigned int m0 = (argv[1][0] - '0');
	for (unsigned int j = 0; j < 10000000; ++j) {
		unsigned int m1 = big_fat_array[m0];
		unsigned int m2 = big_fat_array[m1];
		unsigned int m3 = big_fat_array[m2];
		big_fat_array[m0] = big_fat_array[m3];
		unsigned int nx = (m0 + (1000000 - 2)) % (1000000) + 1;
		while (nx == m1 || nx == m2 || nx == m3) {
			nx = (nx + (1000000 - 2)) % (1000000) + 1;
		}
		unsigned int px = big_fat_array[nx];
		big_fat_array[nx] = m1;
		big_fat_array[m3] = px;
		m0 = big_fat_array[m0];
	}

	printf("%lu\n", (unsigned long)big_fat_array[1] * (unsigned long)big_fat_array[big_fat_array[1]]);
	return 0;
}
