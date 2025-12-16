"""
Yksinkertainen password_utils moduuli.

Sisältää:
- is_strong_password(password) -> (bool, list): perusvahvuustarkistus, palauttaa True ja tyhjän listan jos vahva.
- generate_password(length=12) -> str: generoi salasanan, varmistaa tarvittaessa vähintään yhden merkkiluokan.
"""

import re
import random
import string

def is_strong_password(password):
    """
    Tarkistaa perusvahvuuden:
    - pituus vähintään 8
    - sisältää pienen kirjaimen
    - sisältää ison kirjaimen
    - sisältää numeron
    - sisältää erikoismerkin
    Palauttaa (is_strong, feedback_list) suomeksi.
    """
    feedback = []
    if not password:
        return False, ["Salasana on tyhjä."]

    if len(password) < 8:
        feedback.append("Pituus alle 8 merkkiä (käytä vähintään 8).")

    if not re.search(r"[a-z]", password):
        feedback.append("Lisää pieniä kirjaimia (a-z).")

    if not re.search(r"[A-Z]", password):
        feedback.append("Lisää isoja kirjaimia (A-Z).")

    if not re.search(r"\d", password):
        feedback.append("Lisää numeroita (0-9).")

    if not re.search(r"[{}]".format(re.escape(string.punctuation)), password):
        feedback.append("Lisää erikoismerkki (esim. !@#%).")

    is_strong = len(feedback) == 0
    return is_strong, feedback

def generate_password(length=12):
    """
    Generoi satunnaisen salasanan. Minimipituus 8.
    Varmistaa, että mukana on vähintään yksi pieni kirjain, yksi iso kirjain,
    yksi numero ja yksi erikoismerkki (jos pituus sen sallii).
    """
    if length < 8:
        length = 8

    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    while len(chars) < length:
        chars.append(random.choice(all_chars))

    random.shuffle(chars)
    return ''.join(chars)