# -*- coding: utf-8 -*-

##
# Module for helper static variables
##

# Event Licences

EVENT_LICENCES = {
    # Licence Name : ( Long Name, Description, Licence URL, Licence Logo, Licence Compact Logo )
    'All rights reserved': (
        'All rights reserved',
        u'The copyright holder reserves, or holds for their own use, all the rights provided by copyright law under '
        u'one specific copyright treaty.',
        'https://en.wikipedia.org/wiki/All_rights_reserved',
        '',
        ''),
    'Attribution': (
        'Creative Commons Attribution 4.0 International License',
        u'This license lets others distribute, remix, tweak, and build upon the work, even commercially, as long as '
        u'they credit the copyright holder for the original creation.',
        'https://creativecommons.org/licenses/by/4.0',
        'https://licensebuttons.net/l/by/3.0/88x31.png',
        'https://licensebuttons.net/l/by/3.0/80x15.png'),
    'Attribution-ShareAlike': (
        'Creative Commons Attribution-ShareAlike 4.0 International License',
        u'This license lets others remix, tweak, and build upon the work even for commercial purposes, as long as '
        u'they credit the copyright holder and license their new creations under the identical terms.',
        'https://creativecommons.org/licenses/by-sa/4.0',
        'https://licensebuttons.net/l/by-sa/3.0/88x31.png',
        'https://licensebuttons.net/l/by-sa/3.0/80x15.png'),
    'Attribution-NoDerivs': (
        'Creative Commons Attribution-NoDerivs 4.0 International License',
        u'This license allows for redistribution, commercial and non-commercial, as long as it is passed along '
        u'unchanged and in whole, with credit to the copyright holder.',
        'https://creativecommons.org/licenses/by-nd/4.0',
        'https://licensebuttons.net/l/by-nd/3.0/88x31.png',
        'https://licensebuttons.net/l/by-nd/3.0/80x15.png'),
    'Attribution-NonCommercial': (
        'Creative Commons Attribution-NonCommercial 4.0 International License',
        u'This license lets others remix, tweak, and build upon the work non-commercially, and although their new '
        u'works must also acknowledge the copyright holder and be non-commercial, they don’t have to license their '
        u'derivative works on the same terms.',
        'https://creativecommons.org/licenses/by-nc/4.0',
        'https://licensebuttons.net/l/by-nc/3.0/88x31.png',
        'https://licensebuttons.net/l/by-nc/3.0/80x15.png'),
    'Attribution-NonCommercial-NoDerivs': (
        'Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International License',
        u'This license only allows others to download the work and share them with others as long as they credit the '
        u'copyright holder, but they can’t change them in any way or use them commercially.',
        'https://creativecommons.org/licenses/by-nc-nd/4.0',
        'https://licensebuttons.net/l/by-nc-nd/3.0/88x31.png',
        'https://licensebuttons.net/l/by-nc-nd/3.0/80x15.png'),
    'Attribution-NonCommercial-ShareAlike': (
        'Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License',
        u'This license lets others remix, tweak, and build upon the work non-commercially, as long as they credit the '
        u'copyright holder and license their new creations under the identical terms.',
        'https://creativecommons.org/licenses/by-nc-sa/4.0',
        'https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png',
        'https://licensebuttons.net/l/by-nc-sa/3.0/80x15.png'),
    'Public Domain Dedication (CC0)': (
        'Creative Commons Public Domain Dedication (CC0)',
        u'The copyright holder waives his interest in his work and places the work as completely as possible in the '
        u'public domain so others may freely exploit and use the work without restriction under copyright or database '
        u'law.',
        'https://creativecommons.org/publicdomain/zero/1.0/',
        'http://i.creativecommons.org/p/zero/1.0/88x31.png',
        'http://i.creativecommons.org/p/zero/1.0/80x15.png'),
    'Public Domain Work': (
        'Creative Commons Public Domain Work',
        u'This license enables works that are no longer restricted by copyright to be marked as such in a standard '
        u'and simple way, making them easily discoverable and available to others.',
        'https://creativecommons.org/publicdomain/mark/1.0/',
        'https://licensebuttons.net/p/mark/1.0/88x31.png',
        'https://licensebuttons.net/p/mark/1.0/80x15.png')
}

# Event Topics with sub topics

EVENT_TOPICS = {
    'Auto, Boat & Air': ['Air', 'Auto', 'Boat', 'Motorcycle/ATV', 'Other'],
    'Business & Professional': [
        'Career', 'Design', 'Educators', 'Environment &amp; Sustainability',
        'Finance', 'Media', 'Non Profit &amp; NGOs', 'Other', 'Real Estate',
        'Sales &amp; Marketing', 'Startups &amp; Small Business'
    ],
    'Charity & Causes': [
        'Animal Welfare', 'Disaster Relief', 'Education',
        'Environment', 'Healthcare', 'Human Rights',
        'International Aid', 'Other', 'Poverty'
    ],
    'Community & Culture': [
        'City/Town', 'County', 'Heritage', 'LGBT', 'Language',
        'Medieval', 'Nationality', 'Other', 'Renaissance', 'State'
    ],
    'Family & Education': [
        'Alumni', 'Baby', 'Children &amp; Youth', 'Education', 'Other',
        'Parenting', 'Parents Association', 'Reunion'
    ],
    'Fashion & Beauty': [
        'Accessories', 'Beauty', 'Bridal', 'Fashion', 'Other'
    ],
    'Film, Media & Entertainment': [
        'Adult', 'Anime', 'Comedy', 'Comics', 'Film', 'Gaming', 'Other', 'TV'
    ],
    'Food & Drink': ["Beer", "Food", "Other", "Spirits", "Wine"],
    'Government & Politics': [
        "County/Municipal Government", "Democratic Party", "Federal Government",
        "Non-partisan", "Other", "Other Party", "Republican Party",
        "State Government"
    ],
    'Health & Wellness': [
        "Medical", "Mental health", "Other", "Personal health", "Spa", "Yoga"
    ],
    'Hobbies & Special Interest': [
        "Adult", "Anime/Comics", "Books", "DIY", "Drawing & Painting", "Gaming",
        "Knitting", "Other", "Photography"
    ],
    'Home & Lifestyle': ["Dating", "Home & Garden", "Other", "Pets & Animals"],
    'Music': [
        "Alternative", "Blues & Jazz", "Classical", "Country", "Cultural",
        "EDM / Electronic", "Folk", "Hip Hop / Rap", "Indie", "Latin", "Metal",
        "Opera", "Other", "Pop", "R&B", "Reggae", "Religious/Spiritual", "Rock",
        "Top 40"
    ],
    'Other': ["Avatar"],
    'Performing & Visual Arts': [
        "Ballet", "Comedy", "Craft", "Dance", "Fine Art", "Literary Arts",
        "Musical", "Opera", "Orchestra", "Other", "Theatre"
    ],
    'Religion & Spirituality': [
        "Buddhism", "Christianity", "Eastern Religion", "Islam", "Judaism",
        "Mormonism", "Mysticism and Occult", "New Age", "Other", "Sikhism"
    ],
    'Science & Technology': [
        "Biotech", "High Tech", "Medicine", "Mobile", "Other", "Robotics",
        "Science", "Social Media"
    ],
    'Seasonal & Holiday': [
        "Channukah", "Christmas", "Easter", "Fall events", "Halloween/Haunt",
        "Independence Day", "New Years Eve", "Other", "St Patricks Day",
        "Thanksgiving"
    ],
    'Sports & Fitness': [
        "Baseball", "Basketball", "Cycling", "Exercise", "Fighting & Martial Arts",
        "Football", "Golf", "Hockey", "Motorsports", "Mountain Biking",
        "Obstacles", "Other", "Rugby", "Running", "Snow Sports", "Soccer",
        "Swimming & Water Sports", "Tennis", "Volleyball", "Walking", "Yoga"
    ],
    'Travel & Outdoor': [
        "Canoeing", "Climbing", "Hiking", "Kayaking", "Other", "Rafting", "Travel"
    ]
}
PAYMENT_COUNTRIES = {
    'United States',
    'Argentina',
    'Australia',
    'Austria',
    'Belgium',
    'Brazil',
    'Canada',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Estonia',
    'Finland',
    'France',
    'Germany',
    'Greece',
    'Hong Kong',
    'Hungary',
    'Ireland',
    'Israel',
    'Italy',
    'Japan',
    'Latvia',
    'Lithuania',
    'Luxemborg',
    'Malaysia',
    'Malta',
    'Mexico',
    'Netherlands',
    'New Zealand',
    'Norway',
    'Philippines',
    'Poland',
    'Portugal',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Spain',
    'Sweden',
    'Switzerland',
    'Taiwan',
    'United Kingdom',
}

# (currency_code,available_on_paypal,available_on_stripe)
PAYMENT_CURRENCIES = {
    ('AUD', True, True),
    ('BRL', True, True),
    ('CAD', True, True),
    ('CHF', True, True),
    ('CZK', True, True),
    ('DKK', True, True),
    ('EUR', True, True),
    ('GBP', True, True),
    ('HKD', True, True),
    ('HUF', True, True),
    ('ILS', True, True),
    ('INR', False, True),
    ('JPY', True, True),
    ('MXN', True, True),
    ('MYR', True, True),
    ('NOK', True, True),
    ('NZD', True, True),
    ('PHP', True, True),
    ('PLN', True, True),
    ('RUB', True, True),
    ('SEK', True, True),
    ('SGD', True, True),
    ('THB', True, True),
    ('TWD', True, True),
    ('USD', True, True),
}

# Event Images with Event Topics and Subtopics

DEFAULT_EVENT_IMAGES = {
    'Auto, Boat & Air': 'auto.jpg',
    'Air': 'auto.jpg',
    'Auto': 'auto.jpg',
    'Boat': 'auto.jpg',
    'Motorcycle/ATV': 'auto.jpg',
    'Business & Professional': 'business.jpg',
    'Career': 'business.jpg',
    'Design': 'business.jpg',
    'Educators': 'business.jpg',
    'Environment &amp; Sustainability': 'business.jpg',
    'Finance': 'business.jpg',
    'Media': 'business.jpg',
    'Non Profit &amp; NGOs': 'business.jpg',
    'Real Estate': 'business.jpg',
    'Sales &amp; Marketing': 'business.jpg',
    'Startups &amp; Small Business': 'business.jpg',
    'Charity & Causes': 'charity.jpg',
    'Animal Welfare': 'charity.jpg',
    'Disaster Relief': 'charity.jpg',
    'Environment': 'charity.jpg',
    'Healthcare': 'charity.jpg',
    'Human Rights': 'charity.jpg',
    'International Aid': 'charity.jpg',
    'Poverty': 'charity.jpg',
    'Community & Culture': 'culture.jpg',
    'City/Town': 'culture.jpg',
    'County': 'culture.jpg',
    'Heritage': 'culture.jpg',
    'LGBT': 'culture.jpg',
    'Language': 'culture.jpg',
    'Medieval': 'culture.jpg',
    'Nationality': 'culture.jpg',
    'Renaissance': 'culture.jpg',
    'State': 'culture.jpg',
    'Family & Education': 'education.jpg',
    'Alumni': 'education.jpg',
    'Baby': 'education.jpg',
    'Children &amp; Youth': 'education.jpg',
    'Education': 'education.jpg',
    'Parenting': 'education.jpg',
    'Parents Association': 'education.jpg',
    'Reunion': 'education.jpg',
    'Fashion & Beauty': 'fashion.jpg',
    'Accessories': 'fashion.jpg',
    'Beauty': 'fashion.jpg',
    'Bridal': 'fashion.jpg',
    'Fashion': 'fashion.jpg',
    'Film, Media & Entertainment': 'film.jpg',
    'Adult': 'film.jpg',
    'Anime': 'film.jpg',
    'Comedy': 'film.jpg',
    'Comics': 'film.jpg',
    'Film': 'film.jpg',
    'Gaming': 'film.jpg',
    'TV': 'film.jpg',
    'Food & Drink': 'food.jpg',
    "Beer": 'food.jpg',
    "Food": 'food.jpg',
    "Spirits": 'food.jpg',
    "Wine": 'food.jpg',
    'Government & Politics': 'government.jpg',
    "County/Municipal Government": 'government.jpg',
    "Democratic Party": 'government.jpg',
    "Federal Government": 'government.jpg',
    "Non-partisan": 'government.jpg',
    "Other Party": 'government.jpg',
    "Republican Party": 'government.jpg',
    "State Government": 'government.jpg',
    'Health & Wellness': 'health.jpg',
    'Hobbies & Special Interest': 'hobbies.jpg',
    "Adult": 'hobbies.jpg',
    "Anime/Comics": 'hobbies.jpg',
    "Books": 'hobbies.jpg',
    "DIY": 'hobbies.jpg',
    "Drawing & Painting": 'hobbies.jpg',
    "Gaming": 'hobbies.jpg',
    "Knitting": 'hobbies.jpg',
    "Photography": 'hobbies.jpg',
    'Home & Lifestyle': 'home.jpg',
    "Dating": 'home.jpg',
    "Home & Garden": 'home.jpg',
    "Pets & Animals": 'home.jpg',
    'Music': 'music.jpg',
    "Alternative": 'music.jpg',
    "Blues & Jazz": 'music.jpg',
    "Classical": 'music.jpg',
    "Country": 'music.jpg',
    "Cultural": 'music.jpg',
    "EDM / Electronic": 'music.jpg',
    "Folk": 'music.jpg',
    "Hip Hop / Rap": 'music.jpg',
    "Indie": 'music.jpg',
    "Latin": 'music.jpg',
    "Metal": 'music.jpg',
    "Opera": 'music.jpg',
    "Pop": 'music.jpg',
    "R&B": 'music.jpg',
    "Reggae": 'music.jpg',
    "Religious/Spiritual": 'music.jpg',
    "Rock": 'music.jpg',
    "Top 40": 'music.jpg',
    'Other': 'generic.jpg',
    'Performing & Visual Arts': 'perform.jpg',
    "Ballet": 'perform.jpg',
    "Comedy": 'perform.jpg',
    "Craft": 'perform.jpg',
    "Dance": 'perform.jpg',
    "Fine Art": 'perform.jpg',
    "Literary Arts": 'perform.jpg',
    "Musical": 'perform.jpg',
    "Orchestra": 'perform.jpg',
    "Theatre": 'perform.jpg',
    'Religion & Spirituality': 'spiritual.jpg',
    "Buddhism": 'spiritual.jpg',
    "Christianity": 'spiritual.jpg',
    "Eastern Religion": 'spiritual.jpg',
    "Islam": 'spiritual.jpg',
    "Judaism": 'spiritual.jpg',
    "Mormonism": 'spiritual.jpg',
    "Mysticism and Occult": 'spiritual.jpg',
    "New Age": 'spiritual.jpg',
    "Sikhism": 'spiritual.jpg',
    'Science & Technology': 'science.jpg',
    "Biotech": 'science.jpg',
    "High Tech": 'science.jpg',
    "Medicine": 'science.jpg',
    "Mobile": 'science.jpg',
    "Robotics": 'science.jpg',
    "Science": 'science.jpg',
    "Social Media": 'science.jpg',
    'Seasonal & Holiday': 'holiday.jpg',
    "Channukah": 'holiday.jpg',
    "Christmas": 'holiday.jpg',
    "Easter": 'holiday.jpg',
    "Fall events": 'holiday.jpg',
    "Halloween/Haunt": 'holiday.jpg',
    "Independence Day": 'holiday.jpg',
    "New Years Eve": 'holiday.jpg',
    "St Patricks Day": 'holiday.jpg',
    "Thanksgiving": 'holiday.jpg',
    'Sports & Fitness': 'sport.jpg',
    "Baseball": 'sport.jpg',
    "Basketball": 'sport.jpg',
    "Cycling": 'sport.jpg',
    "Exercise": 'sport.jpg',
    "Fighting & Martial Arts": 'sport.jpg',
    "Football": 'sport.jpg',
    "Golf": 'sport.jpg',
    "Hockey": 'sport.jpg',
    "Motorsports": 'sport.jpg',
    "Mountain Biking": 'sport.jpg',
    "Obstacles": 'sport.jpg',
    "Rugby": 'sport.jpg',
    "Running": 'sport.jpg',
    "Snow Sports": 'sport.jpg',
    "Soccer": 'sport.jpg',
    "Swimming & Water Sports": 'sport.jpg',
    "Tennis": 'sport.jpg',
    "Volleyball": 'sport.jpg',
    "Walking": 'sport.jpg',
    "Yoga": 'sport.jpg',
    'Travel & Outdoor': 'travel.jpg',
    "Canoeing": 'travel.jpg',
    "Climbing": 'travel.jpg',
    "Hiking": 'travel.jpg',
    "Kayaking": 'travel.jpg',
    "Rafting": 'travel.jpg',
    "Travel": 'travel.jpg',
    "Avatar": 'avatar.png'
}