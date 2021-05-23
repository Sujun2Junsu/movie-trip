import requests, json
from .models import Movie
from django.http import HttpResponse

def create_movies(request):

    results = []
   
    ### popular 40 ###
    # data 받아오기
    my_url = 'https://api.themoviedb.org/3/movie/popular?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR'
    response = requests.get(my_url)
    movie_dict = response.json()

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = 'https://image.tmdb.org/t/p/w500' + movie.get('poster_path')
        popularity = movie.get('popularity')

        # DB에 저장하기, 중복제거
        (movie, created) = Movie.objects.get_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)

        result = {
            'model': "movies.movie",
            # 'pk': len(results) + 1,
            "fields": {
            'poster_path': poster_path,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'popularity': popularity
        }}
        if result not in results:
            results.append(result)

    # data 받아오기
    my_url = 'https://api.themoviedb.org/3/movie/popular?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR&page=2'
    response = requests.get(my_url)
    movie_dict = response.json()

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = 'https://image.tmdb.org/t/p/w500' + movie.get('poster_path')
        popularity = movie.get('popularity')

        # DB에 저장하기, 중복제거
        (movie, created) = Movie.objects.get_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)

        result = {
            'model': "movies.movie",
            # 'pk': len(results) + 1,
            "fields": {
            'poster_path': poster_path,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'popularity': popularity
        }}
        if result not in results:
            results.append(result)

    ### now_playing 40 ###
    # data 받아오기
    my_url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR'
    response = requests.get(my_url)
    movie_dict = response.json()

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = 'https://image.tmdb.org/t/p/w500' + movie.get('poster_path')
        popularity = movie.get('popularity')

        # DB에 저장하기, 중복제거
        (movie, created) = Movie.objects.get_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)

        result = {
            'model': "movies.movie",
            # 'pk': len(results) + 1,
            "fields": {
            'poster_path': poster_path,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'popularity': popularity
        }}
        if result not in results:
            results.append(result)
    
    # data 받아오기
    my_url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR&page=2'
    response = requests.get(my_url)
    movie_dict = response.json()

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = 'https://image.tmdb.org/t/p/w500' + movie.get('poster_path')
        popularity = movie.get('popularity')

        # DB에 저장하기, 중복제거
        (movie, created) = Movie.objects.get_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)

        result = {
            'model': "movies.movie",
            # 'pk': len(results) + 1,
            "fields": {
            'poster_path': poster_path,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'popularity': popularity
        }}
        if result not in results:
            results.append(result)

    ### top_rated 40 ###
    # data 받아오기
    my_url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR'
    response = requests.get(my_url)
    movie_dict = response.json()

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = 'https://image.tmdb.org/t/p/w500' +  movie.get('poster_path')
        popularity = movie.get('popularity')

        # DB에 저장하기, 중복제거
        (movie, created) = Movie.objects.update_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)
        
        result = {
            'model': "movies.movie",
            # 'pk': len(results) + 1,
            "fields": {
            'poster_path': poster_path,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'popularity': popularity
        }}
        if result not in results:
            results.append(result)

    # data 받아오기
    my_url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=4dc86c92c350c5edac0c712116558e11&language=ko-KR&page=2'
    response = requests.get(my_url)
    movie_dict = response.json()

    # 필요한 정보 골라내기
    movie_list = movie_dict.get('results')
    for movie in movie_list:
        title = movie.get('title')
        overview = movie.get('overview')
        release_date = movie.get('release_date')
        poster_path = 'https://image.tmdb.org/t/p/w500' + movie.get('poster_path')
        popularity = movie.get('popularity')

        # DB에 저장하기, 중복제거
        (movie, created) = Movie.objects.update_or_create(title=title, overview=overview, release_date=release_date, poster_path=poster_path, popularity=popularity)
        
        result = {
            'model': "movies.movie",
            # 'pk': len(results) + 1,
            "fields": {
            'poster_path': poster_path,
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'popularity': popularity
        }}
        if result not in results:
            results.append(result)
    
    print(len(results))

    with open('movies/fixtures/movies/movies.json', "w", encoding='utf-8') as f: # movies.json은 저장될 json 파일 명입니다., json_data은 저장할 데이터입니다.
        json.dump(results, f, ensure_ascii=False)

    return HttpResponse(status=200)
