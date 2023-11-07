
# Used for toggling between the full corpus and only novels in clean.ipynb
non_novels = ['ANAUTOBIOGRAPHY.txt','LIFEOFCICEROVolI.txt','THELIFEOFCICEROVol2.txt','THEWESTINDIESANDTHESPANISHMAIN.txt','THECOMMENTARIESOFCAESAR.txt', 'NORTHAMERICAVOLUMEI.txt', 'NORTHAMERICAVOLUMEII.txt',]

# Useful for large amounts of text that is not removed programmatically, for example editorial introductions and tables of content that are missed.
remove_above_strings = ['Nina Balatka was a maiden of Prague','In the year 1850 the two estates','In writing these pages']

# Useful for large amounts of text that is not removed programmatically, for example advertisements at the end of books.
remove_below_strings = ['the birthplace of Homer.',]

# For random publishing information not removed programmatically.
publishers = ['London: Printed by William Clowes and Sons,\nStamford Street and Charing Cross.', 'London:\nChapman and Hall, 193, Piccadilly.\n1863.', 'Printed by J. S. Virtue, City Road, London.', 'Westminster:\nJ. B. Nichols and Sons, Printers.\n25, Parliament Street.', 'London:\nChapman and Hall (Limited),\n11, Henrietta Street, Covent Garden.\n1881.', 'William Blackwood and Sons\nEdinburgh and London\nMDCCCLXXXIV', 'London:\nMacMillan and Co.\n1879.\nThe Right of Translation and Reproduction is Reserved.\nCharles Dickens and Evans,\nCrystal Palace Press.', 'London:\nSmith, Elder & Co., 15, Waterloo Place.\n1870.', 'London:\nHurst and Blackett, Publishers,\n13, Great Marlborough Street.\n1871.', 'London:\nR. Clay, Sons, and Taylor, Printers,\nBread Street Hill.', 'London: Printed by William Clowes and Sons,\nStamford Street and Charing Cross.', 'London:\nChapman and Hall, 193, Piccadilly.\n1863.','London:\nChapman and Hall, Limited, 193, Piccadilly.\n1881.', 'London:\nChapman and Hall, 193, Piccadilly.\n1874.', 'London:\nPrinted by Virtue and Co.,\nCity Road.', 'London:\nHurst and Blackett, Publishers,\n13, Great Marlborough Street.\n1871', 'London:\nChapman & Hall, 193, Piccadilly.\n1866.', 'London:\nChapman & Hall, 193, Piccadilly.\n1859.', 'London: Printed by William Clowes and Sons, Stamford Street',]

# For random strings not removed programmatically.
short_scraps = ['"The Warden", "Barchester Towers," "Orley Farm," "The Small House at\nArlington", "The Eustace Diamonds," &c., &c.', 'A Tale of Australian Bush-Life.', 'With Illustrations', 'produced from images', 'available at The Internet Archive)', 'Author of', 'Meet Each Other at Ullathorne\nEncouraged by the Press\nWarden of the Hospital', 'Joseph E. Loewenstein, M.D.', 'generously made available by the Google Books Library Project:', 'was re-published a decade later.', 'Editorial Note:', 'the PG Online Distributed Proofreading Team', 'Reprinted from the "Cornhill Magazine."', '(http://www.pgdp.net)', '(http://www.pgdp.net/)', 'line:&c., &c.', 'With an Introduction by Algar Thorold', 'London & New York: MCMVI', '         Mountains.\n            Omnium.', 'produced from images available at The Internet Archive)', '"Barchester Towers," "Castle Richmond," "Orley Farm," Etc.','and revised by','revised by Rita Bailey and', ', and Delpine Lettau', 'by Marcus Stone', 'Contents:','the people at Distributed Proofreading', 'The right of Translation is reserved.', 'The original illustrations were generously provided by\nInternet Archive (https://archive.org).', ' by F. A. Fraser', ' "Framley Parsonage," etc.', ' "Framley Parsonage," "The Last Chronicle of Barset,"\n&c. &c.', ' available at Google Books)', ' Rita Bailey and','produced from scanned images of public domain material\nfrom the Google Books project.)','produced from scanned images of public domain material\nfrom the Google Books project.)', 'The following Authors, by various Contributors, are in preparation:--','The Kellys and the O’Kellys\n\nor, Landlords and Tenants', ' "Dr. Thorne," "Orley Farm," "Miss Mackenzie,"\n"Can You Forgive Her?" Etc.', 'Born London, April 24, 1815 Died London, December 6, 1882','generously made available by the Google Books Library Project\n(https://books.google.com)', ' "Barchester Towers," "Doctor Thorne,"\n"The Bertrams," etc.','Obvious printer errors have been corrected. Otherwise, the author\'s\noriginal spelling, punctuation and hyphenation have been left intact.']

# For longer strings not removed programmatically.
long_scraps = ['Trollope is believed to have written _An Eye for an Eye_ in 1870, but\nhe did not publish it until the fall of 1878, when it appeared in\nserial form in the _Whitehall Review_, followed by publication of the\nentire book in 1879. The reason for delaying publication is unknown,\nalthough Trollope might have been concerned about the book\'s reception\nby the public, given its subject matter and the hostile reception in\n1853 of Elizabeth Gaskell\'s _Ruth_, which dealt with the same subject.', '   This story, "An Old Man\'s Love," is the last\n   of my father\'s novels. As I have stated in the\n   preface to his Autobiography, "The Landleaguers"\n   was written after this book, but was never fully\n   completed.','This book is about the seduction of a young girl by the heir to an\nearldom, the resulting illegitimate pregnancy, and the young nobleman\'s\nstruggle to decide whether to marry or to abandon the girl--certainly\nnot the usual content of Victorian novels.','Originally published in serial form May through December, 1882, in\n_Good Words_ and in book form in 1882. Trollope died during the last\nmonth of serial publication.',]


def convert_to_camel_case(novel_name):
    # Define a mapping of uppercase words to camel case
    mapping = {
        'ARRONTROW': 'Arron Trow',
        'DOCTORTHORNE': 'Doctor Thorne',
        'HOUSEOFHEINEBROTHERSINMUNICH': 'House Of Heine Brothers In Munich',
        'GEORGEWALKERATSUEZ': 'George Walker At Suez',
        'THEMANWHOKEPTHISMONEYINABOX': 'The Man Who Kept His Money In A Box',
        'THECHURCHOFENGLAND': 'The Church Of England',
        'SIRHARRYHOTSPUROFHUMBLETHWAITE': 'Sir Harry Hotspur Of Humblethwaite',
        'ARIDEACROSSPALESTINE': 'A Ride Across Palestine',
        'LINDATRESSEL': 'Linda Tressel',
        'ORLEYFARM': 'Orley Farm',
        'BARCHESTERTOWERS': 'Barchester Towers',
        'CASTLERICHMOND': 'Castle Richmond',
        'FRAMLEYPARSONAGE': 'Framley Parsonage',
        'LORDPALMERSTON': 'Lord Palmerston',
        'STRUGGLESOFBROWNJONESANDROBINSON': 'Struggles Of Brown Jones And Robinson',
        'THELASTCHRONICLEOFBARSET': 'The Last Chronicle Of Barset',
        'THELANDLEAGUERS': 'The Land Leaguers',
        'WHYFRAUFROHMANNRAISEDHERPRICES': 'Why Frau Frohmann Raised Her Prices',
        'ANUNPROTECTEDFEMALEATTHEPYRAMIDS': 'An Unprotected Female At The Pyramids',
        'THEMISTLETOEBOUGH': 'The Mistletoe Bough',
        'HARRYHEATHCOTEOFGANGOIL': 'Harry Heathcote Of Gangoil',
        'HUNTINGSKETCHES': 'Hunting Sketches',
        'THECLAVERINGS': 'The Claverings',
        'PHINEASFINN': 'Phineas Finn',
        'TALESOFALLCOUNTRIES': 'Tales Of All Countries',
        'JOHNCALDIGATE': 'John Caldigate',
        'THEBELTONESTATE': 'The Belton Estate',
        'KEPTINTHEDARK': 'Kept In The Dark',
        'LAMEREBAUCHE': 'La Mere Bauche',
        'AARONTROW': 'Aaron Trow',
        'LOTTASCHMIDTandOTHERSTORIES': 'Lotta Schmidt And Other Stories',
        'JOHNBULLONTHEGUADALQUIVIR': 'John Bull On The Guadalquivir',
        'THEWAYWELIVENOW': 'The Way We Live Now',
        'COUSINHENRY': 'Cousin Henry',
        'THEEUSTACEDIAMONDS': 'The Eustace Diamonds',
        'THETHREECLERKS': 'The Three Clerks',
        'THEAMERICANSENATOR': 'The American Senator',
        'LADYANNA': 'Lady Anna',
        'THEWARDEN': 'The Warden',
        'THESMALLHOUSEATALLINGTON': 'The Small House At Allington',
        'ANEYEFORANEYE': 'An Eye For An Eye',
        'RALPHTHEHEIR': 'Ralph The Heir',
        'MARIONFAY': 'Marion Fay',
        'HEKNEWHEWASRIGHT': 'He Knew He Was Right',
        'TRAVELLINGSKETCHES': 'Travelling Sketches',
        'CHRISTMASATTHOMPSONHAL': 'Christmas At Thompson Hal',
        'LAVENDEE': 'La Vendee',
        'MISSMACKENZIE': 'Miss Mackenzie',
        'CANYOUFORGIVEHER': 'Can You Forgive Her',
        'THECHATEAUOFPRINCEPOLIGNAC': 'The Chateau Of Prince Polignac',
        'RETURNINGHOME': 'Returning Home',
        'THECOURTSHIPOFSUSANBELL': 'The Courtship Of Susan Bell',
        'MISSSARAHJACKOFSPANISHTOWN': 'Miss Sarah Jack Of Spanish Town',
        'RACHELRAY': 'Rachel Ray',
        'THEPRIMEMINISTER': 'The Prime Minister',
        'NINABALATKA': 'Nina Balatka',
        'THEFIXEDPERIOD': 'The Fixed Period',
        'THEGOLDENLIONOFGRANPERE': 'The Golden Lion Of Granpere',
        'PHINEASREDUX': 'Phineas Redux',
        'THEMACDERMOTSOFBALLYCLORAN': 'The Macdermots Of Ballycloran',
        'THEVICAROFBULLHAMPTON': 'The Vicar Of Bullhampton',
        'THACKERAY': 'Thackeray',
        'THEBERTRAMS': 'The Bertrams',
    }
    # Return the camel case version of the novel name, if it exists in the mapping
    return mapping.get(novel_name, novel_name)





