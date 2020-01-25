import numpy as np

tunecharsstr = """A Á À Â Ā A̍ Ă
a á à â ā a̍ ă
A͘ Á͘ À͘ Â͘ Ā͘ A̍͘ Ă͘
a͘ á͘ à͘ â͘ ā͘ a̍͘ ă͘
E É È Ê Ē E̍ Ĕ
e é è ê ē e̍ ĕ
E͘ É͘ È͘ Ê͘ Ē͘ E̍͘ Ĕ͘
e͘ é͘ è͘ ê͘ ē͘ e̍͘ ĕ͘
I Í Ì Î Ī I̍ Ĭ
i í ì î ī i̍ ĭ
I͘ Í͘ Ì͘ Î͘ Ī͘ I̍͘ Ĭ͘
i͘ í͘ ì͘ î͘ ī͘ i̍͘ ĭ͘
M Ḿ M̀ M̂ M̄ M̍ M̆
m ḿ m̀ m̂ m̄ m̍ m̆
N Ń Ǹ N̂ N̄ N̍ N̆
n ń ǹ n̂ n̄ n̍ n̆
O Ó Ò Ô Ō O̍ Ŏ
o ó ò ô ō o̍ ŏ
O͘ Ó͘ Ò͘ Ô͘ Ō͘ O̍͘ Ŏ͘
o͘ ó͘ ò͘ ô͘ ō͘ o̍͘ ŏ͘
Ö Ö́ Ö̀ Ö̂ Ȫ Ö̍ Ö̆
ö ö́ ö̀ ö̂ ȫ ö̍ ö̆
U Ú Ù Û Ū U̍ Ŭ
u ú ù û ū u̍ ŭ
U͘ Ú͘ Ù͘ Û͘ Ū͘ U̍͘ Ŭ͘
u͘ ú͘ ù͘ û͘ ū͘ u̍͘ ŭ͘
Ṳ Ṳ́ Ṳ̀ Ṳ̂ Ṳ̄ Ṳ̍
ṳ ṳ́ ṳ̀ ṳ̂ ṳ̄ ṳ̍"""
_tunechars = tunecharsstr.split("\n")
tunechars = []
for i in _tunechars:
  tunechars.append(i.split(" "))
tunechars = [x for x in tunechars if x != '']
print(str(tunechars))
tuneindex = []
for line in tunechars:
  tuneindex.append(line[0])
print(str(tuneindex))

"""
调号	1	2	3	4	5	6	7	8
传统调名	阴平	阴上	阴去	阴入	阳平	阳上	阳去	阳入
白话字	a	á	à	ap/at/ak/ah	â	ǎ	ā	a̍p/a̍t/a̍k/a̍h
"""
# 2, 3, 5, 7, 8
# ṳ ṳ́ ṳ̀ ṳ̂ ṳ̄ ṳ̍
# 0 1 2 3 4 5
#           0,    1, 2, 3, 4   , 5, 6   , 7, 8, 9]
_tunelist = [0, None, 1, 2, None, 3, None, 4, 5, None]
# 在这里定义每一个声调对应的位置
tunelist = []
for i in _tunelist:
  _i = 0 if i == None else i
  tunelist.append(_i)
# 将 None 替换成 0

def tunechar(char, num):
  try:
    result = tunechars[tuneindex.index(char)][tunelist[num]]
  except:
    if num <0 or num > 9:
      cl = "Tone mark ranges from 0 to 9."
    else:
      try:
        charindex = tuneindex.index(char)
      except: 
        cl = "Char accepted value:['A', 'a', 'A͘', 'a͘', 'E', 'e', 'E͘', 'e͘', 'I', 'i', 'I͘', 'i͘', 'M', 'm', 'N', 'n', 'O', 'o', 'O͘', 'o͘', 'Ö', 'ö', 'U', 'u', 'U͘', 'u͘', 'Ṳ', 'ṳ']." 
      else:
        cl = "Unexpected Exception."
    print(cl)
    # raise Exception(cl)
    return (char)
  else:
    return result

def tunesyllable(syl):
  leng = len(syl)
  if leng > 1:
    num = syl[-1]
    if num.isdigit():
      syl = syl[:-1]
      num = int(num)
      print("syl:" + syl)
    else:
      num = 0
  else:
    num = 0
 
  vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
  counts = []
  for v in vowels:
    counts.append(syl.count(v))
  sumup = np.sum(counts) # 计算元音总数
  if sumup == 1: # 数组中只有一个元素的值是 1
    # If the syllable has one vowel, that vowel should be tone-marked
    _v = vowels[counts.index(1)]
    print(_v)
    _syl = syl.split(_v)
    _syl = tunechar(_v, num).join(_syl)

  elif sumup == 0:
    # If the syllable has no vowel, mark the nasal consonant
    _syl = ""
  else:
     _syl = ""
  """
If a diphthong contains ⟨i⟩ or ⟨u⟩, the tone mark goes above the other vowel; viz. ⟨ia̍h⟩, ⟨kiò⟩, ⟨táu⟩
If a diphthong includes both ⟨i⟩ and ⟨u⟩, mark the ⟨u⟩; viz. ⟨iû⟩, ⟨ùi⟩
If the final is made up of three or more letters, mark the second vowel (except when rules 2 and 3 apply); viz. ⟨goán⟩, ⟨oāi⟩, ⟨khiáu⟩
If ⟨o⟩ occurs with ⟨a⟩ or ⟨e⟩, mark the ⟨o⟩ (except when rule 4 applies); viz. ⟨òa⟩, ⟨thóe⟩

  """
  return _syl

def tunepara(text):
  words = text.split(" ")
  _words = []
  for word in words:
    syls = word.split("-")
    syls = [tunesyllable(syl) for syl in syls]
    word = "-".join(syls)
    _words.append(word)
  return " ".join(_words)
  

print(tunechar("a", 5))
print(tunesyllable("chang5"))
print(tunesyllable("a4"))
print(tunepara("chang5-chang4 chang2-chak8"))