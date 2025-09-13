import time,sys


indent = 0
indent_increasing = True
try:
    while True:
        print(' '*indent, end= '')
        print('*'*8)
        time.sleep(.1)
        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()


print("adding webhok")
print("adding webhok")
