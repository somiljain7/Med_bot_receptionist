## Receptionist Bot assisting a Doctor 
<p align="center"><img src="assets/CHAT.png" alt="Illustration of pipeline." width="500"/></p>

### INSTRUCTIONS FOR INFERENCING
```
- pip install -r requirements.txt
- docker run -p 6333:6333 qdrant/qdrant
```
<p align="center"><img src="assets/vector_database.png" alt="Illustration of Vector Database" width="500"/></p>

```
- Generate vector database for semantic search
- python vector_database.py

```

### Encoders available
<p align="center"><img src="assets/encoders_medical.png" alt="different encoders available for semantic search" width="500"/></p>

```
- Run all cells in jupyter notebook 'E2E.ipynb'
```

### OUTPUT SAMPLE ####
```
Hello! My name is RIYA and i work as a receptionist for Dr. Adrin. How can I help you today?

RIYA : Please  Send a message or Report an emergency

RIYA : You selected 'Report an emergency'.
User: I am not able to breathe properly dealing with chest pain

Processing the emergency report...
RIYA : Please hold just a sec
User: Indore MP India
RIYA : Location 'Indore MP India' received.  Dr. Adrin will be coming to their location immediately. ETA:00:23:44

RIYA :  Processing complete. Here is the analysis from our system:
The analysis indicates a possible condition based on the symptoms: ({'name': 'Unconscious', 'remedy': 'If someone is unconscious or unresponsive, follow the ABC principle: Airway, Breathing, and Circulation. \n               1. Airway: Open their airway if they are not breathing. \n               2. Breathing: If the airway is clear but the person is still not breathing, provide rescue breathing.\n               3. Circulation: Perform chest compressions to maintain blood circulation while doing rescue breathing. \n               If the person is unresponsive, check their pulse. Begin CPR by pushing against the chest and blowing air into their mouth in a constant rhythm. If their heart has stopped, continue chest compressions.'}, 'score:', 0.4441438)
User: it says 23 min , it will too late for his arrival
RIYA : I understand that you are worried that Dr. Adrin will arrive too late, meanwhile we would suggest that you follow following remedy:The analysis indicates a possible condition based on the symptoms: ({'name': 'Unconscious', 'remedy': 'If someone is unconscious or unresponsive, follow the ABC principle: Airway, Breathing, and Circulation. \n               1. Airway: Open their airway if they are not breathing. \n               2. Breathing: If the airway is clear but the person is still not breathing, provide rescue breathing.\n               3. Circulation: Perform chest compressions to maintain blood circulation while doing rescue breathing. \n               If the person is unresponsive, check their pulse. Begin CPR by pushing against the chest and blowing air into their mouth in a constant rhythm. If their heart has stopped, continue chest compressions.'}, 'score:', 0.4441438) 


RIYA : Thank you for using the service. Stay safe!
```
