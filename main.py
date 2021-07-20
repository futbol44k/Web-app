from flask import Flask, render_template, request
from Mini import FindAnime, review
import pandas as pd


app = Flask(__name__)
simp = FindAnime.from_csv_path("anime_db.csv")
charac = FindAnime.from_csv_path("second_anime_db.csv")


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/data', methods = ['POST', "GET"])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        data = request.form
        char_data, anime_data =  charac.rand_char(simp, data['Year'], data['Genres'], data['Anime'])
        title = anime_data['name'].iloc(0)[0]
        k = review(title)
        if 'No such anime' == title:
            form_data = {
                "anime_name": title,
                "random_char": char_data['character'].iloc(0)[0],
                "char_pic": "https://you-anime.ru/anime-images/characters/PkH8DIgPyEQOiQK7.jpg",
            }
        elif char_data['character'].iloc(0)[0] == "There is no matching characters in data":
            form_data = {
                "anime_name": title,
                "anime_url": anime_data['url'].iloc(0)[0],
                "random_char": char_data['character'].iloc(0)[0],
                "char_pic": "https://you-anime.ru/anime-images/characters/PkH8DIgPyEQOiQK7.jpg",
                "video": f"https://www.youtube.com/embed/{k}"
            }
        else:
            form_data = {
                "anime_name": anime_data['name'].iloc(0)[0],
                "anime_url": anime_data['url'].iloc(0)[0],
                "random_char": char_data['character'].iloc(0)[0],
                "char_pic": char_data['pictures'].iloc(0)[0],
                "video": f"https://www.youtube.com/embed/{k}"
            }
    return render_template('data.html', form_data=form_data)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
