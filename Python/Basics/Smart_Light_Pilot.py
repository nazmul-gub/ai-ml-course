brightness, threshold = map(int, input().split())

if(brightness >= threshold):
    print("ON")
else:
    print("OFF")