#Seatwork 2
from pyscript import display, document

def member_checker (e):
    members = ['Nathan Bautista', 'Hans Baquiran', 'Chester Roxas','Joel Gonzales', 'Isabelle Cabatu', 'Joseph Co','Ezek Bacay', 'Franco Maglaqui','Josua Ortiz']

    fname = document.getElementById('firstname').value.strip().title()
    lname = document.getElementById('lastname').value.strip().title()
    participant = fname + ' ' + lname
    member_checker = participant in members

    display_message = (f'Sorry {participant}, your name is not on the list.', f'Congratulations {participant}! You are now part of the COCC club.') 

    document.getElementById('result').innerHTML = display_message[member_checker]
