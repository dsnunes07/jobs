import requests
import datetime

API_ENDPOINT = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'



def send_cv():
	cv = {
		'full_name': 'Daniel Silva Nunes',
		'email': 'dsnunes@usp.br',
		'mobile_phone': '+55 (11) 96181-8223',
		'age': 23,
		'home_address': 'Rua Deocleciana Serafina de Souza, 241',
		'start_date': int(datetime.datetime(2020,7,4).timestamp()),
		'opportunity_tag': 'dev_intern_2020',
		'past_jobs_experience': 'I worked as a development intern at Nexoos. We have developed many features to the company\'s platform using Ruby On Rails and PostgreSQL',
		'degrees': [{
			'institution_name': 'University of São Paulo',
			'degree_name': 'BSc. in Computer Science',
			'begin_date': int(datetime.datetime(2017,2,2).timestamp()),
			'end_date': int(datetime.datetime(2021,12,31).timestamp())
		}],
		'programming_skills': ['python', 'javascript', 'java', 'ruby on rails', 'c', 'julia', 'node'],
		'database_skills': ['mysql', 'postgresql'],
		'hobbies': ['running', 'music'],
		'why': 'I really like programming and I am very excited to apply my knowledge in a professional way.',
		'git_url_repositories': 'https://github.com/dsnunes07'
	}

	response = requests.post(API_ENDPOINT,
													json=cv)
	print(response.status_code)
	print(response.json())
	

if __name__ == '__main__':
	send_cv()
