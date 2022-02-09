name = input('Hello, what is your name? ')
print('Welcome, '+name+'!')
while True:
    inp = input('''How may I help you?
    - Calculator
    - 8-Ball
    - Coin Flip
    ''')
    inp = inp.lower()

    if inp == 'calculator' or inp == 'calc':
        inpcalc = input('''Select a function:
        + Addition
        - Subtraction
        * Multiplication
        / Division
        ^ Power of
        v Square Root
        
        ''')
        inpcalc = inpcalc.lower()
        if inpcalc == '+' or inpcalc == 'addition':
            pf = input('Input your first number: ')
            pfi = int(pf)
            ps = input('Input your second number: ')
            psi = int(ps)
            ans = (pfi + psi)
            print(ans)

        if inpcalc == '-' or inpcalc == 'subtraction':
            sf = input('Input your first number: ')
            sfi = int(sf)
            ss = input('Input your second number: ')
            ssi = int(ss)
            ans = (sfi - ssi)
            print(ans)

        if inpcalc == '*' or inpcalc == 'multiplication':
            mf = input('Input your first number: ')
            mfi = int(mf)
            ms = input('Input your second number: ')
            msi = int(ms)
            ans = (mfi * msi)
            print(ans)

        if inpcalc == '/' or inpcalc == 'division':
            df = input('Input your first number: ')
            dfi = int(df)
            ds = input('Input your second number: ')
            dsi = int(ds)
            ans = (dfi / dsi)
            print(ans)

        if inpcalc == '^' or inpcalc == 'power of':
            pf = input('Input your first number: ')
            pfi = int(pf)
            ps = input('Input your second number: ')
            psi = int(ps)
            ans = (pfi ** psi)
            print(ans)

        if inpcalc == 'v' or inpcalc == 'square root':
            import math
            sq = input('Input your number: ')
            sqi = int(sq)
            ans = math.sqrt(sqi)
            print(ans)


    if inp == 'coin flip' or inp == 'coin':
        import random
        n = random.random()
        int(n)
        if n > .5:
            print('Heads')
        if n < .5:
            print('Tails')

    if inp == '8-ball' or inp == '8' or inp == 'ball':
        input('What is your question? ')
        import random
        n = random.random()
        int(n)
        if .124 > n > 0:
            print('It is certain.')
        if .24 > n > .125:
            print('Outlook good.')
        if .374 > n > .25:
            print('Yes.')
        if .49 > n > .375:
            print('Ask again later.')
        if .624 > n > .5:
            print('It is unlikely.')
        if .874 > n > .625:
            print('Very Doubtful.')
        if 1 > n > .875:
            print('No.')

    if inp == 'exit':
        print('Goodbye!')
        break