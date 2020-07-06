import Levenshtein

def is_selected(text):
    if(len(text)>0 and len(text)<3):
        return True
    else:
        return False