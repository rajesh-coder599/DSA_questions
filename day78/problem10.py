# 2472. Maximum Number of Non-overlapping Palindrome Substrings



def maxPalindromes(s,k):
    n=len(s)
    memo=[[-1 for _ in range(n)] for _ in range(n)]
    def solve(i,p):
        if i>=n:
            return 0
        if memo[i][p]!=-1:
            return memo[i][p]
        ans=-float("inf")
        take=-float("inf")
        temp=-float("inf")
        if i-p+1>=k:
            check=True
            a=i
            b=p
            while a>=b:
                if s[a]!=s[b]:
                    check=False
                    break
                a-=1
                b+=1
            if check:
                take=1+solve(i+1,i+1)
        if i>p:
            temp=solve(i,p+1)
        not_take=solve(i+1,p)
        ans=max(take,not_take,temp)
        memo[i][p]=ans
        return memo[(i,p)]
    return solve(0,0)

s="eztvgkslhpovldnuwnipbyfgizvrjxpnwdsbblcccihakpowopkahiccclbbsdwnpxjrvzigfybpinwundlvophlskgvtsoenjbjgviujwusbpdjfoxtptwhtuhfhsjfydqruurqdyfjshfhuthwtptxofjdpbsuwjuivgjbjneoszipcoinhssgywylctqwwyhcokrgsodsovzxwpgpmxzagqrlrqgazxmpgpwxzvosdosgrkochywwqtclywygsshniocaexrxwdcquxwuvycjhkofixqxfbsemyqafhhafpwmpjmhgegwehhonfnohhewgeghmjpmwpfahhfaqymesbfxqxifokhjcyvuwwyqlbwusdbnbzlboyqpnxetfoufxryhsplgrafulxosrwbnflfnbwrsoxlufarglpshyrxfuoftexnpqyoblzbnbdsuwblqychpetsnumzgkwnbcmwleuwgybhdiwhyhbxymymldzeovnawanvoezdlmymyxbhyhwidhbygwuelwmcbnwkgzmunstepjomcvuinqlsmmcrdttevmydibsibhrtambywwwhkhwwwybmatrhbisbidymvettdrcmmslqniuvcmojnhlswlsvuhxwudotsdgavdgxezxxmgwuogkmaarpnilvlolvlinpraamkgouwgmxxzexgdvagdstoduwxhuvsuornahdetpwgqfmnjdfjmbjhudisfnzfedgnmpnmowyzzywomnpmngdefznfsiduhjbmjfdjnmfqgwptedhanrowozrrqqbkboribjqkvqgmktpzilgvnlvxevxnjysgontkwbbwktnogsyjnxvexvlnvglizptkmgqvkqjbirobkbqqrrzoyjezbxhhhfgmjsackasxspmquzdaocnsaqnaopyngdotlvrrvltodgnypoanqasncoadzuqmpsxsakcasjmgfhhhxbzqnvwfpptwmqrjmctbdjrgsmlzrkztgriitwumiziinqmurzeezrumqniizimuwtiirgtzkrzlmsgrjdbtcmjrqmwtppfvbjlqmuyaahvtvwtjxxyuhtvwyiqhgefbaxjwdusylmfmhhmfmlysudwjxabfeghqiywvthuyxxjtwvtvhaayumqljbuciotqzmuvwvtfcrmoqsxlwtquskypdaqgcaisbtpafdrdfaptbsiacgqadpyksuqtwlxsqomrcftvwvumzqtvkvcvzmqkkvcnbmawfzydygypmjfhhmaowfmhthgxbbxghthmfwoamhhfjmpygydyzfwambncvkkqmzvcvkvketufpzfrvxcqmfsyqepbwtmzexqzqfxcegbjppafyktxwsufldggdlfuswxtkyfappjbgecxfqzqxezmtwbpeqysfmqcxvrfzpfutbvghvliqnsqagcrqnprpquotusjfarezavutnhbacmmcabhntuvazerafjsutouqprpnqrcgaqsnqilvhgvbtmytudwfrdjtcjiqhjiabyloubzjwcsssmcgunodkxamsnwvouaggauovwnsmaxkdonugcmssscwjzbuolybaijhqijctjdrfwhwwftnmimpbxmdvmbdbkpmrsdsqekgcisfetzcqizjjpgekyubjgekgnorongkegjbuykegpjjziqcztefsicgkeqsdsrmpkbdbmvdmxbpmgnwbsblowbvmgcxyizppeuhzllytfocvxojppzobgkpttpkgbozppjoxvcoftyllzhueppziyxcgmvbwolbsbwngtlbyxvfipkgcbhgunjgiuwhpzkhbpyssdsjxoaayoiahfjgyygjfhaioyaaoxjsdssypbhkzphwuigjnughbcgkpifvxnwobedvtoabcgxlpdxolfkymkjovfgevsrhizhvknjvfiiyaiiayiifvjnkvhzihrsvegfvojkmykfloxdplxgcbaotvdw"
k=79
print(maxPalindromes(s,k))