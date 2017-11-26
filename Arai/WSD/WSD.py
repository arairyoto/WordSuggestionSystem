from nltk.wsd import lesk

class WSD:
    def __init__(self):
        # initialize freq_table
        self._freqs = {}

    def __getitem__(self, synset):
        return self._freqs[synset]

    def lesk(self, sentence):
        res = []
        sentence = sentence.split(' ')

        for w in sentence:
            try:
                res.append(lesk(sentence, w).name())
            except:
                continue

        return res

    def lesk_process(self, sentence):
        sentence = sentence.split(' ')

        for w in sentence:
            try:
                synset = lesk(sentence, w).name()
                if synset not in self._freqs.keys():
                    self._freqs[synset] = 0
                self._freqs[synset] += 1
            except:
                continue


sample = 'my name is Adam Smith'
sample = '私 名前 is Adam Smith'

wsd = WSD()
wsd.lesk_process(sample)
print(wsd['exist.v.01'])
