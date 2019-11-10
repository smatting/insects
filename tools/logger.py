import json
import os
import dateutil.parser
import datetime
import copy
import uuid
import sys
import docopt
import re


def gen_id():
    return str(uuid.uuid4()).replace('-', '')

def add_row(filename, d):
    with open(filename, 'a') as f:
        f.write(json.dumps(d) + '\n')

def get_last_line(filename):
    with open(filename, "rb") as f:
        f.readline()
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b"\n":
            f.seek(-2, os.SEEK_CUR)
        last = f.readline()
    return last.decode('utf8').strip()

def get_last_row(filename):
    return json.loads(get_last_line(filename))

def get_all_rows(filename):
    with open(filename, 'r') as f:
        result = []
        for line in f.read().splitlines():
            result.append(json.loads(line))
        return result

class Entry:
    def __init__(self, id, timestamp, fields):
        self.id = id
        self.timestamp = timestamp
        self.fields = fields

    @staticmethod
    def from_dict(d):
        d = copy.deepcopy(d)

        timestamp = dateutil.parser.parse(d['timestamp'])
        del d['timestamp']

        id = d['id']
        del d['id']

        fields = d
        return Entry(id, timestamp, fields)

    @staticmethod
    def make(fields):
        id = gen_id()
        timestamp = datetime.datetime.utcnow()
        return Entry(id, timestamp, fields)

    def to_dict(self):
        d = copy.deepcopy(self.fields)
        d['timestamp'] = self.timestamp.isoformat()
        d['id'] = self.id
        return d

    def __repr__(self):
        s = 'Entry '
        s += self.timestamp.isoformat()
        s += ' '
        s += json.dumps(self.fields)
        return s

class LogFile:
    def __init__(self, filename):
        if not os.path.exists(filename):
            print(f'"{filename}" does not exist')
            sys.exit(1)
        self.filename = filename

    def add(self, entry):
        add_row(self.filename, entry.to_dict())

    def get_last(self):
        entry = Entry.from_dict(get_last_row(self.filename))
        return entry

    def get_all(self):
        entries = []
        for d in get_all_rows(self.filename):
            entry = Entry.from_dict(d)
            entries.append(entry)
        return entries


def foo():
    add_row('bla.json.lines', {'z': 6})


def bar():
    # return get_last_row('bla.json.lines')
    return get_all_rows('bla.json.lines')

def debug():
    f = LogFile('bla.json.lines-2')
    f.add_entry(Entry.make({'foo': 'bar'}))
    return f.get_all()

def parse_keyval(s):
    m = re.match(r'^([^=]+)=([^=])$', s)
    if m is None:
        print(f'"{s}" is not of format a=b')
        sys.exit(1)
    else:
        k, v = m.groups()
        return (k, v)


def main(args):
    '''
    Usage: logger [options] add <keyval>...

    --file <fn>  log file to use [default: logs.json.lines]
    '''
    keyvals = dict([parse_keyval(s) for s in args['<keyval>']])
    f = LogFile(args['--file'])
    entry = Entry.make(keyvals)
    f.add(entry)
    print(f'Added: {entry}')


if __name__ == '__main__':
    args = docopt.docopt(main.__doc__)
    main(args)
