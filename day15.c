/** This solution needs to be built with the ToaruOS app builder */
#include <stdio.h>
#include <toaru/hashmap.h>

int main(int argc, char * argv[]) {
	hashmap_t * seen = hashmap_create_int(1000000);
	hashmap_set(seen, (void*)0, (void*)0);
	hashmap_set(seen, (void*)3, (void*)1);
	intptr_t latest = 6;
	intptr_t turn = 3;
	while (1) {
		if (hashmap_has(seen, (void*)latest)) {
			intptr_t i = turn - (intptr_t)hashmap_get(seen, (void*)latest) - 1;
			hashmap_set(seen, (void*)latest, (void *)(turn - 1));
			latest = i;
		} else {
			hashmap_set(seen, (void*)latest, (void *)(turn - 1));
			latest = 0;
		}
		turn += 1;
		if (turn <= 2020) {
			//printf("On turn %ld, the number said is %ld.\n", turn, latest);
		}
		if (turn == 30000000) {
			printf("On turn %ld, the number said is %ld.\n", turn, latest);
			break;
		}
	}

	return 0;
}
