import re

def parse_message(text: str) -> str:
    if 'females' in text:
        return 'Saying "females" is pretty objectifying, try "women" instead!'
    # if re.match(r'(spaz|derp|spastic)', text):
    #     return 'gentle reminder: ableist language. check out some alternatives! http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html (scroll down)'
    if 'guys' in text:
        return 'Gentle reminder: exclusionary language. Some alternatives: all, everyone, friends, folks, people'
    if re.match(r'stupid|retarded|idiotic', text):
        return 'Gentle reminder: ableist language. Some alternatives: pathetic, uninspiring, vapid, obtuse'
    if re.match(r'crazy|insane|bonkers', text):
        return 'Gentle reminder: ableist language. Some alternatives: ludicrous, wild, ridiculous, absurd, chaotic, silly, nonsensical, unreal, unbelievable'
    if re.match(r'mad', text):
        return 'Gentle reminder: ableist language. Some alternatives: angry, furious, annoyed'
    if re.match(r'idiot|idiotic|imbecile|moron|retard|lunatic', text):
        return 'Gentle reminder: ableist language. Some alternatives: uninformed, ignorant, incorrect, wrong'
    if re.match(r'hysterical', text):
        return 'Gentle reminder: sexist language. Some alternatives: hilarious, funny'
    if re.match(r'dumb', text):
        return 'Gentle reminder: ableist language. Some alternatives: silly, foolish, ignorant, uninformed, ridiculous, pathetic, absurd'
    if re.match(r'lame', text):
        return 'Gentle reminder: ableist language. Some alternatives: silly, foolish, ridiculous, pathetic, absurd, uncool'
    return None
