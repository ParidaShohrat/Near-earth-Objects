
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for approach in results:
            neo = approach.neo
            writer.writerow({
                'datetime_utc': approach.timestr,
                'distance_au': approach.distance,
                'velocity_km_s': approach.velocity,
                'designation': neo.designation if neo else '',
                'name': neo.name if neo.name else '',
                'diameter_km': neo.diameter if neo.diameter else float('nan'),
                'potentially_hazardous': neo.hazardous if not neo.hazardous else False
            })



def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    output_data = []

    for approach in results:
        
        approach_dict = {
            'datetime_utc': approach.time_str,
            'distance_au': approach.distance,
            'velocity_km_s': approach.velocity,
            'neo': {
                'designation': approach.neo.designation if approach.neo else '',
                'name': approach.neo.name if approach.neo else '',
                'diameter_km': approach.neo.diameter if approach.neo else float('nan'),
                'potentially_hazardous': approach.neo.hazardous if approach.neo else False
            }
        }
        output_data.append(approach_dict)

    with open(filename, 'w') as jsonfile:
        json.dump(output_data, jsonfile, indent=2)
