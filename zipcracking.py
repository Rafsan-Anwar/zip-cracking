import zipfile


zipped = 'ark.zip'
passFile = 'tst.txt'

f = open(passFile, 'r')
passwds = f.read().split()
f.close()

zip_file = zipfile.ZipFile(zipped)
print(zip_file.filename)

for passwd in passwds:
    try:
        zip_file.extractall(pwd=passwd.encode())
        print("matched. The password is " + passwd)
        break
    except:
        print(passwd + " did not match")

