import sqlite3 as sq

# cities within 40-mile radius
cities = ('IRVINE', 'EAST IRVINE', 'FOOTHILL RANCH', 'LAKE FOREST', 'ALISO VIEJO', 'TUSTIN', 'LAGUNA WOODS', 'SANTA ANA', 'EL TORO', 'LAGUNA HILLS', 'MISSION VIEJO', 'NEWPORT COAST', 'RANCHO SANTA MARGARITA', 'TRABUCO CANYON', 'ORANGE', 'SILVERADO', 'NEWPORT BEACH', 'CORONA DEL MAR', 'COSTA MESA', 'LAGUNA BEACH', 'VILLA PARK', 'LAGUNA NIGUEL', 'LADERA RANCH', 'ANAHEIM', 'GARDEN GROVE', 'CORONA', 'FOUNTAIN VALLEY', 'SAN JUAN CAPISTRANO', 'HUNTINGTON BEACH', 'ATWOOD', 'YORBA LINDA', 'DANA POINT', 'MIDWAY CITY', 'PLACENTIA', 'WESTMINSTER', 'FULLERTON', 'CAPISTRANO BEACH', 'SAN CLEMENTE', 'STANTON', 'BREA', 'EASTVALE', 'CHINO HILLS', 'BUENA PARK', 'CHINO', 'NORCO', 'SUNSET BEACH', 'CYPRESS', 'LAKE ELSINORE', 'SEAL BEACH', 'LOS ALAMITOS', 'SURFSIDE', 'LA HABRA', 'LA PALMA', 'LA MIRADA', 'HAWAIIAN GARDENS', 'DIAMOND BAR', 'RIVERSIDE', 'LAKEWOOD', 'ROWLAND HEIGHTS', 'LONG BEACH', 'CERRITOS', 'WHITTIER', 'ARTESIA', 'WALNUT', 'MIRA LOMA', 'PERRIS', 'POMONA', 'ONTARIO', 'SANTA FE SPRINGS', 'NORWALK', 'WEST COVINA', 'BELLFLOWER', 'HACIENDA HEIGHTS', 'SIGNAL HILL', 'LA PUENTE', 'MONTCLAIR', 'JURUPA VALLEY', 'GUASTI', 'WILDOMAR', 'MENIFEE', 'COVINA', 'DOWNEY', 'MURRIETA', 'CAMP PENDLETON', 'PARAMOUNT', 'UPLAND', 'PICO RIVERA', 'MARCH AIR RESERVE BASE', 'FONTANA', 'CARSON', 'COMPTON', 'RANCHO CUCAMONGA', 'SAN DIMAS', 'CLAREMONT', 'GLENDORA', 'SOUTH EL MONTE', 'BELL', 'WILMINGTON', 'MONTEBELLO', 'EL MONTE', 'SAN PEDRO', 'BALDWIN PARK', 'SOUTH GATE', 'LYNWOOD', 'BELL GARDENS', 'LA VERNE', 'TEMECULA', 'LOS ANGELES', 'MORENO VALLEY', 'FALLBROOK', 'BLOOMINGTON', 'ROSEMEAD', 'AZUSA', 'HARBOR CITY', 'MONTEREY PARK', 'MAYWOOD', 'TORRANCE', 'DUARTE', 'GRAND TERRACE', 'HUNTINGTON PARK', 'TEMPLE CITY', 'LOMITA', 'GARDENA', 'SAN GABRIEL', 'SAN LUIS REY', 'RIALTO', 'MONROVIA', 'OCEANSIDE', 'ARCADIA', 'ALHAMBRA', 'COLTON', 'CITY OF INDUSTRY', 'RANCHO PALOS VERDES', 'HOMELAND', 'LOMA LINDA', 'PALOS VERDES PENINSULA', 'SAN MARINO', 'NUEVO', 'SIERRA MADRE', 'SAN BERNARDINO', 'SOUTH PASADENA', 'BRYN MAWR', 'INGLEWOOD', 'LAWNDALE', 'WINCHESTER', 'HAWTHORNE', 'PASADENA', 'HEMET', 'REDONDO BEACH', 'REDLANDS')

with sq.connect('directory.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM directory''')
    records = cursor.fetchall()

for row in records:
    with sq.connect('uls.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'''SELECT * FROM uls WHERE name = "{row[0]}" AND state = "CA"''')
        results = cursor.fetchall()
        if len(results) > 0:
            for operator in results:
                if operator[2].upper() in cities:
                    with open("report.txt", 'a') as report:
                        report.write(f"{operator[0]}\n")
                        for item in row:
                            if item != "":
                                report.write(f"{item}\n")
                        report.write("\n")