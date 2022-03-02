from sys import stdin

while dance := stdin.readline().strip().split():
    error = []

    if 'dip' not in dance:
        error.append(5)

    if dance[0] == 'jiggle':
        error.append(4)

    if 'twirl' in dance and 'hop' not in dance:
        error.append(3)

    if dance[-3:] != ['clap', 'stomp', 'clap']:
        error.append(2)

    for i, step in enumerate(dance):
        if step == 'dip':
            if i < len(dance) - 1 and dance[i+1] == 'twirl':
                continue
            if i >= 1 and dance[i - 1] == 'jiggle':
                continue
            if i >= 2 and dance[i - 2] == 'jiggle':
                continue
            dance[i] = step.upper()
            error.append(1)


    if len(error) <= 1:
        if len(error) == 0:
            print(f'form ok: {" ".join((dance))}')
        else:
            print(f'form error {error[0]}: {" ".join(dance)}')
    else:
        print(f'form errors ', end = '')
        while len(error) > 2:
            print(f'{error.pop()}, ', end = '')
        print(f'{error.pop()} and {error.pop()}: {" ".join(dance)}')


