count = 0
while True:
    count = count + 1
    if count % 2 == 1:
        continue
    print(f"Hello world times {count}")
    if count == 100:
        break