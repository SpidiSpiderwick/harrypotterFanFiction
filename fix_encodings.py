
def fix_windows_encoding(text):
    ## 8 bytes
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xe2\x80\x9c", "–".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xe2\x80\x9d", "—".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xe2\x84\xa2", "’".encode("utf-8"))
    
    ## 7 bytes
    
    text = text.replace(b"\xc3\xa2\xe2\x80\x9a\xc2\xac", "€".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xc2\xa1", "‡".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x80\x9e\xc2\xa2", "™".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xc2\xa2", "•".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xc2\xb0", "‰".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xc2\xb9", "‹".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xc2\xba", "›".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xcb\x9c", "‘".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xe2\x82\xac\xc5\x93", "“".encode("utf-8"))
    
    ## 6 bytes (NOT IN OPFFICIAL LIST)
    text = text.replace(b"\xc3\xa2\xc2\x82\xc2\xac", "€".encode("utf-8"))
    text = text.replace(b"\xc3\xa2\xc2\x80\xc2\xba", "›".encode("utf-8"))
    
    ## 5 bytes
    
    # \xc3\xa2\xe2\x82\xac
    text = text.replace(b"\xc3\xa2\xe2\x82\xac", "”".encode("utf-8"))
    # \xc3\x83\xe2
    text = text.replace(b"\xc3\x83\xe2\x80\x9a", "Â".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\x9e", "Ä".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\xa0", "Æ".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\xa1", "Ç".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\xa2", "Õ".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\xa6", "Å".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\x93", "Ö".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\x94", "×".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\x98", "Ñ".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\x99", "Ò".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\x9c", "Ó".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\x9d", "Ô".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\xb0", "É".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\xb9", "Ë".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x80\xba", "Û".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x82\xac", "À".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xe2\x84\xa2", "Ù".encode("utf-8"))
    # \xc3\x85\xe2\x80
    text = text.replace(b"\xc3\x85\xe2\x80\x99", "Œ".encode("utf-8"))
    text = text.replace(b"\xc3\x85\xe2\x80\x9c", "œ".encode("utf-8"))
    # \xc3\x8b
    text = text.replace(b"\xc3\x8b\xe2\x80\xa0", "ˆ".encode("utf-8"))
    
    ## 4 bytes
    
    # \xc3\x81\xc2
    text = text.replace(b"\xc3\x81\xc2\xa9", "é".encode("utf-8"))
    # \xc3\x82\xc2
    text = text.replace(b"\xc3\x82\xc2\xa1", "¡".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xa2", "¢".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xa3", "£".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xa4", "¤".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xa5", "¥".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xa6", "¦".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xa7", "§".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xa8", "¨".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xa9", "©".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xaa", "ª".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xab", "«".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xac", "¬".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xad", "".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xae", "®".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xaf", "¯".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb0", "°".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb1", "±".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb2", "²".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb3", "³".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb4", "´".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb5", "µ".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb6", "¶".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb7", "·".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb8", "¸".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xb9", "¹".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xba", "º".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xbb", "»".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xbc", "¼".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xbd", "½".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xbe", "¾".encode("utf-8"))
    text = text.replace(b"\xc3\x82\xc2\xbf", "¿".encode("utf-8"))
    # \xc3\x85\xc2
    text = text.replace(b"\xc3\x83\xc2\xa1", "á".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xa2", "â".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xa3", "ã".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xa4", "ä".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xa5", "å".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xa6", "æ".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xa7", "ç".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xa8", "è".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xa9", "é".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xaa", "ê".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xab", "ë".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xac", "ì".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xae", "î".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xaf", "ï".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb0", "ð".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb1", "ñ".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb2", "ò".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb3", "ó".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb4", "ô".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb5", "õ".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb6", "ö".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb7", "÷".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb8", "ø".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xb9", "ù".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xba", "ú".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xbb", "û".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xbc", "ü".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xbd", "ý".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xbe", "þ".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc2\xbf", "ÿ".encode("utf-8"))
    # \xc3\x83\xc5
    text = text.replace(b"\xc3\x83\xc5\x92", "Ì".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc5\x93", "Ü".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc5\xa0", "Ê".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc5\xa1", "Ú".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc5\xb8", "ß".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc5\xbd", "Î".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xc5\xbe", "Þ".encode("utf-8"))
    # \xc3\x83\xc6
    text = text.replace(b"\xc3\x83\xc6\x92", "Ã".encode("utf-8"))
    # \xc3\x83\xcb
    text = text.replace(b"\xc3\x83\xcb\x86", "È".encode("utf-8"))
    text = text.replace(b"\xc3\x83\xcb\x9c", "Ø".encode("utf-8"))
    # \xc3\x85\xc2
    text = text.replace(b"\xc3\x85\xc2\xa1", "š".encode("utf-8"))
    text = text.replace(b"\xc3\x85\xc2\xb8", "Ÿ".encode("utf-8"))
    text = text.replace(b"\xc3\x85\xc2\xbd", "Ž".encode("utf-8"))
    text = text.replace(b"\xc3\x85\xc2\xbe", "ž".encode("utf-8"))
    # \xc3\x8b
    text = text.replace(b"\xc3\x8b\xc5\x93", "˜".encode("utf-8"))
    
    ## 4 bytes
    
    # \xc3\x83
    text = text.replace(b"\xc3\x83", "à".encode("utf-8"))
    
    ## 2 bytes
    
    text = text.replace(b"\xc3\x82", "".encode("utf-8"))
    
    return text
