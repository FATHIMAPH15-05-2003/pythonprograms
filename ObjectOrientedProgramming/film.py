class movie:
    title:str
    rating:int
    run_time:int
    director:str
    genre:str

    def set_movie(self,title,rating,run_time,director,genre):
        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.director=director
        self.genre=genre

    def display_movie(self):
        print(self.title,self.rating,self.run_time,self.director,self.genre)

movie_instance1=movie()
movie_instance2=movie()
movie_instance2.set_movie("ARM",4,2,"vishwanath","action") 
movie_instance2.display_movie()       
