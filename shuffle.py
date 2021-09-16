import csv
import cchardet
from pathlib import Path, PurePosixPath
from sklearn.utils import shuffle


def read_data(file_name):

    file_path = Path.joinpath(PurePosixPath('../data'), file_name)
    print(file_path)

    f = open(file_path, 'rb')
    encoding = cchardet.detect(f.read())['encoding']
    file = open(file_path, newline='', encoding=encoding)
    reader = csv.DictReader(file, delimiter=',')

    contents = []
    labels = []
    for index, row in enumerate(reader):
        label = int(row.get('label'))
        content = row.get('content')
        contents.append(content)
        labels.append(label)

    contents, labels = shuffle(contents, labels, random_state=0)
    return contents, labels
