import pickle
dict_db = {}

for c1 in range(256):
    for c2 in range(256):
        state = (c1 << 8) | c2
        save = state
        for k in range(0x76d2):
            state = 21727 * (18199 * ((25561 * (31663 * (-1635 *
                                                         (state ^ 0x6BB1) - 16196) + 14122)) ^ 0x448C) - 11258)
            state = state & 0xffff
        dict_db[state] = save
    print(c1)

with open('dict_db.pickle','wb') as file:
    pickle.dump(dict_db, file, protocol=pickle.HIGHEST_PROTOCOL)
print('done')