#!/usr/bin/env python3
import concurrent.futures


counter = 0


def increment_counter(fake_value):
    global counter
    for _ in range(1000):
        counter += 1


if __name__ == "__main__":
    fake_data = [x for x in range(5000)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5000) as executor:
        executor.map(increment_counter, fake_data)
    print(counter)
