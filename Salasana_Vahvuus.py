import re
import random
import string

def is_strong_password(password):
    """
    Tarkistaa vahvuuden:
     pituus vähintään 8 merkkiä
     sisältää pienen kirjaimen
     sisältää ison kirjaimen
     sisältää numeron
     sisältää erikoismerkin
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
