def transform_subject_number(sn, ls):
    v = 1
    for _ in range(ls):
        v = (v * sn) % 20201227
    return v


def determine_loop_size(pk):
    sn, v, ls = 7, 1, 0
    while v != pk:
        v = (v * sn) % 20201227
        ls += 1
    return ls


def main():
    # card_pk = 5764801
    # door_pk = 17807724
    card_pk = 12090988
    door_pk = 240583
    card_ls = determine_loop_size(card_pk)
    ek = transform_subject_number(door_pk, card_ls)
    print(ek)


if __name__ == "__main__":
    main()
