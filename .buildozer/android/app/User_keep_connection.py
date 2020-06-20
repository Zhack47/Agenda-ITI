import csv


def save_user(filename, prenom, nom):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['first_name', 'last_name'])
        writer.writerow({'first_name': prenom, 'last_name': nom})
        return 'user added'


def load_usernames(filename):
    with open(filename, 'r') as csvfile:
        fieldnames = ['first_name', 'last_name']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        results = []
        for row in reader:
            results.append(row)
    return results
