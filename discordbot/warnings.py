import re

def parse_message(text: str) -> str:
    if 'females' in text:
        return 'Saying "females" is pretty objectifying, try "women" instead!'
    # if re.match(r'(spaz|derp|spastic)', text):
    #     return 'gentle reminder: ableist language. check out some alternatives! http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html (scroll down)'
    if 'guys' in text:
        return 'Gentle reminder: exclusionary language. Some alternatives: all, everyone, friends, folks, people'
    if re.search(r'stupid|retarded|idiotic', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: pathetic, uninspiring, vapid, obtuse'
    if re.search(r'crazy|insane|bonkers', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: ludicrous, wild, ridiculous, absurd, chaotic, silly, nonsensical, unreal, unbelievable'
    if re.search(r'mad', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: angry, furious, annoyed'
    if re.search(r'idiot|idiotic|imbecile|moron|retard|lunatic', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: uninformed, ignorant, incorrect, wrong'
    if re.search(r'hysterical', text, re.IGNORECASE):
        return 'Gentle reminder: sexist language. Some alternatives: hilarious, funny'
    if re.search(r'dumb', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: silly, foolish, ignorant, uninformed, ridiculous, pathetic, absurd'
    if re.search(r'lame', text, re.IGNORECASE):
        return 'Gentle reminder: ableist language. Some alternatives: silly, foolish, ridiculous, pathetic, absurd, uncool'
    return None
