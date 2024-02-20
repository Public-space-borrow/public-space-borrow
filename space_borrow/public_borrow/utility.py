def check_sequence(registers: list) -> bool:
    if len(registers) < 3:
        return False
    registers.sort()
    count = 1
    for i in range(len(registers) - 1):
        if registers[i + 1] - registers[i] == 1:
            count += 1
        else:
            if count > 2:
                return True
            else:
                count = 1
    return count > 2