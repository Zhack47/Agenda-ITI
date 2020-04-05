import csv


def save_user(filename, prenom, nom):
    with open(filename, 'r+') as csvfile:
#        reader = csv.DictReader(csvfile)
 #       results = []
  #      for row in reader:
   #         results.append(row)
    #    for i in range(len(results)):
     #       if results[i]['firstfieldnames_name'] == prenom and results[i]['first_name'] == nom:
      #          return 'user already registered'
       #     else:
        #        pass
        writer = csv.DictWriter(csvfile, fieldnames=['first_name','last_name'])
        # writer.writeheader()
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
