"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    with(neo_csv_path, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        neos = []
        for l in csv_reader:
            l["name"] = l["name"] or None
            l["diameter"] = float(l["diameter"]) if l["diameter"] else None
            l["pha"] = False if l["pha"] in ["", "N"] else True
            try:
                neo = NearEarthObject(
                    designation = l["pdes"],
                    name = l["name"],
                    diameter = l["diameter"],
                    hazardous = l["pha"],
                )
            except Exception as e:
                print("Exception is,", e)
            else:
                neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    with open(cad_json_path, "r") as csvfile:
        csv_reader = json.load(csvfile)
        csv_reader = [dict(zip(csv_reader["fields"], data)) for data in csv_reader["data"]]
        approaches = []
        for l in csv_reader:
            try:
                approach = CloseApproach(
                    designation=l["des"],
                    time=l["cd"],
                    distance=float(l["dist"]),
                    velocity=float(l["v_rel"]),
                )
            except Exception as e:
                print("Exception is,", e)
            else:
                approaches.append(approach)
    return approaches

