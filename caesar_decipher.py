# 出現頻度確認用
common_words = {"the", "be", "to", "of", "and", "in", "that", "have", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"}

def count_matching_words(text):
    word_list = set(text.lower().split())
    count = sum(word in common_words for word in word_list)
    return count

def caesar_decrypt_by_word_count(encrypted_text):
    decrypted_texts = []
    max_word_count = 0

    for shift in range(26):
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

        # 復号した平文の単語数をカウント
        word_count = count_matching_words(decrypted_text)
        
        # もっとも合致する単語数が多い平文を保持
        if word_count > max_word_count:
            max_word_count = word_count
            decrypted_texts = [decrypted_text]
        elif word_count == max_word_count:
            decrypted_texts.append(decrypted_text)

    return decrypted_texts
# テスト
# encrypted_text = input()
encrypted_text = "Rkj Y ckij unfbqyd je oek xem qbb jxyi cyijqaud ytuq ev tudekdsydw fbuqikhu qdt fhqyiydw fqyd mqi rehd qdt Y mybb wylu oek q secfbuju qssekdj ev jxu ioijuc, qdt unfekdt jxu qsjkqb juqsxydwi ev jxu whuqj unfbehuh ev jxu jhkjx, jxu cqijuh-rkybtuh ev xkcqd xqffyduii. De edu huzusji, tyibyaui, eh qleyti fbuqikhu yjiubv, rusqkiu yj yi fbuqikhu, rkj rusqkiu jxeiu mxe te dej adem xem je fkhiku fbuqikhu hqjyedqbbo udsekdjuh sediugkudsui jxqj qhu unjhucubo fqydvkb. Deh qwqyd yi jxuhu qdoedu mxe belui eh fkhikui eh tuiyhui je erjqyd fqyd ev yjiubv, rusqkiu yj yi fqyd, rkj rusqkiu essqiyedqbbo syhskcijqdsui esskh yd mxysx jeyb qdt fqyd sqd fheskhu xyc iecu whuqj fbuqikhu. Je jqau q jhylyqb unqcfbu, mxysx ev ki uluh kdtuhjqaui bqrehyeki fxoiysqb unuhsyiu, unsufj je erjqyd iecu qtlqdjqwu vhec yj? Rkj mxe xqi qdo hywxj je vydt vqkbj myjx q cqd mxe sxeeiui je udzeo q fbuqikhu jxqj xqi de qddeoydw sediugkudsui, eh edu mxe qleyti q fqyd jxqj fhetksui de huikbjqdj fbuqikhu?"
decrypted_texts = caesar_decrypt_by_word_count (encrypted_text)
decrypted_texts = caesar_decrypt_by_word_count(encrypted_text)
print("解読されたテキスト候補:")
for text in decrypted_texts:
    print(text)
