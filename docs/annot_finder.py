import json
from load_dataset import TimeSeries


def annot_finder(dfile, annots_file):
    annots = json.load(open(annots_file))
    ts = TimeSeries.from_json(dfile)
    return annots[ts.name]
