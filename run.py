import os
import argparse
from bri import import_data

#from mpadi import build_medians_collection

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dataDir',
    type=str, default='data',
    help='The json data dump directory path.')

args = parser.parse_args()
json_dir_path = args.dataDir


# Run the app
if __name__ == '__main__':
    result_dict = {}

    if os.path.isdir(json_dir_path):
        for filename in os.listdir(json_dir_path):
            if(filename.endswith(".json")):

                json_filepath = json_dir_path + '/' + filename

                print "\n\nImporting business registration data '%s':\n" % json_filepath
                import_data(json_filepath)

    print "\n\nIMPORT SUMMARY:"
    for key in result_dict.keys():
        print "Total imported businesses: %i" % 10

    print  # Just skip line
