def four_digits(A, B, C, D):

    l = [A, B, C, D]
    h = []

    try:
        for i, v in enumerate(s):
            if len(h) == 1:
                m = max(list(filter(lambda x: x <= v[1] if h[0] <= 1 else x <= v[0], l)))
            else:
                m = max(list(filter(lambda x: x <= v[0], l)))
            h.append(m)
            l.remove(m)
    except ValueError:
        return "NOT POSSIBLE"

    return "%s%s:%s%s" % tuple(h)

    return "NOT POSSIBLE"
