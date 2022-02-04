def sequential_map(*funcs):
    cont = funcs[-1]
    funcs = funcs[:-1]
    for func in funcs:
        for i in range(len(cont)):
            cont[i] = func(cont[i])
    return cont


def consensus_filter(*funcs):
    cont = funcs[-1]
    funcs = funcs[:-1]
    answer = list()
    for i in cont:
        counter = 0
        for func in funcs:
            if func(i):
                counter += 1
        if counter == len(funcs):
            answer.append(i)
    return answer


def conditional_reduce(func1, func2, cont):
    good_cont = list(filter(func1, cont))
    while len(good_cont) != 1:
        good_cont[0] = func2(good_cont[0], good_cont[1])
        good_cont.pop(1)
    return good_cont[0]


def func_chain(*funcs):
    def res(arg):
        res = arg
        for func in funcs:
            res = func(res)
        return res
    return res


def sequential_map_new(*funcs):
    cont = funcs[-1]
    funcs = funcs[:-1]
    chain = func_chain(*funcs)
    return list(map(chain, cont))
