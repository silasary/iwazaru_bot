import re

WARNINGS = {
    r'\b(females)\b': 'pretty objectifying, try "women" instead!',
    r'\b(guys)\b': 'exclusionary language. Some alternatives: all, everyone, friends, folks, people',
    r'\b(stupid|retarded|idiotic)\b': 'ableist language. Some alternatives: pathetic, uninspiring, vapid, obtuse',
    r'\b(crazy|insane|bonkers)\b': 'ableist language. Some alternatives: ludicrous, wild, ridiculous, absurd, chaotic, silly, nonsensical, unreal, unbelievable',
    r'\b(mad)\b': 'ableist language. Some alternatives: angry, furious, annoyed',
    r'\b(idiot|idiotic|imbecile|moron|retard|lunatic)\b': 'ableist language. Some alternatives: uninformed, ignorant, incorrect, wrong',
    r'\b(hysterical)\b': 'sexist language. Some alternatives: hilarious, funny',
    r'\b(dumb)\b': 'ableist language. Some alternatives: silly, foolish, ignorant, uninformed, ridiculous, pathetic, absurd',
    r'\b(lame)\b': 'ableist language. Some alternatives: silly, foolish, ridiculous, pathetic, absurd, uncool',
    r'\b(cripple|crippled)\b': 'ableist language. Some alternatives: broken, not working',
    r'\b(psycho|schitzo|schizo|spaz|derp|spastic|spacker)\b': 'ableist language. check out some alternatives! <http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html> (scroll down)',

}

def parse_message(text: str) -> str:
    for key in WARNINGS:
        m = re.search(key, text, re.IGNORECASE)
        if m:
            return 'gentle reminder: {0} is {1}'.format(m.group(0), WARNINGS[key])
    if 'females' in text:
        return 'Saying "females" is pretty objectifying, try "women" instead!'
    if re.match(r'\b(spaz|derp|spastic)\b', text):
        return 'gentle reminder: ableist language. check out some alternatives! <http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html> (scroll down)'
    if re.search(r'\b(guys)\b', text, re.IGNORECASE):
        return 'Gentle reminder: exclusionary language. Some alternatives: all, everyone, friends, folks, people'
    if re.search(r'\b(stupid|retarded|idiotic)\b', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: pathetic, uninspiring, vapid, obtuse'
    if re.search(r'\b(crazy|insane|bonkers)\b', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: ludicrous, wild, ridiculous, absurd, chaotic, silly, nonsensical, unreal, unbelievable'
    if re.search(r'\b(mad)\b', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: angry, furious, annoyed'
    if re.search(r'\b(idiot|idiotic|imbecile|moron|retard|lunatic)\b', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: uninformed, ignorant, incorrect, wrong'
    if re.search(r'\b(hysterical)\b', text, re.IGNORECASE):
        return 'Gentle reminder: sexist language. Some alternatives: hilarious, funny'
    if re.search(r'\b(dumb)\b', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: silly, foolish, ignorant, uninformed, ridiculous, pathetic, absurd'
    if re.search(r'\b(lame)\b', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: silly, foolish, ridiculous, pathetic, absurd, uncool'
    if re.search(r'\b(cripple|crippled)\b', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: broken, not working'
    return None
