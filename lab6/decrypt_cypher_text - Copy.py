def decrypt_cypher_text(encrypted_text, key):
	decrypted_text = ""
	for ch in encrypted_text:
		decrypted_char = chr((ord(ch) - key) % 256)
		decrypted_text += decrypted_char
	return decrypted_text

text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$"
print(decrypt_cypher_text(text, 3))
