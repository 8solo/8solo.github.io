def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
    
    if isinstance(field_name, str):
        field_name = field_name.replace(',', ' ').split()
    field_names = list(map(str, field_name))
    typename = _sys.intern(str(typename))

    if rename:
        seen = set()
        for index, name in enumerate(field_names):
            if (not name.isidentifier()
                or _iskeyword(name)
                or name.startwith('_')
                or name in seen):
                field_names[index] = f'_{index}'
            seen.add(name)

    for name in [typename] + field_names:
        if type(name) is not str:
            raise TypeError('Type names and field names must be strings')
        if not name.isidentifier():
            raise ValueError('Type names and field names must be valid '
                             f'keyword: {name!r}')
        if _iskeyword(name):
            raise
