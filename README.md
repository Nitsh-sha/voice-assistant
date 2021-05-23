# voice-assistant
voice assistant based on Python language that protects your privacy

Connection: Connect with VoiceIt.io API for a wake word and identity verification via voice verification. 

Database: MongoDB cloud

Encryption: 
Due to budget constraint, we used free version of MongoDB cloud which does not support automatic encryption. To work around this, we encrypt the data via the client side first before storing in MongoDB cloud. However free version of MongoDB will automatically decrypt the data.
None encrypted data goes through ‘NormalConnection.py’ and then store in MongoDB cloud without encryption.
Encrypted data goes through ‘SecureConnection.py’. The data gets encrypted and store in MongoDB cloud with encryption.

Voice assistant functions:
Due to time and skills constraints, we created noncomplex functions for this artefact to show how these can be connected and use with some of data categorizations mentioned in the research findings section.
Ask for time function: we generate time result without storing any data.
Ask for date function: we generate time result without storing any data.
Sending email function: all data are encrypted and stored except for the timestamp and subject line (so these can be used to fetch the data).
Sending message function: All data including the contact number and message are encrypted. The name is not encrypted so we can fetch the data by name.
Search Wikipedia function: Search history data is stored without encryption and only stored for 30 days and will be automatically deleted. We can fetch data of the most recent search.
Search Google function: Search history data is stored without encryption and only stored for 30 days and will be automatically deleted. We can fetch data of the most recent search.
Search YouTube function: Search history data is stored without encryption and only stored for 30 days and will be automatically deleted. We can fetch data of the most recent search. We can also fetch favourites (most frequently searched).
Ask for weather function: Location data (city) stored is encrypted, weather data stored not encrypted. Data will be deleted in 30 days. We can fetch most recent weather data.
Ask for news function: No data is stored.
Ask the assistant to read a highlighted section of text function: No data is stored.
Ask Covid update function: No data is stored.
Request a joke function: No data is stored.
Screenshot function: No data is stored.
Take notes function: We store title (not encrypted), note content (encrypted), mark as todo? (not encrypted)
Do to list function: Retrieving any notes marked as todo.
Password generator function: No data is stored.
