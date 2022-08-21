import xor_freq_decrypt

freq_analysis_output = []
with open('4.txt', 'r') as file:
    i = 0
    for hex_text in file:
        i += 1
        freq_analysis_output += xor_freq_decrypt.output_top_n_phrase(hex_text, 5)

freq_analysis_output.sort()
for e in freq_analysis_output:
    print(e, end='\n')