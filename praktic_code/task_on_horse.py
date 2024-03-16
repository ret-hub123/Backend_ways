
def count_horses(sound_str):
    s = sound_str
    list_s = [word for word in s]
    horse = []
    fl = False
    
    
    for i in range(1, len(list_s)):
            while int(list_s[i - 1]) > 0:
                for j in range(i - 1, len(list_s), i):
                    if int(list_s[j]) > 0:
                        list_s[j] = str(int(list_s[j]) - 1)
                        fl = True
                if fl == True:
                    horse.append(i)

    return horse