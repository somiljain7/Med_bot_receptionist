from qdrant_client import models,QdrantClient
import numpy
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


documents = [
    {"name": "Unconscious",
     "remedy": """If someone is unconscious or unresponsive, follow the ABC principle: Airway, Breathing, and Circulation. 
               1. Airway: Open their airway if they are not breathing. 
               2. Breathing: If the airway is clear but the person is still not breathing, provide rescue breathing.
               3. Circulation: Perform chest compressions to maintain blood circulation while doing rescue breathing. 
               If the person is unresponsive, check their pulse. Begin CPR by pushing against the chest and blowing air into their mouth in a constant rhythm. If their heart has stopped, continue chest compressions."""},
    
    {"name": "Cardiac Arrest",
     "remedy": "Perform CPR (Cardiopulmonary Resuscitation) and use an AED (Automated External Defibrillator) if available. Call emergency services immediately."},

    {"name": "Severe Bleeding",
     "remedy": "Apply direct pressure to the wound using a clean cloth or bandage. Elevate the injured area if possible. Seek immediate medical attention."},

    {"name": "Choking",
     "remedy": "Perform the Heimlich maneuver to dislodge the object blocking the airway."},

    {"name": "Stroke",
     "remedy": "Use the FAST acronym to recognize symptoms: Face drooping, Arm weakness, Speech difficulty, and Time to call emergency services. Seek immediate medical help."},

    {"name": "Severe Allergic Reaction (Anaphylaxis)",
     "remedy": "Administer an epinephrine auto-injector (EpiPen) if available and call emergency services."},

    {"name": "Broken Bones",
     "remedy": "Immobilize the affected area, apply a cold pack to reduce swelling, and seek medical attention."},

    {"name": "Ingestion of Poison",
     "remedy": "Call poison control or emergency services immediately. Do not induce vomiting unless instructed by a professional."},

    {"name": "Carbon Monoxide Poisoning",
     "remedy": "Move the person to fresh air immediately, call emergency services, and administer oxygen if trained to do so."}
]

def vector_database_init():
    # initializing Qdrant client at port 6333
    qdrant = QdrantClient(
        host='localhost',
        port=6333
    )
    return qdrant

def vector_database_gen(qdrant,encoder,documents):
    # Generating a Vector database 
    #args:
    #qdrant: object of QdrantClient
    #encoder:  encoder for semantic similarity
    #documents: a list of json objects stored as records

    qdrant.recreate_collection(
        collection_name='Clinical',
        vectors_config=models.VectorParams(
            size=encoder.get_sentence_embedding_dimension(),
            distance=models.Distance.COSINE
        )
    )
    records=[]

    for idx, doc in enumerate(documents):
        record = models.Record(
            id=idx,
            vector=encoder.encode(doc['remedy']).tolist(),
            payload=doc
        )
        records.append(record)

    qdrant.upload_records(
        collection_name='Clinical',
        records=records
    )


def vector_search(qdrant,encoder,x):
    # Search within a Vector database 
    #args:
    #qdrant: object of QdrantClient
    #encoder:  encoder for semantic similarity
    #x: sentence for calculating semantic similarity with records 
    hits = qdrant.search(
        collection_name='Clinical',
        query_vector=encoder.encode(x).tolist(),
        limit=1
    )
    for hit in hits:
        return (hit.payload)#,'score:',hit.score)


def process(symptoms):
    # Generating the Output of vector search
    print("\nProcessing the emergency report...")
    time.sleep(15)  # Simulate processing time
    encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    qdrant=vector_database_init()
    llm_output = f"The analysis indicates a possible condition based on the symptoms: {vector_search(qdrant,encoder,symptoms)}"
    return llm_output


#qdrant=vector_database_init()
#encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
#vector_database_gen(qdrant,encoder,documents)