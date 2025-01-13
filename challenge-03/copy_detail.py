import json
import csv
import argparse

def update_json(env, json_file, csv_file):
    # Read CSV file
    with open(csv_file, mode='r') as infile:
        reader = csv.DictReader(infile)
        data = {rows['ENV']: rows for rows in reader}
        # print(data)
    
    # Read JSON file
    with open(json_file, 'r') as infile:
        config = json.load(infile)
        # print(config)
    
    # Update JSON data
    if env in config and env in data:
        config[env]['host'] = data[env]['host']
        config[env]['port'] = int(data[env]['port'])
        config[env]['dbname'] = data[env]['dbname']
        config[env]['user'] = data[env]['user']
        config[env]['password'] = data[env]['password']
    else:
        print ("Environment '{}' not found in JSON or CSV file.".format(env))
        return
    
    # Write updated JSON back to file
    with open(json_file, 'w') as outfile:
        json.dump(config, outfile, indent=4)

    print ("Configuration for '{}' updated successfully.".format(env))

if __name__ == "__main__":
    
    # env = raw_input("Enter the environment to update (e.g., DEV, PROD): ")
    # json_file = raw_input("Enter the path to the JSON config file: ")
    # csv_file = raw_input("Enter the path to the CSV input file: ")

    # update_json(env, json_file, csv_file)
    parser = argparse.ArgumentParser(description='Update JSON config based on CSV input.')
    parser.add_argument('--env', required=True, help='Environment to update (e.g., DEV, PROD)')
    parser.add_argument('--json', required=True, help='Path to JSON config file')
    parser.add_argument('--csv', required=True, help='Path to CSV input file')
    
    args = parser.parse_args()
    update_json(args.env, args.json, args.csv)
