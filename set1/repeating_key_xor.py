import numpy

def xor_encrypt_using_key(phrase: str, key: str) -> hex:
    if not key or not phrase:
        raise Exception('key or phrase not provided')

    # padding phrase
    multiplier = len(phrase) // len(key)
    if len(phrase) % len(key) > 0:
        multiplier += 1
    extended_key = (key*multiplier)[:len(phrase)]

    key_b = bytes(extended_key, 'utf-8')
    key_b_numpy = numpy.frombuffer(key_b, 'uint8')
    phrase_b = bytes(phrase, 'utf-8')
    phrase_b_numpy = numpy.frombuffer(phrase_b, 'uint8')

    xor_result_b = (phrase_b_numpy ^ key_b_numpy).tobytes()
    return xor_result_b.hex()


key = 'ICE'
print(xor_encrypt_using_key("""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""", key))

