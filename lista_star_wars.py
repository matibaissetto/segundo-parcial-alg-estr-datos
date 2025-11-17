grafo_star_wars = [
    # (Personaje1, Personaje2, episodios_juntos)
    ("Luke Skywalker", "Leia", 9),
    ("Luke Skywalker", "Han Solo", 6),
    ("Luke Skywalker", "Chewbacca", 6),
    ("Luke Skywalker", "C-3PO", 9),
    ("Luke Skywalker", "R2-D2", 9),
    ("Luke Skywalker", "Yoda", 5),
    ("Luke Skywalker", "Darth Vader", 6),
    ("Luke Skywalker", "Obi-Wan Kenobi", 4),
    
    ("Leia", "Han Solo", 7),
    ("Leia", "Chewbacca", 7),
    ("Leia", "C-3PO", 9),
    ("Leia", "R2-D2", 9),
    ("Leia", "Darth Vader", 5),
    ("Leia", "Lando Calrissian", 4),
    ("Leia", "Rey", 2),
    ("Leia", "Kylo Ren", 2),
    
    ("Han Solo", "Chewbacca", 8),
    ("Han Solo", "C-3PO", 5),
    ("Han Solo", "R2-D2", 5),
    ("Han Solo", "Lando Calrissian", 4),
    ("Han Solo", "Boba Fett", 2),
    ("Han Solo", "Rey", 2),
    ("Han Solo", "Kylo Ren", 2),
    
    ("Darth Vader", "Obi-Wan Kenobi", 3),
    ("Darth Vader", "Emperor Palpatine", 5),
    ("Darth Vader", "Boba Fett", 3),
    ("Darth Vader", "Yoda", 4),
    
    ("Yoda", "Obi-Wan Kenobi", 4),
    ("Yoda", "Emperor Palpatine", 3),
    
    ("C-3PO", "R2-D2", 9),
    ("C-3PO", "Chewbacca", 5),
    ("C-3PO", "BB-8", 2),
    
    ("R2-D2", "BB-8", 2),
    
    ("Rey", "Kylo Ren", 4),
    ("Rey", "BB-8", 4),
    ("Rey", "Finn", 3),
    ("Rey", "Poe Dameron", 3),
    
    ("Kylo Ren", "Han Solo", 2),
    
    ("Boba Fett", "Jabba the Hutt", 2),
    
    ("Chewbacca", "C-3PO", 5),
    ("Chewbacca", "R2-D2", 5)
]

# Información individual de cada personaje
personajes_detalle = [
    {"nombre": "Luke Skywalker", "episodios": [1, 2, 3, 4, 5, 6, 7, 8, 9], "total_episodios": 9},
    {"nombre": "Leia", "episodios": [1, 2, 3, 4, 5, 6, 7, 8, 9], "total_episodios": 9},
    {"nombre": "C-3PO", "episodios": [1, 2, 3, 4, 5, 6, 7, 8, 9], "total_episodios": 9},
    {"nombre": "R2-D2", "episodios": [1, 2, 3, 4, 5, 6, 7, 8, 9], "total_episodios": 9},
    {"nombre": "Chewbacca", "episodios": [3, 4, 5, 6, 7, 8, 9], "total_episodios": 7},
    {"nombre": "Han Solo", "episodios": [4, 5, 6, 7], "total_episodios": 4},
    {"nombre": "Darth Vader", "episodios": [1, 2, 3, 4, 5, 6], "total_episodios": 6},
    {"nombre": "Yoda", "episodios": [1, 2, 3, 5, 6, 8, 9], "total_episodios": 7},
    {"nombre": "Boba Fett", "episodios": [2, 3, 5, 6], "total_episodios": 4},
    {"nombre": "Rey", "episodios": [7, 8, 9], "total_episodios": 3},
    {"nombre": "Kylo Ren", "episodios": [7, 8, 9], "total_episodios": 3},
    {"nombre": "BB-8", "episodios": [7, 8, 9], "total_episodios": 3},
    {"nombre": "Obi-Wan Kenobi", "episodios": [1, 2, 3, 4, 5, 6], "total_episodios": 6},
    {"nombre": "Emperor Palpatine", "episodios": [1, 2, 3, 5, 6, 9], "total_episodios": 6},
    {"nombre": "Lando Calrissian", "episodios": [2, 3, 5, 6, 9], "total_episodios": 5},
    {"nombre": "Finn", "episodios": [7, 8, 9], "total_episodios": 3},
    {"nombre": "Poe Dameron", "episodios": [7, 8, 9], "total_episodios": 3},
    {"nombre": "Jabba the Hutt", "episodios": [1, 4, 6], "total_episodios": 3}
]