def compressWord(input):
    buffer = None
    output = ""
    cnt = 1
    for ch in input:
        if buffer is None:
            output += ch
            buffer = ch
        else:
            if buffer == ch:
                cnt += 1
            else:
                output += str(cnt)
                cnt = 1
                output += ch
                buffer = ch

    output += str(cnt)

    if len(output) > len(input) :
        return input
    else:
        return output