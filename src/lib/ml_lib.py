# import Levenshtein

def is_selected(text):

    if(len(text)>0 and len(text)<4 and text[0]!='_'):
        return True
    else:
        return False