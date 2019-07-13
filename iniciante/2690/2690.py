digito = ["GQaku", "ISblv", "EOYcmw", "FPZdnx", "JTeoy", "DNXfpz", "AKUgq", "CMWhr", "BLVis", "HRjt"]
if __name__ == '__main__':
    for i in xrange(input()):
        text = raw_input().replace(" ", "")[0:12]

        out = ""
        for j in text:
            for k in xrange(10):
                if j in digito[k]:
                    out += str(k)
                    break
        print(out)
