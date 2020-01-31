import numpy as np

tunecharsstr = """
A Á À Â Ā A̍ Ă
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
ṳ ṳ́ ṳ̀ ṳ̂ ṳ̄ ṳ̍
""".strip()
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


def is_alphabet(uchar):
  """判断一个unicode是否是英文字母"""
  if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
    return True
  else:
    return False
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
  _syl = syl
  if leng > 1:
    num = syl[-1]
    if num.isdigit():
      syl = syl[:-1]
      num = int(num)
    else:
      return syl
  else:
    return syl
  
  # 转换成全部小写，再转换回去
  is_cap=[]
  if syl.islower():
    c_low = True
  elif syl.istitle():
    c_title = True
  elif syl.isupper():
    c_upper = True
  else:
    for x in syl:
      is_cap.append(x.isupper())
  
  _syl = syl
  vowels = [ 'a',  'e',  'i',  'o',  'u']
  counts = []
  booleans = []
  for v in vowels:
    counts.append(syl.count(v))
  sumup = np.sum(counts) # 计算元音总数
  def contains(vowel):
    return counts[vowel.index(vowel)] > 0
  for x in syl:
    is_v = False
    if (is_alphabet(x)):
      for v in vowels:
        if v == x:
          is_v = True
          break
    booleans.append(is_v)

  def tunespecific(text, index, _tune):
    if isinstance(index, int):
      ini = text[0:index]
      mid = text[index]
      end = text[index + 1:]
      return ini + tunechar(mid, _tune) + end
    else:
      return text.replace(index, tunechar(index, _tune))
  if sumup == 1: # 数组中只有一个元素的值是 1
    # If the syllable has one vowel, that vowel should be tone-marked
    _v = vowels[counts.index(1)]
    _syl = syl.split(_v)
    _syl = tunechar(_v, num).join(_syl)
  elif sumup == 0:
    # If the syllable has no vowel, mark the nasal consonant(m or n)
    if contains("n"):
      return tunespecific(syl, "n", num)
    elif contains("m"):
      return tunespecific(syl, "m", num)

  elif sumup == 2:
    if contains("u") and contains("i"):
      return tunespecific(syl, "u", num)
    elif contains("u") or contains("i"):
      _index = 0
      for b in booleans:
        if b:
          char = syl[_index]
          if char != "u" and char != "i":
            return tunespecific(syl, char, num)
        _index += 1
    elif contains("o"):
      return tunespecific(syl, "o", num)
  
  c = 0
  _c = 0
  for b in booleans:
    if b:
      c += 1
    if c == 2:
      return tunespecific(syl, _c, num)
    _c += 1
  return _syl
    # !===== TODO =====
    
"""
if 没有元音
  m or n 加调
elif 只有一个元音
  return 该元音加调
elif 有两个元音
  if 含有 u, i
    return u 加调
  elif 含有 u or i
    return 另一个元音加调
  elif 含有 o
    return o 加调
return 第二个元音加调
"""


def tunepara(text):
  # ===== TODO =====
  # 需要处理更复杂的文本
  words = text.split(" ")
  _words = []
  for word in words:
    syls = word.split("-")
    # ===== TODO ======
    # 动词后有趋向动词时两者连写，如：cháu--chhut-khì（走出去，即跑出去）。（备注：此时趋向动词与动词之间为双连字号，且趋向动词须读为轻声。）
    syls = [tunesyllable(syl) for syl in syls]
    word = "-".join(syls)
    _words.append(word)
  return " ".join(_words)


print(tunechar("a", 5))
print(tunesyllable("chang5"))
print(tunesyllable("a4"))

print(tunepara("mo͘-e si7 chit8-e5 Jit8-gi2 siok8-oe7 chu2-iau3 e5 i3-su3 si7 kong2 tui3 anime, bang3-gah, tian7-tong7 kak-sek e5 kah-i3 kam2-kak. test au5 ai5 ae5 ea5 oe5 meua5-iau5-eo5 ea5-aeaq5"))
# Current output: mo͘-e sī chi̍t-ê Ji̍t-gí siok8-oe7 chú-iau3 ê ì-sù sī kóng tui3 anime, bàng-gah, tian7-tōng kak-sek ê kah-ì kám-kak.