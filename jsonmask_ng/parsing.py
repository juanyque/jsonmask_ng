from __future__ import unicode_literals


TERMINALS = ['(', ')', ',', '/']


def maybe_add_word(name, tokens):
    name = name.strip()
    if name:
        tokens.append(name)
        name = ''
    return name, tokens


def tokenize_partial_response(text):
    tokens = []
    name = ''

    if not text:
        return tokens

    for ch in text:
        if ch in TERMINALS:
            name, tokens = maybe_add_word(name, tokens)
            tokens.append(ch)

        else:
            name += ch

    name, tokens = maybe_add_word(name, tokens)
    return tokens


def parse_partial_response(tokens) -> dict:
    return _parse_partial_response(tokens, {}, [])


def _parse_partial_response(tokens, parent, stack) -> dict:
    parent = parent.copy()
    props = {}

    while True:
        if not tokens:
            return parent

        token = tokens.pop(0)
        if token not in TERMINALS:

            stack.append(token)
            resp = _parse_partial_response(
                tokens, props.get(token, {}), stack,
            )
            props[token] = resp
            stack.pop()

        elif token == ',':
            return props

        elif token == '/':
            stack.append(token)
            continue

        elif token == '(':
            stack.append(token)
            continue

        elif token == ')':
            return props

        parent.update(props)

        if stack and stack[-1] in ['/']:
            stack.pop()
            return parent

    return parent


def parse_fields(fields) -> dict:
    """Turn a string jsonmask_ng into a Python dictionary representing the desired data pruning.

    You will likely want to call ``jsonmask_ng.mask.apply_json_mask``.

    :fields:    Plain text value or list representing desired structure, e.g., `a,b/c` / ['a', {'b': ['c']}]

    :returns:   dict
    """
    if not fields:
        return {}

    if isinstance(fields, list):
        fields = parse_fields_list(fields)

    return parse_partial_response(
        tokens=tokenize_partial_response(fields),
    )


def parse_fields_list(fields_list) -> str:
    fields_string = ''

    for field in fields_list:
        if isinstance(field, str):
            if fields_string:
                fields_string += ','
            fields_string += field
        elif hasattr(field, "__dict__"):
            field = field.__dict__

        if isinstance(field, dict):
            for key in field:
                if fields_string:
                    fields_string += ','
                fields_string += key
                fields_string += '('
                fields_string += parse_fields_list(field[key])
                fields_string += ')'

    return fields_string
