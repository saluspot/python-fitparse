from fitparse import FitFile

name = 'testfile.FIT'

fitfile = FitFile(name)
fitfile.parse()

records = list(fitfile.get_messages())

for r in records:
    print('==> {}'.format(r))
    for k, v in r.get_values().items():
        print('  {} = {}'.format(k, v))
