import re
from typing import Optional

WARNINGS = {
    # Sexist/exclusionary language
    r'\b(females)\b': 'pretty objectifying. If you are referring to women, use the gender term instead',
    r'\b(hysterical)\b': 'sexist language. Some alternatives: hilarious, funny',
    r'\b(bimbo|bitch|cunt|hag|slut|twat|whore)\b': 'sexist language',
    # LGBT-related slurs
    r'\b(sissy|pansy|sodomite|poofter|pillow-biter|bugger|fudgepacker|cocksucker|fag|faggot|flamer|ponce|tapette|nola|quean|jocker|poove|woofter)\b': 'a homophobic word or slur used against gay men',
    r'\b(dyke|lesbo)\b': 'a homophobic slur used against gay women',
    r'\b(fauxbian)\b': 'a biphobic slur used against bisexual women',
    r'\b(tranny|trannie|shim|heshe|shehe|she-man|sheman|transtrender|cuntboy|hefemale|shemale|dickgirl|ladyboy|trans-identified)\b': 'A slur or derogatory way of referring to transgender people',
    r'\b(hermie)\b': 'A slur for intersex people',
    r'\b(transvestite)\b': 'a slur for cross-dressers',
    # Mental conditions
    r'\b(stupid|retarded|idiotic)\b': 'ableist language. Some alternatives: pathetic, uninspiring, vapid, obtuse, silly',
    r'\b(crazy|insane|bonkers)\b': 'ableist language. Some alternatives: ludicrous, wild, ridiculous, absurd, chaotic, silly, nonsensical, unreal, unbelievable',
    r'\b(mad)\b': 'ableist language. Some alternatives: angry, furious, annoyed',
    r'\b(idiot|idiotic|imbecile|moron|retard|lunatic)\b': 'ableist language. Some alternatives: uninformed, ignorant, incorrect, wrong',
    r'\b(cretin|cripple|midget|gimp|freak|nutter|schizo|tard|spaz)\b': '',
    # Physical conditions
    r'\b(dumb)\b': 'ableist language. Some alternatives: silly, foolish, ignorant, uninformed, ridiculous, pathetic, absurd',
    r'\b(lame)\b': 'ableist language. Some alternatives: silly, foolish, ridiculous, pathetic, absurd, uncool',
    r'\b(cripple|crippled)\b': 'ableist language. Some alternatives: broken, not working',
    # Racism
    r'\b(gypsy|gipp|pikey|piky)\b': 'a racial slur against the Romani people.',
    r'\b(beaner|beaney|tacohead|wetback)\b': 'a racial slur for Mexican/mestizo people',
    r'\b(chink|chonky|jap|dothead|gook|gooky|nip|slant-eye|slopehead|slopey|sloper|zipperhead)\b': 'a racial slur against Asians',
    r'\b(guido|wop)\b': 'a racial slur for Italians',
    r'\b(gusano)\b': 'a racial slur for Cubans that fled the Cuban Revolution',
    r'\b(injun|nitchie|neche|neechee|neejee|nitchy|nitchee|nidge|redskin|squaw)\b': 'a racial slur for Native Americans',
    r'\b(kanaka)\b': 'a racial slur for Pacific Islanders',
    r'\b(lubra)\b': 'a racial slur for Australian Aboriginal people',
    r'\b(mick)\b': 'a racial slur for people of Irish descent',
    r'\b(polack|polak|polock)\b': 'a racial slur for people of Polish or Slavic origin',
    r'\b(portagee)\b': 'a racial slur for people of Portugese origin',
    r'\b(russki)\b': 'a slur for people of Russian origin',
    r'\b(spic|spick|spik|spig|spigotty)\b': 'a racial slur for a person of Hispanic descent',
    r'\b(wigger|whigger|wigga)\b': 'a racial slur against white people perceived to be "acting black"',
    r'\b(paki|pakki|pak)\b': 'a slur against Pakistanis and Middle-Easterners in general',
    r'\b(nigger|nigga|niggress|nigette|niglet|nig|nigor|nigra|nigre|nigar|niggur|niggah|niggar|nigguh|negro|negroid|groid|coon|coons|burrhead|bluegum|golliwog|kaffir|kaffer|kafir|kaffre|kuffar|mau-mau|mouli|mulignan|mulignon|moolinyan|pickaninny|quashie|rastus|sheboon|spearchucker|thicklips|wog)\b': 'a racial slur against black people.',
    r'\b(savage)\b': "a word that has racist roots in colonial violence against indigenous peoples and shouldn't be used. Some alternatives are: ridiculous, absurd, ruthless, brutal, rough, wild.",
    # Ethno-religious identity
    r'\b(mussie|haji|hajji|hodgie|raghead|towelhead|mohammedan)\b': 'a slur against Muslim people and people whose appearance leads them to be perceived as Muslim like Sikhs',
    r'\b(ayrab|a-rab)\b': 'intentional mispelling of an Arab person meant as a slur',
    r'\b(christ-killer|heeb|hebe|kike|jewboy|sheeny|shylock|yid|yakubian)\b': 'a slur for Jews',
    # catchall ableist (No suggestions)
    r'\b(psycho|schitzo|schizo|spaz|derp|spastic|spacker)\b': 'ableist language. check out some alternatives! <http://www.autistichoya.com/p/ableist-words-and-terms-to-avoid.html> (scroll down)',
}

GUYS_RESPONSE = """Many people feel excluded when you refer to a group of people as "Guys".
Some alternatives if you meant to refer to explicitly men: men, dudes
Some alternatives if you meant to refer to people in general: all, everyone, friends, folks, people"""


def parse_message(text: str) -> Optional[str]:
    for key in WARNINGS:
        m = re.search(key, text, re.IGNORECASE)
        if m:
            return 'gentle reminder: {} is {}'.format(m.group(0), WARNINGS[key])

    if re.search(r'\b(hey|hi|you)\W+(guys)\b', text, re.IGNORECASE):
        return GUYS_RESPONSE

    return None
