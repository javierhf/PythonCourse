# DATA STRUCTURES

# MOVIE DATA STRUCTURE
movies = [
    { 'Title': 'Alien',
            'Genre': 'Science-fiction',
            'Director': 'Ridley Scott',
            'Year': '1979'
    },
    { 'Title': 'Con la espada en la lona',
                'Genre': 'Comedy',
                'Director': 'Keith Merrill',
                'Year': '1979'
        },
    { 'Title': '2001: Space Odissey',
                'Genre': 'Science fiction',
                'Director': 'Stanley Kubric',
                'Year': '1968'
        },
    { 'Title': 'Cantinflas',
                'Genre': 'Animation',
                'Director': 'Don Messick',
                'Year': '1979'
        },
    { 'Title': 'E.T',
                'Genre': 'Science fiction',
                'Director': 'Steven Spielberg',
                'Year': '1982'
        },
    { 'Title': 'Jaws',
                'Genre': 'Adventure',
                'Director': 'Steven Spielberg',
                'Year': '1975'
        },
    { 'Title': 'Star Wars',
                'Genre': 'Science fiction',
                'Director': 'George Lucas',
                'Year': '1975'
        },
    { 'Title': 'See no evil, Hear no evil',
                'Genre': 'Comedy',
                'Director': 'Arthur Hiller',
                'Year': '1989'
        },
    { 'Title': 'Elephant man',
                'Genre': 'Mistery',
                'Director': 'David Lynch',
                'Year': '1980'
        },
    { 'Title': 'Los inmortales',
                'Genre': 'Action',
                'Director': 'Russell Mulcahy',
                'Year': '1986'
        },
    { 'Title': 'Kamikaze',
                'Genre': 'War',
                'Director': 'Luc Besson',
                'Year': '1983'
        },
    { 'Title': 'Amanece que no es poco',
                'Genre': 'Comedy',
                'Director': 'José Luis Cuerda',
                'Year': '1989'
        },
    {'Title': 'Amadeus',
     'Genre': 'History',
     'Director': 'Milos Forman',
     'Year': '1984'
     },
]

# MENU DATA STRUCTURE

user_options = {
    '1': byTitle,
    '2': byGenre,
    '3': byDirector,
    '4': byYear,
    '5': add_Film,
    '6': show_All
}
# FUNCTIONS DEFINITION


def use_app(prompt):
    while prompt != 'n':
        print('''
            SEARCH MOVIES BY:
            1.- Title
            2.- Genre
            3.- Director
            4.- Year \n
            MOVIES OPTIONS:
            5.- Add a new film.
            6.- Show all films.
            ''')
        menu = int(input('Enter menu option: '))
        user_menu(menu)
        prompt = input('Run MovieApp? (y/n) \n')


def print_result(ptitle, pgenre, pano, pdirector):
    print(f'{ptitle} is a {pgenre} released in {pano} and directed by {pdirector} \n')


def user_menu(selection):
    if selection in user_options:
        selected_function = user_options[selection]
        selected_function(selection)
    else:
        print('Wrong option!')
        '''
    if m == 1:
        film_title = input('Enter film title: ')
        byTitle(film_title)
    elif m == 2:
        film_genre = input('Enter film genre: ')
        byGenre(film_genre)
    elif m == 3:
        film_director = input('Enter film director: ')
        byDirector(film_director)
    elif m == 4:
        film_year = input('Enter released year: ')
        byYear(film_year)
    elif m == 5:
        add_Film()
    elif m == 6:
        show_All()
    else:
        print(' ')
        print('Wrong option!')

 '''


def byTitle(f):
# SEARCH ENTERED FILM IN OUR DATE BASE
    not_found_film = True
    while not_found_film:
        for pelis in movies:
            if f in pelis['Title']:
                titulo = pelis['Title']
                genero = pelis['Genre']
                director = pelis['Director']
                ano = pelis['Year']
                print(' ')
                print_result(titulo, genero, director, ano)
                #print(f'{titulo} is a {genero} released in {ano} and directed by {director}')
                not_found_film = False
            elif f not in pelis['Title']:
                continue

        if not_found_film:
            print(f'{f} is not in our database... yet')
        break


def byGenre(g):
    # SEARCH ENTERED GENRE IN OUR DATE BASE
    not_found_film = True
    while not_found_film:
        for pelis in movies:
            if g in pelis['Genre']:
                titulo = pelis['Title']
                genero = pelis['Genre']
                director = pelis['Director']
                ano = pelis['Year']
                print(' ')
                print_result(titulo, genero, director, ano)
                #print(f'{titulo} is a {genero} released in {ano} and directed by {director}')
                not_found_film = False
            elif g not in pelis['Genre']:
                continue

        if not_found_film:
            print(f'{g} is not in our database... yet')
        break


def byDirector(d):
    # SEARCH ENTERED DIRECTOR IN OUR DATE BASE
    not_found_film = True
    while not_found_film:
        for pelis in movies:
            if d in pelis['Director']:
                titulo = pelis['Title']
                genero = pelis['Genre']
                director = pelis['Director']
                ano = pelis['Year']
                print(' ')
                print_result(titulo, genero, director, ano)
                #print(f'{titulo} is a {genero} released in {ano} and directed by {director}')
                not_found_film = False
            elif d not in pelis['Title']:
                continue

        if not_found_film:
            print(f'{d} is not in our database... yet')
        break


def byYear(y):
    # SEARCH ENTERED YEAR IN OUR DATE BASE

    not_found_film = True
    while not_found_film:
        for pelis in movies:
            if y in pelis['Year']:
                titulo = pelis['Title']
                genero = pelis['Genre']
                director = pelis['Director']
                ano = pelis['Year']
                print(' ')
                print_result(titulo, genero, director, ano)
                #print(f'{titulo} is a {genero} released in {ano} and directed by {director}')
                not_found_film = False
            elif y not in pelis['Year']:
                continue

        if not_found_film:
            print(f'{y} is not in our database... yet')
        break


def add_Film():
    add_answer = 'y'
    while add_answer == 'y':
       add_title = input('Film title: ')
       add_genre = input('Genre: ')
       add_director = input('Film director: ')
       add_year = input('Year of release: ')
       movies.append({'Title': add_title, 'Genre': add_genre, 'Director': add_director, 'Year': add_year})
       print(f'New film added:\n Title: {add_title} \n Genre: {add_genre} \n Year: {add_year} \n Director: {add_director} \n')
       add_answer = input('Continue adding films (y/n)?: ')


def show_All():

    for pelis in movies:
        titulo = pelis['Title']
        genero = pelis['Genre']
        director = pelis['Director']
        ano = pelis['Year']
        print(' ')
        print_result(titulo, genero, director, ano)
        #print(f'{titulo} \n Genre: {genero} \n Year: {ano} \n Director: {director} \n')


# APP INPUT
# BODY PROGRAMM

menu_prompt = input('''
********************************************************************

                           MOVIEAPP, Inc

********************************************************************
\n
OPEN MOVIEAPP? (y/n) \n
''')
use_app(menu_prompt)



