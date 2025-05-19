############################################################
# Transcription tool found at https://www.assemblyai.com/ 
# sign up for free API key
############################################################

############################################################
# last file update- 2025/05/19
############################################################

import csv
import assemblyai as aai 

aai.settings.api_key = "your key goes here"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe("analysis/mp3/John Denver - Take Me Home.MP3") #change this to your file path for transcrition

print(transcript.text)    #print to your terminal

# Save the transcription to a CSV file
with open('analysis/csv transcript/Denver_countryRoad.csv', 'w', newline='', encoding='utf-8') as csvfile: #update to your file pathway
    writer = csv.writer(csvfile)
    # Write the transcript text as a single row
    writer.writerow([transcript.text])