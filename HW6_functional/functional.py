def sequential_map(*funcs):
    cont = funcs[-1]
    funcs = funcs[:-1]
    for func in funcs:
        cont = func(cont)
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
    good_cont = list()
    for i in cont:
        if func1(i):
            good_cont.append(i)
    return func2(good_cont[0], good_cont[1])


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
    return func_chain(*funcs)(cont)
