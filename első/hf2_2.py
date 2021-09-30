cordinate_1_a = 2
cordinate_1_b = 5

cordinate_2_a = 6
cordinate_2_b = 12


cordinate_distance = ((cordinate_1_a - cordinate_1_b * cordinate_1_a - cordinate_1_b) + (cordinate_2_a - cordinate_2_b * cordinate_2_a - cordinate_2_b)) / ((cordinate_1_a - cordinate_1_b * cordinate_1_a - cordinate_1_b) + (cordinate_2_a - cordinate_2_b * cordinate_2_a - cordinate_2_b))

print("A", cordinate_1_a, cordinate_1_b, "koordinátájú és", cordinate_2_a, cordinate_2_b, "koordinátájú pontok távolsága:", cordinate_distance, ".")