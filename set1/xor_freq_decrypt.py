import numpy
from collections import Counter

freq = {"E": "12.02", "T": "9.10", "A": "8.12", "O": "7.68", "I": "7.31", "N": "6.95", "S": "6.28", "R": "6.02", "H": "5.92", "D": "4.32", "L": "3.98", "U": "2.88", "C": "2.71",
        "M": "2.61", "F": "2.30", "Y": "2.11", "W": "2.09", "G": "2.03", "P": "1.82", "B": "1.49", "V": "1.11", "K": "0.69", "X": "0.17", "Q": "0.11", "J": "0.10", "Z": "0.07"}


h = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# A~z


def output_top_n_phrase(hex_text, output_n):
    ranked_phrases = []  # [(score, phrase)]
    for i in range(256):
        h_bytes = bytes.fromhex(hex_text)
        numpy_h_bytes = numpy.frombuffer(h_bytes, dtype="uint8")

        to_xor = bytes([i])
        numpy_to_xor = numpy.frombuffer(to_xor, dtype="uint8")

        # XOR each byte
        xored_bytes = (numpy_h_bytes ^ numpy_to_xor).tobytes()

        phrase = None
        try:
            phrase = xored_bytes.decode('ascii')
        except:
            continue # some ordinals are not in range(128)

        freq_data = freq_analysis(phrase)
        if not freq_data:
            continue

        ranked_phrases.append(freq_data)

    ranked_phrases.sort()
    return ranked_phrases[:output_n]


def freq_analysis(phrase) -> tuple((int, str)):  # (delta, phrase)
    upper_clean_phrase = phrase_to_upper_clean(phrase)
    n = len(upper_clean_phrase)
    if n == 0:
        return None

    # evaluate how far from the "ideal" frequency the phrase is
    clean_phrase_counter = Counter(upper_clean_phrase)
    agg = 0
    n = len(upper_clean_phrase)
    for c, v in clean_phrase_counter.items():
        percentage = (v/n) * 100
        agg += abs(float(freq[c]) - percentage)
    return (agg, phrase)


def phrase_to_upper_clean(phrase):
    # convert to uppercase so that we can easily check with the freq list
    upper_phrase = phrase.upper()

    # get rid of special characters and numbers for evaluation
    clean_phrase = []
    for c in upper_phrase:
        if c.isalpha():
            clean_phrase.append(c)
    return ''.join(clean_phrase)


#print(output_top_n_phrase(h, 10))
