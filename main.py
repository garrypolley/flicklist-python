import webapp2
import random

class Index(webapp2.RequestHandler):

    def get_random_movie(self):

        movies = [
            "The Big Lebowski",
            "Lord of the Rings: Two Towers",
            "The Hobbit",
            "Aladdin",
            "Star Wars"
        ]

        random_movie_index = random.randrange(len(movies))

        return movies[random_movie_index]

    def get(self):
        movie = self.get_random_movie()

        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        tomorrow_movie = self.get_random_movie()
        content += "<h1>Tomrrow's moview</h1>"
        content += "<p>" + tomorrow_movie + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
