import csv


def save_user(filename, prenom, nom):
    with open(filename, 'w') as file:

        results = []
        for row in reader:
            results.append(row)
        for i in range(len(results)):
            if results[i]['first_name'] == prenom and results[i]['first_name'] == nom:
                return 'user already registered'
            else:
                pass
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': prenom, 'last_name': nom})
        return 'user added'

def load_usernames(filename):
    with open(filename, 'w') as csvfile:
        fieldnames = ['first_name', 'last_name']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        results = []
        for row in reader:
            results.append(row)
    return results
