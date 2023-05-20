import sys 

# argv in full is argument vector
# if len(sys.argv) == 2:
#     print(f"hello, {sys.argv[1]}!")
# else:
#     print("Hello, world!")

if len(sys.argv) != 2:
    print("Missing commandline arguments!")
    sys.exit(1)
print(f"Hello, {sys.argv[1]}")
