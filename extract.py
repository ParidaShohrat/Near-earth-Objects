
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []

    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            designation = row['pdes']
            name = row['name'] if row['name'] else None
            diameter = float(row['diameter']) if row['diameter'] else float('nan')
            hazardous = row['pha']

            neos.append(NearEarthObject(designation=designation,
                                         name=name,
                                         diameter=diameter,
                                         hazardous=hazardous))

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []

    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)
        for entry in contents['data']:
            designation = entry[0]
            time = entry[3]
            distance = float(entry[4])
            velocity = float(entry[7])

            approaches.append(CloseApproach(
                designation=designation,
                time=time,
                distance=distance,
                velocity=velocity
            ))  

    return approaches
