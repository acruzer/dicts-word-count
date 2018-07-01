def word_count (filename):
	f = open(filename)
	word_lst = []
	for w in f:
		word = w.strip().split(" ")
		word_lst = word_lst + word
	return word_lst

def get_word_count (word_lst):
	word_dic = {}
	for word in word_lst:
		word_dic[word] = word_dic.get(word, 0) + 1
	return (word_dic.items())

def print_dic (word_dic):
	for key in word_dic: 
		print (key[0], key[1])

word_lst = word_count("test.txt")
word_dic = get_word_count(word_lst)
print_dic(word_dic)
# print (get_word_count(word_lst))