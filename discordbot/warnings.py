import re

def parse_message(text: str) -> str:
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
