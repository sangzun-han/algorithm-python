from base64 import b64decode

t = int(input())

for tc in range(t):
    print("#{} {}".format(tc+1, b64decode(input()).decode("UTF-8")))
