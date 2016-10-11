import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, 1)

def reducer(key, list_of_values):
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.excute(inputdata, mapper, reducer)
