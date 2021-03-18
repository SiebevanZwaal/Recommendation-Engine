from pymongo import MongoClient
import psycopg2
from random import randint


def connect():
    '''opens connection with database'''
    global client
    global database
    global db_profiles
    global con
    global cur

    client = MongoClient()
    database = client.huwebshop

    db_profiles = database.profiles.find()

    con = psycopg2.connect(
        host="localhost",
        database="huwebshop",
        user="postgres",
        password="Vicecity_007",
    )
    cur = con.cursor()

def close():
    '''closes connection with database'''
    global cur
    global con
    cur.close()
    con.close()

def getID():
    pass

def wipecontentfilter():
    cur.execute('DROP TABLE IF EXISTS recommendations; CREATE TABLE recommendations(sub_sub_category varchar(255),gender varchar(255),brand varchar(255),id varchar(255),name varchar(255))')
    con.commit()

def wipecollaborationfilter():
    cur.execute('DROP TABLE IF EXISTS recommendations2; CREATE TABLE recommendations2(product_id varchar(255),segment varchar(255))')
    con.commit()

def contentfilter():
    # cur.execute('select sub_sub_category,gender,brand,id,name from product')
    # data = cur.fetchall()

    # subsubcategorylist = []
    # genderlist = []
    # brandlist = []
    #
    # subsubcategorydict = {}
    # genderdict = {}
    # branddict = {}
    #
    # for i in data:
    #     if i[1] not in subsubcategorylist:
    #         subsubcategorylist.append(i[1])
    #     if i[2] not in genderlist:
    #         genderlist.append(i[2])
    #     if i[4] not in brandlist:
    #         brandlist.append(i[4])
    # print(subsubcategorylist)
    # print(genderlist)
    # print(brandlist)


    subsubcategorylist = ['Nagellak',None, 'Nagellakremovers', 'Kunstnagels', 'Make-up accessoires', 'Oogschaduw', 'Foundation & concealer', 'Mascara', 'Lipstick', 'Wenkbrauwproducten', 'Reiniging', 'Poeder', 'Blush', 'Tandpasta', 'Shampoo', 'Elektrische tandenborstels', 'Haarkuur en haarmasker', 'Conditioner', 'Deodorant', 'Scheermesjes', 'Mondwater & spray', 'Aftershave', 'Bad en douche', 'Handzeep en handgel', 'Lipverzorging', 'Scheren', 'Scheerschuim en scheergel', 'Haarstyling', 'Toiletblokken', 'Handcremes', 'Homeopathisch', 'Lampen', 'Herengeuren', 'Incontinentie', 'Haarserum', 'Haarkleuring', 'Nachtcreme', 'Wasmiddel', 'Bodylotion en bodymilk', 'Schoonmaken', 'Gezichtsmasker', 'Baby huidverzorging', 'Wondverzorging', 'Pleisters', 'Damesgeuren', 'Toiletreinigers', 'Vaatwastabletten', 'Reiniging vaatwasser', 'Luchtwegen en verkoudheid', 'Pijnstillers', 'Mini deodorant en geuren', 'Wasverzachter', 'Babyhaartjes, bad en douche', 'Kerst', 'Dagcreme', 'Snacks en snoep', 'Mini bad en douche', 'Panties en sokken', 'Huishoudelijk textiel', 'Kunstgebitverzorging', 'Tandenborstels', 'Textielverf', 'Tampons', 'Afwasmiddel', 'Outdoor en vrije tijd', 'Luiers', 'Babydoekjes', 'Geschenksets', 'Glijmiddelen en seksspeeltjes', 'Vakantie', 'Mini tandpasta', 'Mini olie en lotion', 'Zonnebrand en aftersun', 'Mondverfrissers', 'Luchtverfrissers', 'Batterijen', 'Inlegkruisjes', 'Mini haarstyling', 'Make-up remover & reiniging', 'Maandverband', 'Mini shampoo en conditioner', 'Insectenbestrijding', 'Overige huishoudelijke artikelen', 'Vlekkenverwijderaars', 'Oogcreme en serum', 'Dames brillen', 'Mini scheerschuim en scheergel', 'Creme', 'Condooms', 'Intiemverzorging', 'Overige dierverzorging', 'Reiniging man', 'Huidverzorging en koortslip', 'Dames kleding', 'Spijsvertering', 'Oor en mond', 'Multivitaminen', 'Kind', 'Energie', 'Kaarsen', 'Tandenstokers, floss & ragers', "Vibrators en dildo's", 'Voetverzorging', 'Onzuivere huid & acne', 'Keuken artikelen', 'Ontharingscreme, wax en hars', 'Media', 'Woonaccessoires', 'Flessen en flessenspenen', 'Kappersproducten', 'Overige dranken', 'Speelgoed', 'Baby- en kinderaccessoires', 'Sportdranken', 'Toilettassen', 'Lenzen', 'Lenzenvloeistof', 'Sokken', 'Toiletpapier en vochtige doekjes', 'Stoppen met roken', 'Kalknagels', 'Heren ondergoed', 'Weerstand', 'Hond', 'Wattenschijfjes en wattenstaafjes', 'Kat', 'Babykleding', 'Tuinartikelen', 'Oordoppen', 'Halloween', 'Feestartikelen', 'Kantoor benodigdheden', 'Baby accessoires', 'Tissues en zakdoekjes', 'Verzorgende voetcremes', 'Beeld en geluid', 'Anti-lekbekers', 'Fopspenen', 'Spierwrijfmiddelen', 'Voetdeodorant', 'Voetschimmel', 'Sportverzorging', 'Luizen', 'Baby speelgoed', 'Boeken', 'Sportartikelen', 'Zwangerschapstest en ovulatietest', 'Gezichtsmasker man', 'Highlighters en bronzers', 'Mama verzorging', 'Dames ondergoed', 'Carnaval', 'Supplementen', 'Tablets en computers', 'Haaraccessoires', 'Keukenpapier', 'Botten', 'Enkelvoudige vitaminen', 'Overige voedingssuplementen', 'Uiterlijk', 'Ontspanning en rust', 'Tassen', 'Wondontsmetting', 'Lipliner', 'Blaas', 'Hart en visolie', 'Mineralen', 'Gewrichten', 'Elektronica accessoires', 'Flesvoeding', 'Chips', 'Sieraden & bijoux', 'Koffie', 'Zwemluiers', 'Sportvoeding', 'Verlichting', 'Zwangerschapsvitamines', 'Knutselen en hobby', 'Watten', 'Wratten', 'Lipgloss', 'Patty Brard Collectie', 'Dames accessoires', 'Luierbroekjes en pyjamabroekjes', 'Thee', 'Bandages en windsels', 'Kinderbestek', 'Persoonlijke verzorging', 'EHBO', 'Foto en film', 'Heren accessoires', 'Man', 'Kinderkleding', 'Zwangerschap', 'Koffers', 'Cartridges', 'Eelt en harde huid', 'Huishoudelijke apparaten', 'Overige elektronika', 'Muziek', 'Scheerapparaten', 'Dvd en blue-ray', 'Schoenen, slippers en sloffen', 'Accessoires', 'Kaarten', 'Dames nachtmode', 'Leesbrillen', 'Heren brillen', 'Vaginale schimmel', 'Natuurlijke gezondheid', 'Pasen', 'Meubels', 'Telefonie', 'Valentijn', 'Energy drank', 'Maaltijdvervangers', 'Allergieen', 'Bordspellen', 'Heren nachtmode', 'Reisziekte', 'Aambeien']
    genderlist = ['Unisex',None, 'Vrouw', 'Man', 'Gezin', 'B2B', 'Kinderen', 'Baby', 'Senior', 'Grootverpakking', '8719497835768']

    wipecontentfilter()

    for category in subsubcategorylist:
        for gender in genderlist:
            cur.execute('SELECT sub_sub_category,gender,brand,id,name FROM product WHERE sub_sub_category = %s and gender =%s LIMIT 4',(category,gender))
            data = cur.fetchall()
            # for product in data:
            #     print(product)

            cur.executemany('INSERT INTO recommendations VALUES(%s,%s,%s,%s,%s)',data)

    con.commit()

    # brandlist = ['Op is Op', 'Saffron', 'Royal Cosmetic Connections', 'W7', 'Colgate', 'Andrelon', 'Garnier', 'Axe', 'Wilkinson', 'Rexona', 'Listerine', 'Brut', 'Fa', 'Dove', 'Denim', 'Schwarzkopf', 'Labello', 'De Vergulde Hand', 'Gillette', 'Airwick', 'Glycerona', 'VSM', 'Calex', 'Tena', 'Syoss', 'Diadermine', 'Robijn', 'Bio-Oil', 'Cif', 'L Oreal', 'Nivea', 'Sanex', 'Montagne Jeunesse', 'Zwitsal', 'Guhl', 'Shirley May', 'Sunil', 'Palmolive', 'Maybelline', 'Proset', 'Cillit', 'Harpic', 'Finish', 'Kleenex', 'WC-Eend', 'HTP', 'Kneipp', 'Sudocrem', 'Sunlight', 'Blue Stratos', 'Vogue', 'Prodent', 'Head And Shoulders', 'Neutral', 'Vaseline', 'Johnsons', 'Purol', 'Goldline', 'Therme', 'KitKat', 'Mars', 'Nestle', 'Snickers', 'Twix', 'Mr Muscle', 'Atrix', 'SoftSocks', 'Shine', 'Dente Dura', 'Dylon', 'Murrays', 'Nu Nile', 'Bigen', 'ORS', 'Rident', 'OB', 'HCA', 'Sito', 'Cleany', 'Promo', 'John Frieda', 'Pampers', 'Glorix', 'Burberry', 'Davidoff', 'Dolce en Gabbana', 'Diesel', 'Laura Biagiotti', 'Durex', 'Thomas', 'Ambi Pur', 'Wella', 'Omo', 'Sportlife', 'Nicols', 'Duracell', 'Theramed', 'Oral-B', 'Always', 'Bounty Mini', 'Milky Way', '8x4', 'Playboy', 'Unicura', 'Byphasse', 'Fruittella', 'Mentos', 'Vapona', 'Page', 'Zendium', 'Elmex', 'Odorex', 'Vanish', 'Blue Wonder', 'Adidas', 'Andy', 'Aquafresh', 'Melkmeisje', 'Alpifresh', 'Smarties', 'Dumil', 'Studio Line', 'Hegron', 'Fixodent', 'Puma', 'Sun', 'Bref', 'Kinder', 'Kinder Bueno', 'Brise', 'Varta', 'Rayovac', 'Sence', 'Marbert', 'Best for your friend', 'Jordan', 'Studio', 'Tommy Hilfiger', 'Chopard', 'David Beckham', 'Vinolia', 'Jaguar', 'Dubro', 'Floratex', 'Denterest', 'Compeed', 'At Home', 'Calvin Klein', 'Milka', 'Dreft', 'Kylie', 'Savon Doux Classique', 'Kate Moss', 'Sorbo', 'Tic Tac', 'Libresse', 'Victoria Beckham', 'Argan', 'Chupa Chups', 'Agfa', 'Olaz', 'Adelante', 'Sensodyne', 'Apollo', 'Esprit', 'Dermalex', 'Formule W', 'Imodium', 'Roter', 'Vicks', 'Dampo', 'Davitamon', 'Prevalin', 'Dr Van Der Hoog', 'Amando', 'Skittles', 'Autodrop', 'Fishermans', 'Dr. Swaab', 'Cillit Bang', 'SenceFresh', 'Dermolin', 'Resdan', 'Silan', 'Persil', 'Kotex', 'Inecto', 'Parodontax', 'Calgon', 'Herbamedicus', 'Jean Marc', 'Eleganza', 'SterStyle', 'Biotex', 'Toy Joy', 'Old Spice', 'Rimmel', 'Hansaplast', 'Tea Tree', 'Ritter Sport', 'Clearasil', 'Loda', 'Max Factor', 'Zirh', 'Lactacyd', 'Badedas', 'Nibro', 'Werthers Original', 'Travelagent', 'Veet', 'Zaini', 'Creation', 'Backscratcher', 'Bathroom Solutions', 'Ariel', 'Bodysecret', 'Farouk', 'Maoam', 'Fresh Up', 'Lipton', 'Herbal', 'Studio 100', 'Mega Mindy', 'Coca-Cola', 'Fanta', 'Red Bull', 'Rio', 'Dash', 'Corega', 'Parfum De Fleur', 'Splash', 'Bright', 'Fittydent', 'Bright Eyes', 'Plackers', 'Britney Spears', 'Joop', 'Cacharel', 'Nina Ricci', 'Australian', 'AA', 'Sprite', 'Nicotinell', 'Nailner', 'Strepsils', 'Toys4You', 'Maja', 'Steradent', 'Bolsius', 'Lowboys', 'Pedigree', 'Dermomed', 'Demak Up', 'BIC', 'Whiskas', 'Glade', 'Kappa', 'Groenland', 'Entity', 'Dorall', 'Baby', 'Sanrio', 'Dettol', 'Dixan', 'Disney', 'Mickey & Minnie', 'Beyonce', 'Lolita Lempicka', 'Giorgio Beverly Hills', 'Iceberg', 'Jean Paul Gaultier', 'Astor', 'Mimosa', 'Guess', 'Actif', 'Kylie Minogue', 'Lip Smacker', 'Junior Elf', 'Ohropax', 'Red Band', 'Anta Flu', 'Haribo', 'Partychimp', 'Lenor', 'Embrace', 'Pantene', 'Fruity Sensation', 'Scholl', 'Max Brands', 'Spa Secrets', 'Biotin & Collagen', 'BodyX', 'Biotanicus', 'Dutch Originals', 'Aroma Di Rogito', 'Sence Beauty', 'Trachitol', 'Ajax', 'Soapy', 'Ultra', 'Le Jardin', 'Sagrotan', 'Oktoberfest', 'Body treatment', 'Midalgan', 'Dales & Dunes', 'Bruno Banani', 'Heidi Klum', '1Auto', 'Cadbury', 'Venco', 'Katja', 'Swiffer', 'Hero', 'KC Oxid', 'Xt-Luis', 'NUK', 'Bargje Big', 'Maya', 'Ballon', 'Impliva', 'Siglitos', 'King', 'Catisfactions', 'Sebamed', 'Capri-Sun', 'Nurofen', 'Carin Haircosmetics', 'Biodermal', 'Philips', 'Pure&Care', 'Prokennex', 'Predictor', 'Mind Candy', 'Ben10', 'Doctor Clean', "M&M's", 'Lion', 'Quick', 'Gehwol', 'Aquarius', 'Croc', 'Chaudfontaine', 'Jumbo', 'Wetties', 'Sence Beauty Time', 'Gemar Balloons', 'Simpsons', 'Sanicur', 'Protex', 'Minions', 'Sesamstraat', 'Huggies', 'Dasty', 'La Paay', 'Meridol', 'Essential Organics', 'Yours', 'Stimul8', 'Oldtimers', 'Walking Socks', 'Sheba', 'Laser', 'Pledge', 'KFS-B-Candles', 'Gloria Vanderbilt', 'Seashell', 'Pro Garden', 'Bath Fizzer', 'MB', 'CL', 'Proud', 'Heathcote & Ivory', 'Rakker', 'XL-S', 'Big Soft', 'Lifes Up', 'Jil Sander', 'Oreo', 'Celine Dion', 'Vileda', 'Plantur', 'Alpecin', 'Coccolino', 'Herbal Essences', 'Ralph Lauren', 'Mexx', 'Moshi', 'Pure Buddha', 'Umbro', 'Van Gils', 'HL Agenturen', 'Gel Beads', 'Monster High', 'Ooops', 'Bien', 'Vernel', 'Lucovitaal', 'Dentalcare', 'Paul Frank', 'Kitekat', 'Replay', "Tesori d'Oriente", 'Early Sign', 'Silk', 'Deluxa', 'Napisan', 'Lafita', 'Soundlogic', 'Elizabeth Arden', 'Shirley', 'Tefal', 'Wipp', 'Bifi', 'Vasenol', 'Bon Giorno', 'Nutrilon', 'Pringles', 'Pierre Cardin', 'Citronella', 'Bye Bites', 'Issey Miyake', 'Bransus', 'Joy Division', 'Diamond', 'Choco Time', 'Stimorol', 'Autan', 'Ibex', 'Buisman', 'Dextro', 'Siderius', 'Lu', 'Salvequick', 'Riesen', 'NESCAFE', 'Black & Red', 'O Neill', 'Candy', 'K2r', 'Xpel Hair Cair', 'Mr Proper', 'Olay', 'Savon', 'Luxe Star', 'Cosmo', 'Zantac', 'Witte Reus', 'Toblerone', 'Blistex', 'Marletka', 'Baylis and Harding', 'Zocool', 'Sky Candy', 'EasyToys', 'SBT', 'SBR', 'Easyglide', 'Elite Models', 'Heat Keeper', 'Fine Luxury Soaps', 'Brylcreem', 'Pestalozzi Puzzle', 'Queen Royale', 'Cosmo Designs', 'Coop', 'My Happy Pets', 'Wash & Go', 'Trolls', 'Balance', 'Spaas', 'Thorntons', 'Vibovit', 'Daro', 'CB12', 'Wartner', 'Color', 'Treffer', 'Baron', 'Mullrose', 'Christina Aguilera', 'Luxury', 'Estee Florance', 'Muchachomalo', 'Febreze', 'Premium Parts', 'Zazie', 'Bional', 'Kodak', 'UHU', 'Tetesept', 'P&G Professional', 'Alpina', 'Bepanthen', 'Niquitin', 'Strepfen', 'Duschdas', 'Vegter', 'Black Onyx', 'Earth Kiss', 'Spectrum', 'Lifetime', 'Patty', 'Create It!', 'Bicycle Gear', 'Home & Styling Collection', 'PB', 'CSI', 'Velpon', 'Dunlop', 'Elegance', 'A Vogel', 'Canesten', 'Gaviscon', 'Nisska', 'Oroclean', 'Otalgan', 'Tiger Balm', 'Valdispert', 'Kledingroller', 'Excellent Houseware', 'Wasknijpers', 'Storage Solutions', 'Bloemen', 'La Cucina', 'Thermometer', 'ecovif', 'Home Basics', 'Roundies', 'Rodeo', 'Dutch Decor', 'Kitchen Collection', 'DreamWorks', 'Beco', 'Click&Fresh', 'Aluflon', 'Royal Konig', 'Edet', 'Boek Specials Nederland', 'Color Plus', 'Canard', 'ABK', 'Domestos', 'Nova', 'Fleurus', 'Tristar', 'FX Tools', 'Work Socks', 'Kuschelweich', 'Ceracraft', 'Vaporesse', 'JML', 'Turbo Maxx', 'Excellent Dental Care', 'Bobble Off', 'Schott Zwiesel', 'Tactic', 'BBQ Collection', 'Perfect Fit', 'Dynamic Energy', 'Bestway', 'Fisher-Price', 'Pepi', 'Activa', 'Acord', 'BenBits', 'Playtime', 'Ultra Clean', 'Benson Care', 'Lastpak', 'Benson', 'Urban Junk', 'Benson Tools', 'THM', 'Dolmen', 'WD-40', 'Qura', 'Mens Health', 'Regis Stone', 'Arterin', 'Jaico', 'Jungle Formula', 'Samenwerkende Apothekers', 'Tantum', 'Magic Brush', 'Voor Jou!', 'New Rebels', 'Iba Paris', 'Evora', 'Who`s Hair', 'DKNY', 'Duyvis', 'Maltesers', 'Russky Kazak', 'Tommee Tippee', 'Simba', 'Unico Plus', 'Beauty Skin Care', 'Franck Provost', 'DLP', 'Etui', 'Casio', 'Runaway', 'Nedac', 'Writewell', 'Stationery Neon', 'Bamboo', 'Snow Queen', 'Canderel', 'Dextro Energy', 'Meisterbach', 'Waterzone', 'Peppa Pig', 'Paw Patrol', 'Polaroid', 'Spiderman', 'Batman', 'Perfectly Clear', 'Frolic', 'Cuisinier Elegance', 'Evian', 'Benson Office', 'Stahlex', 'Nouka', 'Sanders', 'Op = Op Boeken', 'Dehghan', 'The Marshmallow Company', 'Tricel Oxi', 'Pure Plus', 'Aloe Vera Fresh', 'Real Time', 'Kind Looks', 'Sporty & Pink', 'Night Canyon', 'Calypso', 'QNT', 'Fun Outdoors', 'grafix', 'Sunware', 'Marco Milano', 'Ice Age', 'Antikal', 'Piove', 'Twingles', 'Insect Trap', 'Plant Protect', 'Princess', 'Safety', 'Magic Door Mesh', 'DermaSel', 'Blend-a-med', 'Piace Molto', 'Amefa', 'Canon', 'Epson', 'HP', 'Imagebooks', 'Manhattan', 'Converse', 'Fresh for Life', 'Denivit', 'Tempo', 'Crocodor', 'Fashion Professional', 'La Pelucheria', 'Interior Elegance', 'Findon', 'JES collection', 'Hosti', 'Cartoon Network', 'Dr. Care', 'Gillette Venus', 'Marvel', 'New Balance', 'Dummy', 'Lief!', 'Ranex', 'Antonio Miro', 'Modderman', 'Studio Onszelf', 'Deco', 'Kwikkie', 'Brother', 'Gusta', 'Coral', 'Home Edition', 'Toni&Guy', 'Masha and the Bear', 'Pritt', 'Angry Birds', 'Around The Home', "L'alerteur", 'Gold Rush', 'Fritt', 'Schogetten', 'The Secret Life of Pets', 'Floppy', 'Bellson', 'Storage Line', 'Handy Mates', 'Azoza', 'Smartwares', 'Topcom', 'Flamingo', 'My Favorite Friends', 'Superdry', 'Belux', 'Food for Fun', 'Kukident', 'Easy Line', 'SQZD', 'Domior', 'Lynx', 'Burago', 'Active Sports', 'Nickelodeon', 'Hit', 'Yokebe', 'Stewardess', 'Klok', 'Erik van Klinken', 'Eco Styler', 'Opticalm', 'HNP', 'Decostar', 'CF Nails', 'Symex', 'Grundig', 'Metal Mekanic', 'Asmodee', 'Play-Doh', 'Playskool', 'Mad Machines', 'Knex', 'Lufkin', 'Topmaxx', 'Cresent', 'Wiss', 'Selina', 'Clown Games', 'Tex-Pert', 'Beta Klus Box', 'Trumpf', 'Braun', 'PlayBIG Bloxx', 'Kiwi', 'Tigi', 'Hakle', "Lay's", "Dr. Tom's", 'Elseve', 'Planters', 'Little Lovelies', 'Chewmaster', 'Block Tech', 'Pip Studio', 'Bibi', 'Universal', 'Dickie Toys', 'Kai Deng', 'Barbie', 'Hot Wheels', 'Footcare', 'Odina', 'Comfort Aid', 'Vita', 'Telefunken', 'Bath & Shower', 'Marinex', 'Tresemme', 'Cesar', 'Signal', 'Pepsodent', 'This Is It', 'Trendy Girlz', 'Icon', 'Cosmetics to Go', 'Care Plus', 'Gimborn', 'HeltiQ', 'Leidapharm', 'Norlevo', 'Fruttini', 'Revlon', 'Home & Deco', 'Trufalié', 'Lifebuoy', 'Radox', 'Intex', 'Vidal Sassooon', 'Lux', 'Star Bright', 'Siro', 'Black & White Cuisine', 'Like it a lot', 'Bel Premium', 'Sensitive', 'Frozen', 'Cars', 'Denver', 'Happy Chocolate', 'Voetbal Inside', 'Weekdeal', 'Ideal', 'Trespass', 'Toffifee', 'Pure', 'Asco', 'Funnycandy', 'Taveners', 'Felix', 'Paris Riviera', 'Wiko', 'Samsung', 'Play and Joy', 'Goldwell', 'Orofluido', 'Color  Me', 'Nokia', 'Alcatel', 'Leapp iPhone', 'DProduct4', 'Lifetime Garden', 'Kinzo Garden', 'Op is Op Kids', 'Inventum', 'Hydro Clean', 'Core Max', 'Turbo Stick', 'Super Sports', 'Vince Design', 'Op = Op Kids', 'Peanuts', 'Antonio', 'Orange Elephant', 'Top Juice', 'Breazz', 'Aussie', 'Proderm', 'Vitory', 'Chillfactor', 'Poly', 'Op is Op Toys', 'Bosch', 'Edco', 'Softy', 'Indoor Life', 'KNVB', 'Eurobed', 'Guylian', 'Xpel Oral Care', 'Starscent', 'Dell', 'Bestron', 'Dalan D Olive', 'Slazenger', 'Gigaset', 'DIY', 'Lexro', 'Grolsch', 'Daniel Hechter', 'Libby Design', 'Eddy Toys', 'Fresh and Cold', 'Scatch', 'Home and Away 2.0', 'TomTom', 'Hydroblast', "Pet's Unlimited", 'Sappy', 'Leev', 'Celebrations', 'Green Nature', 'Jono Toys', 'Silen', 'Probike', 'Lebara', 'Selpak', 'Outdoor Life', 'RefectoCil', 'Belflam', 'My Little Pony', 'Continental Bakeries', 'DohVinci', 'Tonka', 'Atomic', 'Nerf', 'Air Dragon', 'Lifetime Clean', 'Envy', 'SexyHair', 'Be Creativ', 'N-Joy', 'Sunny', 'Grand Maestro Italiano', 'Wahl', 'Amstel', 'Casibel', 'Verkade', 'Illy', 'Seven For 7', 'Vivess', 'Bounty', 'Funtastix', "Grab 'n Go", 'mi ABC', 'Pip&Nut', 'Bolletje', 'Doccio', 'Fava Mill', 'Rocky Mountains', 'Gicopa', 'Gummy Zone', 'Love Bomb Cushion', 'Extreme Clean', 'Zed Candy', 'IronWood', 'Gies', 'Brew Monkey', 'Bison', 'Zonnatura', 'van der Meulen', 'James Bond', "Lucy's Home", 'Diele', 'Lonka', 'Cheetos', 'Kraft', 'Quaker', 'Sgreasy', 'Miffy', 'Fortuin', 'Chocoland', 'Belvita', 'Asus', 'Dunicec', 'Strike Energy', 'Bjorn Borg', 'Famosa', 'Hasbro', 'Zensation', 'Candy Cane', 'Fast and Furious', 'Kiddymix', 'Magnani Italy', 'Chocomel', 'Reload', 'Cafe Paris', 'Mandemakers', 'Thermo Heat', 'De Ruiter', 'Molens Banket', 'Rang', 'Liga', 'Familie Pos', 'Chio', 'Meltums', 'Hatchimals', 'Molino', 'Larco', 'GlitterPalz', 'XL-S Medical', 'Navigator', 'Thermo', 'Brink', 'Crococoll', 'Sula', 'Starlyf', 'Bavaria', 'DubbelFrisss', 'Marne', 'Delhaize', 'Springing', 'Mr. Cream', 'Slava Zaitsev', 'Bel Cosmetic', 'Aleve', 'Clean', 'Advil', 'Antigrippine', 'Aspirine', 'Azaron', 'Betadine', 'Bisolvon', 'Citrosan', 'Norit', 'Oscillococcinum', 'Primatour', 'Rennie', 'Saridon', 'Sinaspril', 'Sperti', '5 99', 'Voltaren', 'Zovirax', 'FCUK']


def collaborativefilter():

    # cur.execute('SELECT DISTINCT segment FROM profile')
    # segs = cur.fetchall()
    # segments =[]
    # for segment in segs:
    #     if list(segment)[0] is not None and list(segment)[0].lower() not in segments:
    #         segments.append(list(segment)[0].lower())

    segments = ['leaver', 'bouncer', 'fun_shopper', 'judger', 'browser', 'comparator', 'shopping_cart', 'buyer', 'comparer']
    segmentdict = {}

    cur.execute('SELECT previously_recommended.productid as product_id,profile.segment FROM profile '
                'INNER JOIN previously_recommended ON profileprofile_id = profile.profile_id '
                'WHERE profile.segment is not null ')
    products = cur.fetchall()

    print(products)
    for product,seg in products:
        segment = seg.lower()
        if segment in segmentdict.keys():
            if product in segmentdict[segment]:
                segmentdict[segment][product] +=1
            else:
                segmentdict[segment][product] = 1
        else:
            segmentdict[segment] = {product:1}
    print(segmentdict)
    #uit sementdict halen wat de meest populaire producten zijn per segment


    for segment in segments:
        highestfreq0 = ['',0]
        highestfreq1 = ['',0]
        highestfreq2 = ['',0]
        highestfreq3 = ['',0]

        id_frequency_dict = segmentdict[segment]
        for id,frequency in id_frequency_dict:
            if frequency > highestfreq0:
                highestfreq3 = highestfreq2
                highestfreq2 = highestfreq1
                highestfreq1 = highestfreq0
                highestfreq0 = [id,frequency]
            elif frequency > highestfreq1:
                highestfreq3 = highestfreq2
                highestfreq2 = highestfreq1
                highestfreq1 = [id,frequency]
            elif frequency > highestfreq2:
                highestfreq3 = highestfreq2
                highestfreq2 = [id,frequency]
            elif frequency > highestfreq3:
                highestfreq3 = [id,frequency]
        data =[]
        data.append()
        cur.executemany('INSERT INTO recommendations2 VALUES(%s,%s)',data)



def main():
    connect()
    #contentfilter()
    collaborativefilter()
    close()



if __name__ == '__main__':
    main()

# Story 5: Categorieën (van sub sub):
# Story 6: Kochten ook
# Story 7: Aanbiedingen
# Story 8: Merk
# Story 9: Type klant