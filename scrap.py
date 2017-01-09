'^01 |02 |03 |04 |05 |06 |07 |08 |09 |010 |011 |012 |013 |014 |015 |016 |017 |18 |19 |20 |021 |022 |023 |024 |025 |026 |027 |028 |029 |030 |031 |032 |033 |034 |035 |036 |037 |038 |039 |040 |041 |042 |043 |044 |045 |046 |047'


def get_similar(X):
    ids = X.index
    text = [x.split(" ") for x in X.text]
    m = len(map(len, text))
    Names = []
    for i in range(m):
        name = set([x[i] for x in text])
        n = len(name)
        if n == 1:
            Names.append(name.pop())
        else:
            return " ".join(Names)
    return " ".join(Names)


def get_names(X):
    name = get_similar(X)
    i = X["index"]
    return zip(i, repeat(name, len(i)))
    



def make_number(x):
    try:
        return int(x)
    except:
        return x



def get_max_min(X):
    res = [x for x in X.values]
    res1 = filter(lambda x: isinstance(x[-1], int), res)
    if len(res1) > 1:
        Max = max(res1, key=lambda x: x[-1])
        Min = min(res1, key=lambda x: x[-1])
        return [Max, Min]
    elif len(res1) == 1:
        return {"max": res1[0]}
    elif len(res1) == 0 and len(res) == 1:
        return res
        
        
    
    
           
