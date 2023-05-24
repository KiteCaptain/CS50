def mario(width):
    if width == 0:
        return
    print("#" * width )
    mario(width - 1)
        
mario(10)