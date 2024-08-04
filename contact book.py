contacts = []


def addcontact():
  contact = input(" enter a contact: ")
  contacts.append(contact)
  print(f"contact '{contact}' added.")


def listcontacts():
  if not contacts:
    print("There are no contacts.")
  else:
    print("Current contacts:")
    for index, contact in (contacts):
      print(f"contact #{index}.{contact}")


def deletecontact():
  listcontacts()
  try:
    contactToDelete = int(input("Enter the # to delete: "))
    if contactToDelete >= 0 and contactToDelete < len(contacts):
      contacts.pop(contactToDelete)
      print(f"contact {contactToDelete} has been removed.")
    else:
      print(f"contact #{contactToDelete} was not found.")
  except:
    print("Invalid input.")


if __name__ == "__main__":
  
  print("Welcome!)")
  while True:
    print("\n")
    print("Please select")
    print("____________________")
    print("1. Add a new contct")
    print("2. Delete a contact")
    print("3. List contacts")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      addcontact()
    elif (choice == "2"):
      deletecontact()
    elif (choice == "3"):
      listcontacts()
    elif (choice == "4"):
      break
    else:
      print("Invalid value.")

  print("Goodbye")