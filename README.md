# What functionalities should the app provide
1. Given an url, the app should return a shorter url
    1. The user can select a special short character sequence
2. Given a short url, the user should be redirected to the original url
3. Delete a stored short url

# How to Run

1. **pip install -r requirements.txt**
2. **python manage.py makemigrations**
3. **python manage.py migrate**

# What does the app do?
As of now, the app has two rest endpoints:
1. **POST** /create-short-url 
```
{
	"original_url": <url>
}
```
2. **GET** /<short-code> 