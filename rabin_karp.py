def string_match_naive(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        segment = text[i : i + len(pattern)]
        if segment == pattern:
            return (i, i + len(pattern))
    return (-1, -1)


def string_match_naive_hash(text, pattern):
    hash_pattern = hash(pattern)
    for i in range(len(text) - len(pattern) + 1):
        segment = text[i : i + len(pattern)]
        hash_segment = hash(segment)
        if hash_pattern == hash_segment:
            if segment == pattern:
                return (i, i + len(pattern))
    return (-1, -1)


def string_match_simple_rolling_hash(text, pattern):
    hash_pattern = sum([ord(c) for c in pattern])
    segment = text[0 : len(pattern)]
    hash_segment = sum([ord(c) for c in segment])
    # TODO: I really didn't want the if check in the loop, see if there is a cleaner way
    if hash_pattern == hash_segment:
        if segment == pattern:
            return (0, len(pattern))

    for i in range(1, len(text) - len(pattern) + 1):
        hash_segment = hash_segment - ord(text[i - 1]) + ord(text[i + len(pattern) - 1])
        if hash_pattern == hash_segment:
            segment = text[i : i + len(pattern)]
            if segment == pattern:
                return (i, i + len(pattern))
    return (-1, -1)


def string_match_rolling_hash(text, pattern):
    hash_pattern = sum([ord(c) for c in pattern])
    segment = text[0 : len(pattern)]
    hash_segment = sum([ord(c) for c in segment])
    # TODO: I really didn't want the if check in the loop, see if there is a cleaner way
    if hash_pattern == hash_segment:
        if segment == pattern:
            return (0, len(pattern))

    for i in range(1, len(text) - len(pattern) + 1):
        hash_segment = hash_segment - ord(text[i - 1]) + ord(text[i + len(pattern) - 1])
        if hash_pattern == hash_segment:
            segment = text[i : i + len(pattern)]
            if segment == pattern:
                return (i, i + len(pattern))
    return (-1, -1)


print(string_match_simple_rolling_hash("ooooooooooohello", "hello"))
