#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

Names = []
with open('day24/Input/Names/invited_names.txt' , 'r') as d:
    for line in d.readlines():
        line = line.strip()
        Names.append(line)


with open ('day24/Input/Letters/starting_letter.txt','r') as f:
    Letter = f.read()

for i in Names:
    New_Letter = Letter.replace('[name]', i)
    with open(f'day24/Output/ReadyToSend/{i}.txt','w') as w:
        w.write(New_Letter)
