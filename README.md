
#Test Umich API OAuth using Python


Tested with Python 3.6

Follow the instructions to generate your `client_id` and `secret` for an application ID at [https://api.it.umich.edu/]

#To run without docker


 * Install Python 3.6
 * `pip install -r requirements.txt`
 * Update Secret and client ids from Umich API Gateway
 * `python oauthtest.py`


#To Run with docker (recomended)

Update `client_id` and `secret` from the UMICH API directory

	docker build -t api-python umich-api-python
	
	#run onetime and exit
	docker run api-python
	
	#start with bash shell and run manually
