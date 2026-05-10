# encoding message

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    al={
        "a":"z",
        "b":"y",
        "c":"x",
        "d":"w",
        "e":"v",
        "f":"u",
        "g":"t",
        "h":"s",
        "i":"r",
        "j":"q",
        "k":"p",
        "l":"o",
        "m":"n",
        "n":"m",
        "o":"l",
        "p":"k",
        "q":"j",
        "r":"i",
        "s":"h",
        "t":"g",
        "u":"f",
        "v":"e",
        "w":"d",
        "x":"c",
        "y":"b",
        "z":"a"
    }

    final_string=""
    i=0
    while i<n:
        if i+1<n:
            a=s[i]
            b=s[i+1]
            temp=al[b]+al[a]
            final_string+=temp
        else:
            final_string+=al[s[i]]
            break
        i+=2
    print(final_string)

