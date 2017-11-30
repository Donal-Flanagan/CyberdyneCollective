def count():
        filename = raw_input("Please input the filename here: ")
        text = open(filename, "r")
        vow = 0
        cons = 0
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        low = 0
        up = 0
        lowers = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
        uppers = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
        lowersstring = "abcdefghijklmnopqrstuvwxyz"
        uppersstring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        vowelsstring = "aeiou"
        conststring = "bcdfghjklmnpqrstvwxyz"
        vowelupstring = "AEIOU"
        constupstring = "BCDFGHJKLMNPQRSTVWXYZ"
        for line in text:
                chars = len(line)
                linechars = list(line)
                print linechars
                linelowers = 0
                lineuppers = 0
                for i in range(len(lowers)):
                        lowers[i] = lowers[i] + linechars.count(lowersstring[i])
                        low = low + linechars.count(lowersstring[i])
                for i in range(len(uppers)):
                        uppers[i] = uppers[i] + linechars.count(uppersstring[i])
                        up = up + linechars.count(uppersstring[i])
                for i in range(len(vowelsstring)):
                        vow = vow + linechars.count(vowelsstring[i])
                        vow = vow + linechars.count(vowelupstring[i])
                for i in range(len(conststring)):
                        cons = cons + linechars.count(conststring[i])
                        cons = cons + linechars.count(constupstring[i])
        prompt = raw_input("Would you like to count the uppercase AND lowercase instances of each letter (y), or just total instances(n)? ")
        if prompt in ["y", "ye", "yes", "yep"]:
                for letter in range(len(lowers)):
                        print lowersstring[letter], "occurs", lowers[letter], "times."
                for letter in range(len(uppers)):
                        print uppersstring[letter], "occurs", uppers[letter], "times."
        else:
                for letter in range(len(lowers)):
                        print lowersstring[letter], "occurs", lowers[letter]+uppers[letter], "times."
        print "There are", low, "lowercase letters,", up, "uppercase letters,", vow, "vowels and", cons, "consonants in the document."
        print "There are", low + up, "letters in total in the document."
        count()
