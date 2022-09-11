import re
# обучение


with open('data/база.txt', encoding='utf-8', mode='r') as my_file:
    text = my_file.read()

# очистка от цифр
corpus = re.split(r'\W+', text)

corpus = [word.lower() for word in corpus]
vocab = set(corpus)

# считаем количество каждой двуграммы и триграммы
uni_counter = {}
bi_counter = {}

for i in range(0, len(corpus)-1):
    uni = corpus[i]
    bi = (corpus[i], corpus[i+1])
    if uni in uni_counter.keys():
        uni_counter[uni] += 1
    else:
        uni_counter[uni] = 1
    if bi in bi_counter.keys():
        bi_counter[bi] += 1
    else:
        bi_counter[bi] = 1
vocab.remove('')


# программа, предлагающая следующее слово
def next_word(input_):
    c_input = input_.split()
    last_uni = str(c_input[-1])
    p = {}
    for vocab_word in vocab:
        i_uni = last_uni
        i_bi = (last_uni, vocab_word) # итерируемая биграмма

        i_uni_counter = uni_counter.get(i_uni, 0)
        i_bi_counter = bi_counter.get(i_bi, 0)

        p[vocab_word] = i_bi_counter / i_uni_counter

    suggested_word = max(p, key=p.get)
    return suggested_word

# генерация


print('Введите фразу, которую вы хотитие продолжить и количество слов, сколько нужно добавить')
phrase = input()
test = phrase.split()
while test[-1] not in vocab:
    print('такое слово не встречается:( введите пожалуйста другое')
    phrase = input()
    test = phrase.split()
n = int(input())
for i in range(0, n):
    new_word = next_word(phrase)
    phrase += (' ' + new_word)
print(phrase)

