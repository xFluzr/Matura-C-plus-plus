def czy_palindrom(tekst):
    tekst=tekst.lower()
    if (tekst==tekst[::-1]):
        return True
    return False

print(czy_palindrom("ABa"))