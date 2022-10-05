name = input("Name of `HTML` file: ")
print("Creating file...")

try: 
    file = open('index.html', 'x')
    file.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
</body>
</html>""")
    file.close()
except:
    print(f'A file with name \'{name}.html\' already exists in this directory.')
