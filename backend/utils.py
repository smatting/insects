from sqlalchemy.ext.declarative import DeclarativeMeta


def to_dict(obj, rels=[], backref=None):
    '''
    Turn models to dicts. Nested relationships listed in `rels` are turned to dicts too,
    otherwise they are missing. Hacky, barely tested.

    From https://mmas.github.io/sqlalchemy-serialize-json
    '''
    res = {}
    for key in dir(obj):
        if key.startswith('_') or key in ['metadata']:
            continue
        else:
            res[key] = getattr(obj, key)

    # res = {column.key: getattr(obj, attr)
    #        for attr, column in obj.__mapper__.c.items()}

    if len(rels) > 0:
        items = obj.__mapper__.relationships.items()

        for attr, relation in obj.__mapper__.relationships.items():
            if attr not in rels:
                continue

            if hasattr(relation, 'table'):
                if backref == relation.table:
                    continue

            value = getattr(obj, attr)
            if value is None:
                res[relation.key] = None
            elif isinstance(value.__class__, DeclarativeMeta):
                res[relation.key] = to_dict(value, backref=obj.__table__, rels=rels)
            else:
                res[relation.key] = [to_dict(i, backref=obj.__table__, rels=rels)
                                     for i in value]
    return res
