words = {
'anal': 'sex',
'ass hole': 'ask hole',
'assfucker': 'ask hole',
'asshole': 'ask hole',
'assshole': 'ask hole',
'ass': 'ask',
'black cock': 'pendis',
'cock': 'pendis',
'cockfucker': 'ask hole',
'cocksucker': 'ask hole',
'cunt': 'ask hole',
'dick': 'ask hole',
'faggot': 'ask hole',
'fuck': 'duck',
'fuckass': 'ask hole',
'fuckhole': 'ask hole',
'mother fucker': 'ask hole',
'motherfuck': 'ask hole',
'motherfucker': 'ask hole',
'negro': 'afro-american',
'nigger': 'afro-american',
'orgasm': 'climax',
'pussy': 'vagina',
'slut': 'not a good girl',
'son of a bitch': 'son of a mother',
'viagra': 'v pill',
'whore': 'not a good girl',
'hore': 'not a good girl'
}

def filter(text):
    text = text.lower()
    for k,v in words.items():
        if k in text:
            text = text.replace(k,v)
    return text