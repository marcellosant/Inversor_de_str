def inverter_string(string):
    string_invertida = ''
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string_normal = input('Digite algo:')
string_invertida = inverter_string(string_normal)
print("String normal:", string_normal)
print("String invertida:", string_invertida)
