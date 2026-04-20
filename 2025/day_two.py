from sys import argv
from pathlib import Path

def star_one_validator(_id):
    if len(_id) % 2 == 0:
        return _id[:len(_id)//2] != _id[len(_id)//2:]
    return True

def star_two_validator(_id):
    for sub_str_len in range(1, len(_id)):
        if len(_id) % sub_str_len != 0: continue
        for start_idx in range(0, len(_id), sub_str_len):
            if _id[:sub_str_len] != _id[start_idx:start_idx + sub_str_len]:
                break
        else:
            return False
    return True

def day_two_iterator(inranges, validator):
    result = 0
    ranges = inranges.split(",")
    for _range in ranges:
        start_end = [x.strip() for x in _range.split("-")]
        for i in range(int(start_end[0]), int(start_end[1]) + 1):
            if not validator(str(i)):
                result += i

    print(result)

if __name__ == "__main__":
    ranges = Path(argv[1]).open().readline()
    day_two_iterator(ranges, star_one_validator)
    day_two_iterator(ranges, star_two_validator)

