import json
import os

profiles = {}

def load_profiles():
  global profiles
  if os.path.exists('profiles.json'):
    with open('profiles.json', 'r') as f:
      profiles = json.load(f)

def save_profiles():
  with open('profiles.json', 'w') as f:
    json.dump(profiles, f, indent=4)

def add_profile():
  id = input("Enter ID: ")
  name = input("Enter Name: ")
  sec = input("Enter sec: ")
  phno = input("Enter Phone Number: ")
  profiles[id] = {'name': name, 'sec': sec, 'phno': phno}
  save_profiles()
  print(f"'{name}' added successfully.\n")

def view_profiles():
  if not profiles:
    print("No profiles found.\n")
    return
  print("Details:")
  for id, info in profiles.items():
      print(f"ID: {id}, Name: {info['name']}, sec: {info['sec']}, phno: {info['phno']}")
  print()

def search_profile():
  id = input("Enter student ID to search: ")
  if id in profiles:
    print(f"Found: {profiles[id]}")
  else:
    print("profile not found.\n")
  print()

def remove_profile():
  id = input("Enter ID to remove: ")
  if id in profiles:
    del profiles[id]
    save_profiles()
    print(f"'{id}' removed successfully.\n")
  else:
    print("profile not found.\n")
  print()

def main():
  load_profiles()
  while True:
    print("MENU")
    print("1. Add profile")
    print("2. View profiles")
    print("3. Search profile by ID")
    print("4. Remove profile by ID")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      add_profile()
    elif choice == '2':
      view_profiles()
    elif choice == '3':
      search_profile()
    elif choice == '4':
      remove_profile()
    elif choice == '5':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.\n")

main()