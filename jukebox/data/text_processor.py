import re
from unidecode import unidecode

class TextProcessor():
    def __init__(self, v3=False):
        if v3:
            vocab = '꾸준느것순졌죠플군쩔께오거흥실지세평뭔론원산데잊볼숨차져환황웠복았따밍출린4샴많억수음유성난나채누똑겠어으떻렀곳땐같장달프자서사넘약!.핸리필얼한가닌척블봤럼놀럽열별틋폰염먹집번녕설쩌에노분며추속깊탑의전다걷헷넥킬깨구글쉬밤굴쳐능만당상러반찾냥손비람릴킨내렌이말운맘넌향그~조남슨생심여연스되각점게흑대보까테푸떤불꽃무살아랑너쁜밀선골솔일매젠텐벽바적않웃중레뒤랬예3요항후또면봄주피십터엔더떠픈타든간답름런냐닿려들용겨혼없했끼,직춤히슬흘기물모팅을찮돌두좋랠텀목드잘짧귀금건부빨울치래걸작묻야해빵저란못잠루감늘질빛괜끄째때신새온미할처락줬고였와곁도좀은싶뱉움임과퇴올는년날될네흐멈천껴워녀었정를늦문길파렇꺼굉마흔크인진빠방렸버팠애계발멍옆던근니몇언갈궁하꿈떨영함잡소잔른끝우갔라닐로갑툭취힘앞절있시뤄톤슴안왜알르습형봐친꼈응제판ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?-\'\"()[] \t\n'
            not_vocab = re.compile('[^A-Za-z0-9.,:;!?\-\'\"()\[\] \t\n]+')
        else:
            vocab = '꾸준느것순졌죠플군쩔께오거흥실지세평뭔론원산데잊볼숨차져환황웠복았따밍출린4샴많억수음유성난나채누똑겠어으떻렀곳땐같장달프자서사넘약!.핸리필얼한가닌척블봤럼놀럽열별틋폰염먹집번녕설쩌에노분며추속깊탑의전다걷헷넥킬깨구글쉬밤굴쳐능만당상러반찾냥손비람릴킨내렌이말운맘넌향그~조남슨생심여연스되각점게흑대보까테푸떤불꽃무살아랑너쁜밀선골솔일매젠텐벽바적않웃중레뒤랬예3요항후또면봄주피십터엔더떠픈타든간답름런냐닿려들용겨혼없했끼,직춤히슬흘기물모팅을찮돌두좋랠텀목드잘짧귀금건부빨울치래걸작묻야해빵저란못잠루감늘질빛괜끄째때신새온미할처락줬고였와곁도좀은싶뱉움임과퇴올는년날될네흐멈천껴워녀었정를늦문길파렇꺼굉마흔크인진빠방렸버팠애계발멍옆던근니몇언갈궁하꿈떨영함잡소잔른끝우갔라닐로갑툭취힘앞절있시뤄톤슴안왜알르습형봐친꼈응제판ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?-+\'\"()[] \t\n'
            not_vocab = re.compile('[^A-Za-z0-9.,:;!?\-+\'\"()\[\] \t\n]+')
        self.vocab = {vocab[index]: index + 1 for index in range(len(vocab))}
        self.vocab['<unk>'] = 0
        self.n_vocab = len(vocab) + 1
        self.tokens = {v: k for k, v in self.vocab.items()}
        self.tokens[0] = ''  # <unk> became ''
        self.not_vocab = not_vocab

    def clean(self, text):
        text = unidecode(text)  # Convert to ascii
        text = text.replace('\\', '\n')
        text = self.not_vocab.sub('', text)  # Remove non vocab
        return text

    def tokenise(self, text):
        return [self.vocab[char] for char in text]

    def textise(self, tokens):
        return ''.join([self.tokens[token] for token in tokens])

    def characterise(self, tokens):
        return [self.tokens[token] for token in tokens]
